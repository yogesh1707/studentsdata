import requests
import pytest

@pytest.mark.getrequest
def testGetrequest(apirequest):
	u=apirequest
	response = requests.get(u+'id=12')
	cd=response.status_code
	assert cd==200

def testPostBadrequest():
	response = requests.post("http://127.0.0.1:5000/students?id=a123&firstName=fn123&lastName=ln123&class=123testclass&nationality=indian")
	cd=response.status_code
	assert cd==400

def testPostrequest():
	response = requests.post("http://127.0.0.1:5000/students?id=10001&firstName=fn123&lastName=ln123&class=123testclass&nationality=indian")
	cd=response.status_code
	assert cd==200
