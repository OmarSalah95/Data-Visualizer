import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


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

names, stars = [], []
#Examine selected information repos.
print('\nSelected information on repos:')
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Set Vislualizuals attributes
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style )
chart.title = 'Most-Starred Python Projects on Git Hub'
chart.x_labels = names
#set Y axis attributes
chart.add('', stars)
#Render to WebBrowser SVG file.
chart.render_to_file('python_repos.svg')

