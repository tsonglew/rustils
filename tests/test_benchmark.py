"""Benchmark tests for rustils"""
import pytest
from rustils import str_to_bool, py_str_to_bool, point3d_distance, py_point3d_distance

# Test data for string to bool conversion
STR_TO_BOOL_CASES = [
    "true",
    "false",
    "yes",
    "no",
    "1",
    "0",
    "on",
    "off"
]

# Test data for 3D point distance calculation
POINT3D_CASES = [
    ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),  # Simple case
    ((1.5, 2.7, 3.9), (4.2, 5.6, 6.8)),  # Floating point case
    ((-1.0, -2.0, -3.0), (1.0, 2.0, 3.0)),  # Negative numbers
    ((10.5, 20.5, 30.5), (40.5, 50.5, 60.5)),  # Larger numbers
]

def test_benchmark_str_to_bool_rust(benchmark):
    """Benchmark Rust implementation of str_to_bool"""
    def run_conversion():
        for case in STR_TO_BOOL_CASES:
            str_to_bool(case)
    benchmark(run_conversion)

def test_benchmark_str_to_bool_python(benchmark):
    """Benchmark Python implementation of str_to_bool"""
    def run_conversion():
        for case in STR_TO_BOOL_CASES:
            py_str_to_bool(case)
    benchmark(run_conversion)

def test_benchmark_point3d_distance_rust(benchmark):
    """Benchmark Rust implementation of point3d_distance"""
    def run_distance():
        for p1, p2 in POINT3D_CASES:
            point3d_distance(p1, p2)
    benchmark(run_distance)

def test_benchmark_point3d_distance_python(benchmark):
    """Benchmark Python implementation of point3d_distance"""
    def run_distance():
        for p1, p2 in POINT3D_CASES:
            py_point3d_distance(p1, p2)
    benchmark(run_distance)

def test_benchmark_str_to_bool_single_rust(benchmark):
    """Benchmark single call to Rust str_to_bool"""
    benchmark(str_to_bool, "true")

def test_benchmark_str_to_bool_single_python(benchmark):
    """Benchmark single call to Python str_to_bool"""
    benchmark(py_str_to_bool, "true")

def test_benchmark_point3d_single_rust(benchmark):
    """Benchmark single call to Rust point3d_distance"""
    p1, p2 = POINT3D_CASES[0]
    benchmark(point3d_distance, p1, p2)

def test_benchmark_point3d_single_python(benchmark):
    """Benchmark single call to Python point3d_distance"""
    p1, p2 = POINT3D_CASES[0]
    benchmark(py_point3d_distance, p1, p2)
