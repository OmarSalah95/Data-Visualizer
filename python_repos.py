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

#Examine first repo
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))

#Examine selected information repos.
print('\nSelected information on repos:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    #print('Created:', repo_dict['created_at'])
    #print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])

#for key in sorted(repo_dict.keys()):
    #print(key)


