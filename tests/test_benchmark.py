import pytest
from rustils import str_to_bool, py_str_to_bool

TEST_CASES = [
    "true", "false",
    "True", "False",
    "1", "0",
    "yes", "no",
    "Y", "N",
    "on", "off"
]

def test_implementations_match():
    """Ensure both implementations return the same results"""
    for test_case in TEST_CASES:
        assert str_to_bool(test_case) == py_str_to_bool(test_case)

def test_benchmark_rust(benchmark):
    """Benchmark Rust implementation"""
    def run_rust():
        for test_case in TEST_CASES:
            str_to_bool(test_case)
    benchmark(run_rust)

def test_benchmark_python(benchmark):
    """Benchmark Python implementation"""
    def run_python():
        for test_case in TEST_CASES:
            py_str_to_bool(test_case)
    benchmark(run_python)

def test_benchmark_single_rust(benchmark):
    """Benchmark single call to Rust implementation"""
    benchmark(str_to_bool, "true")

def test_benchmark_single_python(benchmark):
    """Benchmark single call to Python implementation"""
    benchmark(py_str_to_bool, "true")
