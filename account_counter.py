import requests

class AccountCounter():
	def __init__(self):
		pass

	def throw_request(self, hidden_number_of_docs, page_size, page_number):
		if page_size < 0 or page_number < 0:
			return {"message": "unprocessable entity"}

		last_account = page_size * (page_number+1)
		if last_account == 0:
			return {}

		first_account = page_size * (page_number)
		
		if last_account > hidden_number_of_docs:
			if first_account > hidden_number_of_docs:
				return {}
			last_account = hidden_number_of_docs

		return {str(i):i for i in range(first_account, last_account)}

	@staticmethod
	def throw_debug_request(total, page_size, page_number):
		URL = "https://badger-staging-2-pr-2699.herokuapp.com/api/accounts?"
		PARAMS = {'Total':total, 'pageSize': page_size, 'pageNumber': page_number}
		r = requests.get(url = URL, params = PARAMS) 
		data = r.json()
		return data


	@staticmethod
	def throw_real_request(page_size, page_number):
		URL = "https://badger-staging-2-pr-2699.herokuapp.com/api/accounts?"
		PARAMS = {'pageSize': page_size, 'pageNumber': page_number}
		r = requests.get(url = URL, params = PARAMS) 
		data = r.json()
		return data