import base64
import github3
import importlib
import json
import random
import sys
import threading
import time

from datetime import datetime


def github_login():
    
    with open('mytoken.txt') as f:
        token = f.read()

    # Login to github
    user = 'JonArbuckle0'
    sess = github3.login(token=token)
    # return the trojan repository
    return sess.repository(user, 'trojaning')
