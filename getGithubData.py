#!/usr/bin/python

from github import Github
from github import Auth

import datetime
import sys
import os

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

  # create the file for the milestone
  if (totalCount > 0):

    # create the folder if not existing
    path = "content/roadmap/generated-milestone-" + msTitle + "/"
    isExist = os.path.exists(path)
    if not isExist:
      os.makedirs(path)
  
    with open(path + '/index.md', 'a') as f:
      # page header
      f.write('---\n')
      f.write('title: "Kaoto ' + msTitle + '"\n')
      f.write('summary: "Check out the planned roadmap of Kaoto ' + msTitle + '"\n')
      f.write('date: ')
      f.write(str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")))
      f.write('+06:00\n')
      f.write('authors:\n')
      f.write('  - admin\n')
      f.write('tags:\n')
      f.write('  - Roadmap ' + msTitle + '\n')
      f.write('  - Kaoto ' + msTitle + '\n')
      f.write('---\n')
      # page content
      f.write('<h4>\n')
      f.write('Milestone <a href="https://github.com/KaotoIO/kaoto/milestone/' + msNumber + '"><strong>' + msTitle + '</strong></a>&nbsp;&nbsp')
      progress = str(round(100*(totalCount - milestone.open_issues)/totalCount))
      f.write('<img style="padding: 0px; display: inline;" src="https://geps.dev/progress/')
      f.write(progress)
      f.write('?dangerColor=800000&warningColor=ff9900&successColor=006600"/>')
      f.write('&nbsp;&nbsp;(Open: ' + str(openCount) + '  Closed: ' + str(closedCount) + ') \n\n')
      f.write('Expected delivery: ')
      if (milestone.due_on is None):
        f.write('Not Set')
      else:
        f.write(milestone.due_on.strftime("%m/%d/%Y"))
      f.write('\n\n')
      f.write('Description\n')
      f.write("```\n")
      f.write(milestone.description)
      f.write('\n```\n')
      f.write('Issues\n')

      for entry in entries:
        f.write(entry)
      f.write('</h4>\n')

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
