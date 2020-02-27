from account_counter import AccountCounter

if __name__ == '__main__':
    ac = AccountCounter()
    result = ac.count_accounts(page_size=2000,
                               estimated_max=100000,
                               verbose=False,
                               simulate=False,
                               total_accounts=None)
    print(f"There's {result['n_accounts']} accounts in the database. I got it throwing {result['requests_used']} requests.")
