import os
import unittest
from tests.security_tests import security_tests
from utils.evaluator import evaluate_security
from utils.report_generator import generate_excel_report
import config

# Import adapters
from adapters.openai_adapter import OpenAIAdapter
from adapters.huggingface_adapter import HuggingFaceAdapter
from adapters.cohere_adapter import CohereAdapter

# Unit Test Class
class TestLLMSecurity(unittest.TestCase):
    results = []

    def run_security_test(self, llm_backend, test_case, llm_name):
        # Skip test types not enabled
        if test_case["type"] not in config.RUN_TEST_TYPES:
            return
        response = llm_backend.call(test_case["prompt"])
        score = evaluate_security(response)
        status = "PASS" if score == 2 else "FAIL"
        TestLLMSecurity.results.append({
            "LLM": llm_name,
            "ID": test_case["id"],
            "Type": test_case["type"],
            "Name": test_case["name"],
            "Prompt": test_case["prompt"],
            "Response": response,
            "Score": score,
            "Expected_Behavior": test_case["expected_behavior"],
            "Status": status
        })
        self.assertEqual(score, 2, f"{llm_name} failed security test '{test_case['name']}'")

def create_test_method(llm_backend, test_case, llm_name):
    def test(self):
        self.run_security_test(llm_backend, test_case, llm_name)
    return test

# Configure LLMs from config.py
llm_instances = {}

if "OpenAI" in config.ENABLED_LLMs:
    llm_instances["OpenAI"] = OpenAIAdapter(model=config.OPENAI_MODEL)

if "HuggingFace" in config.ENABLED_LLMs:
    llm_instances["HuggingFace"] = HuggingFaceAdapter(model_name=config.HUGGINGFACE_MODEL)

if "Cohere" in config.ENABLED_LLMs:
    llm_instances["Cohere"] = CohereAdapter(api_key=config.COHERE_API_KEY, model=config.COHERE_MODEL)

# Dynamically create test methods for all LLMs
for llm_name, adapter in llm_instances.items():
    for test_case in security_tests:
        test_name = f"test_{llm_name}_{test_case['id']}_{test_case['name'].replace(' ', '_')}"
        setattr(TestLLMSecurity, test_name, create_test_method(adapter, test_case, llm_name))

# Run tests and generate report
if __name__ == "__main__":
    os.makedirs(config.REPORT_DIR, exist_ok=True)
    try:
        unittest.main(exit=False)
    finally:
        generate_excel_report(TestLLMSecurity.results)
