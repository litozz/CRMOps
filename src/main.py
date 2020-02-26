from account_counter import AccountCounter

if __name__ == '__main__':
    ac = AccountCounter(100000)
    count, nrequests = ac.count_accounts(page_size=2000)
    print(f"There's {count} accounts in the database. I got it throwing {nrequests} requests")
