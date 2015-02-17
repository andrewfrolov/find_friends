#!/usr/bin/env python
"""
Tester module for Vkontakte downloader.
Uses download.py
Tests the main function calls,
like vk('users.get', 137589139)
"""
__author__ = 'Yuliy Lobarev'
__name__='Tester module for Vkontakte downloader'
from prototype.vk.download import vk, getfriends
import time
import json
import io
#import sys
#import os
#import download
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
output = {}
output['users.get'] = {37740532: vk('users.get', 37740532)}
time.sleep(0.36)
output['friends.get'] = {37740532: vk('friends.get', 37740532)}
time.sleep(0.36)
output['groups.getById'] = {38463621: vk('groups.getById', 38463621)}
time.sleep(0.36)
output['wall.get'] = {37740532: vk('wall.get', 37740532)}
# print(vk('wall.get', 9393002)) Get an error, wall isn't accessible
time.sleep(0.36)
output['getfriends()'] = {37740532: getfriends(37740532)}

with open('tester.json', 'w') as f:
    json.dump(output, f, indent=4)
print('Hurray, something was dumped!')