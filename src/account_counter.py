import requests
import math


class AccountCounter:
	def __init__(self, estimated_max):
		self.estimated_max = estimated_max

	@staticmethod
	def throw_request(page_size, page_number, total):
		if page_size < 0 or page_number < 0:
			return {"message": "unprocessable entity"}

		last_account = page_size * (page_number+1)
		if last_account == 0:
			return {}

		first_account = page_size * page_number
		
		if last_account > total:
			if first_account > total:
				return {}
			last_account = total

		return {str(i): i for i in range(first_account, last_account)}

	@staticmethod
	def throw_real_request(page_size, page_number, total=None):
		url = "https://badger-staging-2-pr-2699.herokuapp.com/api/accounts?"
		params = {'pageSize': page_size, 'pageNumber': page_number}
		if total is not None:
			params['Total'] = total
		r = requests.get(url=url, params=params)
		return r.json()

	def count_accounts(self, page_size, verbose=False, simulate=False, total_accounts=None):
		if page_size <= 0:
			raise ValueError('Page size cannot be lower than 0')

		current_min = 0
		current_max = math.ceil(self.estimated_max / page_size)

		range_finished = False

		records = {	
			'latest_page': None,
			'latest_page_has_result': None,
			'latest_highest_acc': None,
			'lowest_page_without_response': None,
			'highest_page_with_response': None
		}

		result = {
			'n_accounts': None,
			'requests_used': None
		}

		requests_throwed = 0

		while not range_finished:
			request_page = int((current_max - current_min) / 2) + current_min
			range_finished = request_page == records['latest_page']
			
			if verbose:
				print(f"range: {current_min}-{current_max} | request page: {request_page} | latest_page: {records['latest_page']} | range_finished: {range_finished}")  # | last page_has_results: {records['latest_page_has_result']}")
			
			if range_finished:
				raise Exception(f"Could'n get number of registers after {requests_throwed} requests. Try incrementing estimated_max.")

			if simulate:
				response = self.throw_request(page_size=page_size, page_number=request_page, total=total_accounts)
			else:
				response = self.throw_real_request(page_size=page_size, page_number=request_page, total=total_accounts)
			

			requests_throwed+=1
			
			if response:
				records['highest_page_with_response'] = request_page
				
				if verbose: print("\tFound response in this page range.")
				
				highest_account = sorted(response.items(), key=lambda x: x[1] )[-1][1]

				if records['latest_page'] is not None:
					if request_page == records['latest_page']-1 and not records['latest_page_has_result']:
						result['n_accounts'] = int(highest_account)+1
						result['requests_used'] = requests_throwed
						return result

				if records['lowest_page_without_response'] is not None:
					if request_page == records['lowest_page_without_response']-1:
						result['n_accounts'] = int(highest_account)+1
						result['requests_used'] = requests_throwed
						return result

				records['latest_page'] = request_page
				records['latest_page_has_result'] = True
				records['latest_highest_acc'] = highest_account

				if len(response) < page_size:
					result['n_accounts'] = int(records['latest_highest_acc'])+1
					result['requests_used'] = requests_throwed
					return result

				current_min = request_page

			else:
				if verbose: print("\tResponse NOT found in this page range.")
				records['lowest_page_without_response'] = request_page



				if request_page == 0:
					result['n_accounts'] = 0
					result['requests_used'] = requests_throwed
					return result

				if records['latest_page'] is not None:
					if request_page == records['latest_page']+1 and records['latest_page_has_result']:
						result['n_accounts'] = int(records['latest_highest_acc'])+1
						result['requests_used'] = requests_throwed
						return result

				if records['highest_page_with_response'] is not None:
					if request_page == records['highest_page_with_response']+1:
						result['n_accounts'] = int(records['latest_highest_acc'])+1
						result['requests_used'] = requests_throwed
						return result
					
				records['latest_page'] = request_page
				records['latest_page_has_result'] = False
				records['latest_highest_acc'] = None
				current_max = request_page