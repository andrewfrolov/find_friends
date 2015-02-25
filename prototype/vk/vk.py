#!/usr/bin/env python
"""
Main module for Vkontakte downloader.
Works with Python 3.4
Uses download.py
"""
__author__ = 'Yuliy Lobarev'
__name__ = 'Main module for Vkontakte downloader'
from prototype.vk.download import vk, getfriends
import time
import json

def query_user(friends_list):
    full_output = {}
    for friend in friends_list:
        print('Collecting data for ', friend) # Some debugging
        time.sleep(0.36)
        output = {'user': vk('users.get', friend)}
        time.sleep(0.36)
        output['friends'] = vk('friends.get', friend)
        time.sleep(0.36)
        output['wall'] = vk('wall.get', friend)
        full_output[friend] = output
    return full_output

def extract_friends(big_list):
    all_friends = set()
    for key in big_list:
        all_friends = all_friends | set(big_list[key]['friends']['items'])
    return  all_friends

start_user = 179976680 # User to start with. Not many friends...
friends_list = vk('friends.get', start_user)['items'] # Initial list.
big_list = query_user(friends_list) # Gather all information from persons from the list
all_friends = extract_friends(big_list) # Create set of friend for future work
almost_all_friends = all_friends - set(friends_list) # Remove people from big list
second_order = query_user(sorted(almost_all_friends)) # Collect information from the bigger second order list


with open('vk2.json', 'w') as f:
    json.dump(second_order, f, indent=4)
print('Hurray, something was dumped!')

