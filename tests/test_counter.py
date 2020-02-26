import pytest
import sys

sys.path.append('..')
from src.account_counter import AccountCounter


@pytest.fixture()
def estimated_max():
    return 999999


@pytest.fixture()
def account_counter(estimated_max):
    return AccountCounter(estimated_max)


@pytest.mark.parametrize("test_input,expected", [
    # (page_size, verbose, simulate, total_accounts)
    ((5, False, False, 5), 5),
    ((2000, False, False, 5), 5),
    ((5, False, False, 2000), 2000),
    ((2000, False, False, 2000), 2000),
    ((5, False, False, 0), 0),
    ((-5, False, False, 5), 'value_error'),
    ((0, False, False, 5), 'value_error'),
])
def test_account_counter(account_counter, test_input, expected):
    count = None
    try:
        response = account_counter.count_accounts(*test_input)
        count = response['n_accounts']
    except ValueError as e:
        count = 'value_error'
    assert count == expected
