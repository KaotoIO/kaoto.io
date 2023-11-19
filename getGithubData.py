#!/usr/bin/python

from github import Github
from github import Auth

import datetime
import sys

def generate_new_entry(filename, date, title, content, url):
  with open('content/timeline/generated-' + filename, 'a') as f:
    f.write('---\n')
    f.write('title: ' + title + '\n')
    f.write('draft: false\n')
    f.write('type: "timeline"\n')
    f.write('date: ' + date + '\n')
    f.write('---\n')
    f.write(content[0:250] + '\n\n[Read more](' + url + ')')

def generate_new_milestone(milestone):
  issues = repo.get_issues(milestone=mstone, state='all')
  msTitle = mstone.title
  msNumber = str(mstone.number)
  print("Total Issue Count: " + str(issues.totalCount) + " / Open Issues: " + str(milestone.open_issues))

  if (issues.totalCount > 0):
    with open('content/roadmap/generated-milestone-' + msTitle + '.md', 'a') as f:
        f.write('---\n')
        f.write('title: Milestone ' + msTitle + '\n')
        f.write('draft: false\n')
        f.write('type: "roadmap"\n')
        f.write('date: ')
        f.write(str(datetime.datetime.now().year))
        f.write('-')
        f.write(str(datetime.datetime.now().month))
        f.write('-')
        f.write(str(datetime.datetime.now().day))
        f.write('\n')
        f.write('---\n')
        f.write('Milestone **[' + msTitle + '](https://github.com/KaotoIO/kaoto-next/milestone/' + msNumber + ')** ')
        
        progress = str(round(100*(issues.totalCount - milestone.open_issues)/issues.totalCount))
        f.write('![](https://geps.dev/progress/')
        f.write(progress)
        f.write('?dangerColor=800000&warningColor=ff9900&successColor=006600)\n\n')
        
        for issue in issues:
          f.write(' - *')
          f.write(issue.state)
          f.write('* ')
          if (issue.state == 'closed'):
            f.write('~~')
          f.write('[')
          f.write(issue.title)
          f.write('](')
          f.write(issue.html_url)
          f.write(')')
          if (issue.state == 'closed'):
            f.write('~~')
          f.write('\n')

stargazers = []
mergedprs = 0
forks = 0
contributors = []

# using an access token
auth = Auth.Login(sys.argv[1], sys.argv[2])

# Public Web Github
g = Github(auth=auth)
g.get_user().login
org = g.get_organization("KaotoIO")
org.login

repositories = org.get_repos()
print("Processing repositories...")
for repo in repositories:
  print("Processing " + repo.name)
  
  # we are atm only interested in releases and milestones of Kaoto-Next
  if repo.name == "kaoto-next":

    #releases
    releases = repo.get_releases()
    for release in releases:
        if (not (release.published_at is None)):
          generate_new_entry('release-' + str(release.published_at) + '.md', str(release.published_at), release.title, release.body, release.html_url)
    
    #milestones
    milestones = repo.get_milestones()
    for mstone in milestones:
      if mstone.state == "open":
        generate_new_milestone(mstone)

  # but we want to aggregate the remaining stats from all repos in the org  
  
  # followers
  gazers = repo.get_stargazers()
  for stargazer in gazers:
      if stargazer.login not in stargazers: 
         stargazers.append(stargazer.login)
      
  # merged pr
  PRs = repo.get_pulls(state='closed')
  mergedprs = mergedprs + PRs.totalCount
  
  # forks
  repoForks = repo.get_forks()
  forks = forks + repoForks.totalCount

  # contributors
  contribs = repo.get_contributors()
  for contributor in contribs:
      if contributor.id not in contributors: 
         contributors.append(contributor.id)

g.close()