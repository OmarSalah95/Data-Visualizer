import requests


#Make an API call and store it.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

#Store API response in a new variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#Process the results
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))