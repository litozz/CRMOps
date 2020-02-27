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
    ((2000, 99999,  False, USE_SIMULATED_SERVICE, 100000), 'runtime_error'),
    ((2000, 100000,  False, USE_SIMULATED_SERVICE, 100000), 'runtime_error'),
    ((2000, 100001,  False, USE_SIMULATED_SERVICE, 100000), 100000),
    ((2000, 100000,  False, USE_SIMULATED_SERVICE, 38769), 38769),
])
def test_account_counter(account_counter, test_input, expected):
    count = None
    try:
        response = account_counter.count_accounts(*test_input)
        count = response['n_accounts']
    except ValueError:
        count = 'value_error'
    except RuntimeError:
        count = 'runtime_error'
    assert count == expected
