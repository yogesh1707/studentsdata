import pytest

@pytest.fixture
def apirequest():
	url='http://127.0.0.1:5000/students?'
	return url
