import pytest
import sys

sys.path.append('..')
from src.account_counter import AccountCounter

USE_SIMULATED_SERVICE = True

@pytest.fixture()
def account_counter():
    return AccountCounter()

@pytest.mark.parametrize("test_input,expected", [
    # (page_size, estimated_max, verbose, simulate, total_accounts)
    ((5, 99999, False, USE_SIMULATED_SERVICE, 5), 5),
    ((2000, 99999,  False, USE_SIMULATED_SERVICE, 5), 5),
    ((5, 99999,  False, USE_SIMULATED_SERVICE, 2000), 2000),
    ((2000, 99999,  False, USE_SIMULATED_SERVICE, 2000), 2000),
    ((5, 99999,  False, USE_SIMULATED_SERVICE, 0), 0),
    ((-5, 99999,  False, USE_SIMULATED_SERVICE, 5), 'value_error'),
    ((0, 99999,  False, USE_SIMULATED_SERVICE, 5), 'value_error'),
])
def test_account_counter(account_counter, test_input, expected):
    count = None
    try:
        response = account_counter.count_accounts(*test_input)
        count = response['n_accounts']
    except ValueError as e:
        count = 'value_error'
    assert count == expected
