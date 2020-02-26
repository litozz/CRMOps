import requests

class AccountCounter():
	def __init__(self):
		pass

	@staticmethod
	def throw_request(page_size, page_number, hidden_number_of_docs):
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
	def throw_real_request(page_size, page_number, total=None):
		URL = "https://badger-staging-2-pr-2699.herokuapp.com/api/accounts?"
		PARAMS = {'pageSize': page_size, 'pageNumber': page_number}
		if total:
			PARAMS['Total']=total
		r = requests.get(url = URL, params = PARAMS) 
		return r.json()