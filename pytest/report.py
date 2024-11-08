import json

def create_report():

	data = {
	"timestamp": "1245743543594",
	"date": "November 5th 2024",
	"owner": "Nishanth Hegde"
	}

	with open('test_report', 'w') as file:
		json.dump(data, file)

