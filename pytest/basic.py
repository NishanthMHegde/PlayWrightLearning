from util import sqrt

#tests should start with test_
#to see print statements, run test with pytest -s
def test_sqrt_25():
	print("Test sqrt of 25")
	assert sqrt(25) == 5

def test_sqrt_100():
	print("Test sqrt of 100")
	assert sqrt(100) == 9