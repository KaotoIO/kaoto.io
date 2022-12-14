#!/usr/bin/python

import sys
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


print("Processing releases...\n")
data = requests.get('https://api.github.com/repos/KaotoIO/kaoto-ui/releases')
for release in data.json():
    print (release)
    generate_new_entry('release-' + release['published_at'] + '.md', release['published_at'],  release['name'], release['body'], release['html_url'])
data = requests.get('https://api.github.com/repos/KaotoIO/kaoto-backend/releases')
for release in data.json():
    generate_new_entry('release-' + release['published_at'] + '.md', release['published_at'], release['name'], release['body'], release['html_url'])
  
stargazers = []
mergedprs = 0
forks = 0
contributors = []
authentication = HTTPBasicAuth( sys.argv[1],  sys.argv[2])
repositories = requests.get('https://api.github.com/orgs/KaotoIO/repos', auth = authentication)
for repo in repositories.json():
  # followers
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/stargazers', auth = authentication)
  for stargazer in data.json():
      if stargazer['login'] not in stargazers: stargazers.append(stargazer['login'])
  # merged pr
  data = requests.get('https://api.github.com/search/issues?q=repo:' + repo['full_name'] + '+is:pr+is:merged', auth = authentication)
  mergedprs = mergedprs + data.json()['total_count']
  # forks
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/forks?per_page=100', auth = authentication)
  forks = forks + len(data.json())
  # contributors
  data = requests.get('https://api.github.com/repos/' + repo['full_name'] + '/contributors', auth = authentication)
  for contributor in data.json():
      if contributor['id'] not in contributors: contributors.append(contributor['id'])

with open('content/timeline/_index.md', 'a') as f:
  f.write('\n\n ## Some Cross-Project statistics')
  f.write('\n\nForks: ' + str(forks))
  f.write('\n\nMerged Pull Requests: ' + str(mergedprs))
  f.write('\n\nTotal number of unique followers: ' + str(len(stargazers)))
  f.write('\n\n ## Timeline')

with open('/content/timeline/generated-contributor-total.md', 'a') as f:
  f.write('---')
  f.write('\ntitle: Total number of contributors')
  f.write('\ndraft: false')
  f.write('\ntype: timeline')
  f.write('\ndate: "$(date)')
  f.write('\n---')
  f.write('\nWe have ' + str(len(contributors)) + ' individuals contributing to Kaoto.')
    
