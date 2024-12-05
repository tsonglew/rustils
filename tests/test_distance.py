import math
import pytest
from rustils import point3d_distance, py_point3d_distance

TEST_CASES = [
    ((0, 0, 0), (1, 0, 0), 1.0),  # Unit distance along x-axis
    ((0, 0, 0), (0, 1, 0), 1.0),  # Unit distance along y-axis
    ((0, 0, 0), (0, 0, 1), 1.0),  # Unit distance along z-axis
    ((0, 0, 0), (1, 1, 1), math.sqrt(3)),  # Equal distance in all dimensions
    ((1, 2, 3), (4, 6, 8), math.sqrt(50)),  # General case
    ((0, 0, 0), (0, 0, 0), 0.0),  # Same point
    ((-1, -1, -1), (1, 1, 1), math.sqrt(12)),  # Negative coordinates
]

def test_implementations_match():
    """Ensure both implementations return the same results"""
    for p1, p2, expected in TEST_CASES:
        rust_result = point3d_distance(p1, p2)
        py_result = py_point3d_distance(p1, p2)
        assert abs(rust_result - py_result) < 1e-10, f"Results differ for points {p1} and {p2}"

def test_distance_values():
    """Test distance calculations against known values"""
    for p1, p2, expected in TEST_CASES:
        rust_result = point3d_distance(p1, p2)
        assert abs(rust_result - expected) < 1e-10, f"Incorrect distance for points {p1} and {p2}"

def test_distance_properties():
    """Test mathematical properties of distance"""
    p1 = (1.0, 2.0, 3.0)
    p2 = (4.0, 5.0, 6.0)
    
    # Symmetry: d(a,b) = d(b,a)
    assert abs(point3d_distance(p1, p2) - point3d_distance(p2, p1)) < 1e-10
    
    # Non-negativity: d(a,b) >= 0
    assert point3d_distance(p1, p2) >= 0
    
    # Identity: d(a,a) = 0
    assert abs(point3d_distance(p1, p1)) < 1e-10

def test_benchmark_rust(benchmark):
    """Benchmark Rust implementation"""
    p1, p2, _ = TEST_CASES[4]  # Use general case for benchmarking
    benchmark(point3d_distance, p1, p2)

def test_benchmark_python(benchmark):
    """Benchmark Python implementation"""
    p1, p2, _ = TEST_CASES[4]  # Use general case for benchmarking
    benchmark(py_point3d_distance, p1, p2)
