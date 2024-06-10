#!/usr/bin/python

from github import Github
from github import Auth

import datetime
import sys

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
      f.write('type: "roadmap"\n')
      f.write('date: "')
      f.write(str(datetime.datetime.now().year))
      f.write('-')
      f.write(str(datetime.datetime.now().month))
      f.write('-')
      f.write(str(datetime.datetime.now().day))
      f.write('"\n')
      f.write('---\n')
      f.write('Milestone **[' + msTitle + '](https://github.com/KaotoIO/kaoto/milestone/' + msNumber + ')** ')
      progress = str(round(100*(totalCount - milestone.open_issues)/totalCount))
      f.write('![](https://geps.dev/progress/')
      f.write(progress)
      f.write('?dangerColor=800000&warningColor=ff9900&successColor=006600)')
      f.write('   (Open: ' + str(openCount) + '  Closed: ' + str(closedCount) + ') \n\n')
      f.write('**Expected delivery:** ')
      if (milestone.due_on is None):
        f.write('Not Set')
      else:
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
  
  # we are atm only interested in milestones of kaoto repo
  if repo.name == "kaoto":
    print("Generating milestones for repository: " + repo.name)
    
    #milestones
    milestones = repo.get_milestones()
    for mstone in milestones:
      if mstone.state == "open":
        generate_new_milestone(mstone)

g.close()
