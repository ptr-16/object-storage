import mindio
import pytest
import warnings
import logging
def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("This is a warning", UserWarning)

def test_logging(caplog):
    logging.warning("This is a log warning")
    assert "This is a log warning" in caplog.text

def test_rand_name_length():
    name = mindio.rand_name()
    assert len(name) == 7

def test_rand_data_type():
    data = mindio.rand_data()
    assert isinstance(data, str)
    assert len(data) >= 10 
