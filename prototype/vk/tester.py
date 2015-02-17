#!/usr/bin/env python
"""
Tester module for Vkontakte downloader.
Uses download.py
"""
__author__ = 'Yuliy Lobarev'
__name__='Tester module for Vkontakte downloader'
from prototype.vk.download import vk
#import sys
#import os
#import download
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

print(vk('friends.get', 137589139))