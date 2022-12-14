#!/usr/bin/python

import sys
import datetime
import json
import requests
import subprocess as sb
from requests.auth import HTTPBasicAuth

def generate_new_entry(filename, date, title, content, url):
  with open('content/timeline/generated-' + filename, 'a') as f:
    f.write('---\n')
    f.write('title: ' + title + '\n')
    f.write('draft: false\n')
    f.write('type: "timeline"\n')
    f.write('date: ' + date + '\n')
    f.write('---\n')
    f.write(content[0:250] + '\n\n[Read more](' + url + ')')


authentication = HTTPBasicAuth( sys.argv[1],  sys.argv[2])
stargazers = []
mergedprs = 0
forks = 0
contributors = []
repositories = requests.get('https://api.github.com/orgs/KaotoIO/repos', auth = authentication)
print("Processing repositories...\n")
for repo in repositories.json():
  print("Processing " + repo['full_name'])
  #releases
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/releases', auth = authentication)
  for release in data.json():
      print(release)
      if (not (release['published_at'] is None))
        generate_new_entry('release-' + release['published_at'] + '.md', release['published_at'], release['name'], release['body'], release['html_url'])
  # followers
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/stargazers', auth = authentication)
  for stargazer in data.json():
      print(stargazer)
      if stargazer['login'] not in stargazers: stargazers.append(stargazer['login'])
  # merged pr
  data = requests.get('https://api.github.com/search/issues?q=repo:' + repo['full_name'] + '+is:pr+is:merged', auth = authentication)
  print(data.json())
  mergedprs = mergedprs + data.json()['total_count']
  # forks
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/forks?per_page=100', auth = authentication)
  print(data.json())
  forks = forks + len(data.json())
  # contributors
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/contributors', auth = authentication)
  for contributor in data.json():
      print(contributor)
      if contributor['id'] not in contributors: contributors.append(contributor['id'])

with open('content/timeline/_index.md', 'a') as f:
  f.write('\n\n ## Some Cross-Project statistics')
  f.write('\n\nForks: ' + str(forks))
  f.write('\n\nMerged Pull Requests: ' + str(mergedprs))
  f.write('\n\nTotal number of unique followers: ' + str(len(stargazers)))
  f.write('\n\n ## Timeline')

with open('content/timeline/generated-contributor-total.md', 'w') as f:
    f.write('---\n')
    f.write('title: Total number of contributors\n')
    f.write('draft: false\n')
    f.write('type: "timeline"\n')
    f.write('date: ')
    f.write(str(datetime.datetime.now()))
    f.write('\n')
    f.write('---\n')
    f.write('\nWe have ')
    f.write(str(len(contributors)))
    f.write(' individuals contributing to Kaoto.\n\n')
    
