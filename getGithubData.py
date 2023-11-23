#!/usr/bin/python

from github import Github
from github import Auth

import datetime
import sys

def generate_new_timeline_entry_for_release(filename, date, title, content, url, repository):
  with open('content/timeline/generated-' + filename, 'a') as f:
    f.write('---\n')
    f.write('title: "' + repository+ ' ' + title + '"\n')
    f.write('draft: false\n')
    f.write('type: "timeline"\n')
    f.write('date: "' + date + '"\n')
    f.write('---\n')
    f.write(content[0:250] + '\n\n[Read more](' + url + ')')

def generate_issue_entry(entries, issue):
  entry = ""
  entry += '- ['
  if (issue.state == 'closed'):
    entry += 'X'
  else:
    entry += ' '
  entry += '] ['
  entry += issue.title
  entry += ']('
  entry += issue.html_url
  entry += ')'
  entry += '\n'
  entries.append(entry)

def generate_new_milestone(milestone):
  msTitle = mstone.title
  msNumber = str(mstone.number)
  totalCount = 0
  openCount = 0
  closedCount = 0
  entries = []

  # first list the open issues
  issues = repo.get_issues(milestone=mstone, state='open')  
  openCount = issues.totalCount
  totalCount += issues.totalCount
  for issue in issues:
    generate_issue_entry(entries, issue)

  # then the closed ones
  issues = repo.get_issues(milestone=mstone, state='closed')
  closedCount = issues.totalCount
  totalCount += issues.totalCount
  for issue in issues:
    generate_issue_entry(entries, issue)
  
  print("Total Issue Count: " + str(totalCount) + " / Open Issues: " + str(milestone.open_issues))

  if (totalCount > 0):
    with open('content/roadmap/generated-milestone-' + msTitle + '.md', 'a') as f:
      f.write('---\n')
      f.write('title: "Milestone ' + msTitle + '"\n')
      f.write('draft: false\n')
      f.write('type: "roadmap"\n')
      f.write('date: "')
      f.write(str(datetime.datetime.now().year))
      f.write('-')
      f.write(str(datetime.datetime.now().month))
      f.write('-')
      f.write(str(datetime.datetime.now().day))
      f.write('"\n')
      f.write('---\n')
      f.write('Milestone **[' + msTitle + '](https://github.com/KaotoIO/kaoto-next/milestone/' + msNumber + ')** ')
      progress = str(round(100*(totalCount - milestone.open_issues)/totalCount))
      f.write('![](https://geps.dev/progress/')
      f.write(progress)
      f.write('?dangerColor=800000&warningColor=ff9900&successColor=006600)')
      f.write('   (Open: ' + str(openCount) + '  Closed: ' + str(closedCount) + ') \n\n')
      f.write('**Expected delivery:** ')
      f.write(milestone.due_on.strftime("%m/%d/%Y"))
      f.write('\n\n')
      f.write('**Description**\n')
      f.write("```\n")
      f.write(milestone.description)
      f.write('\n```\n')
      f.write('**Issues**\n')

      for entry in entries:
        f.write(entry)
      f.write('---\n')

stargazers = []
mergedprs = 0
forks = 0
contributors = []

# using an access token
auth = Auth.Login(sys.argv[1], sys.argv[2])

# for local test purposes...please keep it here
#auth = Auth.Token(sys.argv[1])

# Public Web Github
g = Github(auth=auth)
g.get_user().login
org = g.get_organization("KaotoIO")
org.login

repositories = org.get_repos()
print("Processing repositories...")
for repo in repositories:
  print("Processing " + repo.name)
  
  # we are atm only interested in milestones of Kaoto-Next
  if repo.name == "kaoto-next":

    #milestones
    milestones = repo.get_milestones()
    for mstone in milestones:
      if mstone.state == "open":
        generate_new_milestone(mstone)

  # but we want to aggregate the remaining stats from all repos in the org  

  #releases
  releases = repo.get_releases()
  for release in releases:
      if (not (release.published_at is None)):
        generate_new_timeline_entry_for_release('release-' + str(release.published_at) + '.md', str(release.published_at), release.title, release.body, release.html_url, repo.name)

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