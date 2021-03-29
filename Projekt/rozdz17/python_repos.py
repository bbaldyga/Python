import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the respones
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a variable.
response_dir = r.json()
print("Total repositiories: ",response_dir['total_count'])
# Explore information about the repositories
repo_dicts = response_dir['items']
names, plot_dicts = [], []
#print("Repositories returned: ",len(repo_dicts))
# Examine the first reporitory
#print("\nSelected information about each repository:")
for repo_dist in repo_dicts:
    names.append(repo_dist['name'])
    plot_dict = {
        'value': repo_dist['stargazers_count'],
        'label': repo_dist['description'],
    }
    plot_dicts.append(plot_dict)
#repo_dicts = repo_dicts[0]
#    print("\nSelected information about first repository")
#    print("Name: ",repo_dist['name'])
#    print("Owner: ",repo_dist['owner']['login'])
#    print("Stars: ",repo_dist['stargazers_count'])
#    print("Repository: ",repo_dist['html_url'])
#    print("Created: ",repo_dist['created_at'])
#    print("Updated: ",repo_dist['updated_at'])
#    print("Descriptoin: ",repo_dist['description'])

# Make visualization
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.x_label_font_size = 14
my_config.y_labels_major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
#print("\nKeys: ",len(repo_dicts))
#for key in sorted(repo_dicts.keys()):
#    print(key)
# Process results.
#print(response_dir.keys())