################################## GITTY IMPORTS ############################################

from calendar import calendar
from time import time
import dotenv
from github import Github
import os, sys
from dotenv import load_dotenv
import datetime
import colorama
import github
import pickle
from dataHandler import Git as GitDataHandler
from localDebuger import Debuger

########################### GITTY FUNCTIONS AND CLASSES ############################################

Debug = Debuger("GITTY")

def CheckGitIsUse():
    return __isInit__

def __Init__():
    global __isInit__
    gitRepoName = GitDataHandler.Load("GitReposetoryName", newEntry=True) # Chaossplitter/littlealchemist
    if (__isInit__ or (gitRepoName == None)):
        return -1
    try:
        colorama.init()
    
        date1 = datetime.datetime(1970,1,1,0,0,0)
    
        load_dotenv()
        TOKEN = os.getenv('GITHUB_TOKEN')
        IND = int(os.getenv('INDICES'))
        t2 = os.getenv('TIME').replace("'","")
        time2 = datetime.timedelta(0,(int(t2)))
        TIME = date1 + time2
        g = Github(TOKEN)
    
        repo = g.get_repo(gitRepoName)
    
        commit= []
        comms = CheckCommits()
    
        for i in range(comms.totalCount):
            commit.append(str(comms[i]))
            commit[i] = commit[i].replace('Commit(sha="','')
            commit[i] = commit[i].replace('")','')
    
        __isInit__ = True
        return 0
    except Exception as _err:
        Debug.LogError("Git faild to init", _err)
        __isInit__ = False
        return 1

def __GetGitPath():
    global

class colors():
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

def truncate(num, n):
    if (not CheckGitIsUse()):
        return
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def CheckCommits():
    if (not CheckGitIsUse()):
        return
    comms = repo.get_commits(since=TIME)
    tim = datetime.datetime.now().replace(microsecond=0)
    print(f'{colors.CYAN}'+str(tim)+f'{colors.ENDC}')
    secs = int(round(tim.timestamp(), 0))
    print(f'{colors.CYAN}'+str(secs)+f'{colors.ENDC}')
    #dotenv.set_key('.env','TIME',str(secs))
    return comms

def CommitData(sha: str):
    if (not CheckGitIsUse()):
        return
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

    return auth,com,allfiles,url,sha


def CommitStatuses(c):
    if (not CheckGitIsUse()):
        return
    statuses = []
    for i in range(c.get_statuses().totalCount):
        statuses.append(c.get_statuses()[i]+'\n')
        return statuses


def CommitComments(c):
    if (not CheckGitIsUse()):
        return
    comments = []
    for i in range(c.get_statuses().totalCount):
        comments.append(c.get_statuses()[i]+'\n')
        return comments
    
def OrderFiles(f: str):
    if (not CheckGitIsUse()):
        return
    f = f.replace('File(sha="','')
    f = f.replace('"','')
    f = f.replace(' filename="','')
    f = f.replace('")','')
    return f.split(',')

def NewCommits(commit: list):
    if (not CheckGitIsUse()):
        return
    changed = False
    if True:#len(commit) != IND:
        changed = True
    return changed

class ReversableList(list):
    def rev(self):
        return list(reversed(self))

def botinfo():
    if (not CheckGitIsUse()):
        return
    changed = NewCommits(commit)
    changes = []
    l=ReversableList(commit)
    if changed:
        for i in range(len(commit)):
            changes.append(commit[i])
    dotenv.set_key('.env','INDICES',str(comms.totalCount))
    return changed, l.rev(), comms.totalCount
                            #len(commit)

#################################### GITTY INIT ############################################

__isInit__ = False
__Init__()

