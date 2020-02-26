import pytest
from account_counter import AccountCounter

@pytest.fixture()
def account_counter():
    return AccountCounter()

@pytest.mark.parametrize("test_input", [
	# (total, page_size, page_number)
	(5, 0,0),
	(5, -1,2),
	(5, 1,-2),
	(5, -1,-2),
	(5, 1,0),
	(5, 1,1),
	(5, 1,2),
	(5, 1,3),
	(5, 1,4),
	(5, 1,5),
	(5, 2,0),
	(5, 2,1),
	(5, 2,2),
	(5, 2,3),
	(5, 3,0),
	(5, 3,1),
])
def test_service_simulator(account_counter,test_input):
	assert account_counter.throw_request( *test_input ) == account_counter.throw_debug_request( *test_input )


if __name__ == '__main__':
	ac = AccountCounter()
	acinput = (5, -1,0)
	print(ac.throw_request(*acinput))
	print(ac.throw_debug_request(*acinput))
