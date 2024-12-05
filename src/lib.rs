pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

use pyo3::prelude::*;

#[pyfunction]
fn str_to_bool(s: &str) -> PyResult<bool> {
    match s.to_lowercase().as_str() {
        "true" | "1" | "yes" | "y" | "on" => Ok(true),
        "false" | "0" | "no" | "n" | "off" => Ok(false),
        _ => Err(pyo3::exceptions::PyValueError::new_err(
            format!("Cannot convert '{}' to bool", s)
        )),
    }
}

#[pymodule]
fn rustils(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(str_to_bool, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
