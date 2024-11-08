import pytest
from report import *

#add this annotation on top of function that we wish to use as fixture
#use scope as session to make this function data available for this file
#use scope as module to make this function data available for all files in this folder
#default scope is function and this allows for the function data to be used in only the calling function. Other functions have to reuse it.
@pytest.fixture(scope='session')
def generate_report():
	print("[GENERATING REPORT CALLED]: Generating the report")
	create_report()
	with open('test_report', 'r') as file:
		return json.load(file)

#send fixture name as argument to call the fixture and get its data
def test_json_generation(generate_report):
	print("[TEST JSON GENERATION CALLED]: Testing the report type")
	assert dict == type(generate_report)

def test_fields_in_report(generate_report):
	print("[TEST FIELDS In REPORT CALLED]: Testing the report fields")
	assert 'timestamp' in generate_report.keys()
	assert 'date' in generate_report.keys()
	# assert 'author' in generate_report.keys()
	assert 'owner' in generate_report.keys()

