#!/usr/bin/env python
"""
Tester module for Vkontakte downloader.
Uses download.py
Tests the main function calls,
like vk('users.get', 137589139)
"""
__author__ = 'Yuliy Lobarev'
__name__='Tester module for Vkontakte downloader'
from prototype.vk.download import vk
import time
#import sys
#import os
#import download
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

print(vk('users.get', 37740532))
time.sleep(0.36)
print(vk('friends.get', 37740532))
time.sleep(0.36)
# print(vk('groups.get', 150454703))
# time.sleep(0.36)
print(vk('groups.getById', 38463621))
time.sleep(0.36)
print(vk('wall.get', 37740532))