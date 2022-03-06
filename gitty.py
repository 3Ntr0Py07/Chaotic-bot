from calendar import calendar
from time import time
import dotenv
from github import Github
import os
from dotenv import load_dotenv
import datetime
import colorama
import github


colorama.init()

class colors():
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'


date1 = datetime.datetime(1970,1,1,0,0,0)

load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
IND = int(os.getenv('INDICES'))
t2 = os.getenv('TIME').replace("'","")
time2 = datetime.timedelta(0,(int(t2)))
TIME = date1 + time2
g = Github(TOKEN)

repo = g.get_repo("Chaossplitter/littlealchemist")

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def CheckCommits():
    comms = repo.get_commits(since=TIME)
    tim = datetime.datetime.now().replace(microsecond=0)
    print(f'{colors.CYAN}'+str(tim)+f'{colors.ENDC}')
    secs = int(round(tim.timestamp(), 0))
    print(f'{colors.CYAN}'+str(secs)+f'{colors.ENDC}')
    #dotenv.set_key('.env','TIME',str(secs))
    return comms

def CommitData(sha: str):
    c = repo.get_commit(sha)
    auth = str(c.author).replace('NamedUser(login="','')
    auth = auth.replace('")','')
    curl = str(c.comments_url)
    com = c.commit
    committer =  str(c.committer).replace('NamedUser(login="','')
    committer = committer.replace('")','')
    allfiles = []
    for i in range(len(c.files)):
        file = OrderFiles(str(c.files[i]))
        allfiles.append(file)
    url = str(c.html_url)
    parents = str(c.parents)

    return auth,curl,com,committer,allfiles,url,parents,sha


def CommitStatuses(c):
    statuses = []
    for i in range(c.get_statuses().totalCount):
        statuses.append(c.get_statuses()[i]+'\n')
        return statuses


def CommitComments(c):
    comments = []
    for i in range(c.get_statuses().totalCount):
        comments.append(c.get_statuses()[i]+'\n')
        return comments
    
def OrderFiles(f: str):
    f = f.replace('File(sha="','')
    f = f.replace('"','')
    f = f.replace(' filename="','')
    f = f.replace('")','')
    return f.split(',')

def NewCommits(commit: list):
    changed = False
    if True:#len(commit) != IND:
        changed = True
    return changed

commit= []
comms = CheckCommits()
for i in range(comms.totalCount):
    commit.append(str(comms[i]))
    commit[i] = commit[i].replace('Commit(sha="','')
    commit[i] = commit[i].replace('")','')

def botinfo():
    changed = NewCommits(commit)
    changes = []
    if changed:
        for i in range(len(commit)):
            changes.append(commit[i])
    dotenv.set_key('.env','INDICES',str(comms.totalCount))
    return changed, commit.reverse(), comms.totalCount
                            #len(commit)