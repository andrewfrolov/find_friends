#!/usr/bin/env python
"""
Vkontakte downloader module. Uses API.
"""
__author__ = 'Yuliy Lobarev'
__name__ = 'Vkontakte downloader (via API)'
import urllib.request, urllib.error, urllib.parse
import json
import sys

def vk(meth, vkid):
    """
    VK API access function.
    Don't forget to add time.sleep(0.36) between requests or VK will stop to respond!
    :vkid meth: Method to send to API.
    :vkid vkid: User ID.
    :return: Response from API.
    """
    token = '123' # If group.get method is used
    apiver = '5.28' # version of VK API
    url = 'https://api.vk.com/method/%s' % meth
    method = {
                 'friends.get': 'user_id=%s',
                 'users.get': 'user_ids=%s',
                 'wall.get': 'owner_id=%s&count=20',
                 'groups.get': 'user_id=%s&access_token=' + token, # Doesn't work without token...
                 'groups.getById': 'group_ids=%s&fields=contacts,description,members_count',
             }[meth] % vkid

    connector = urllib.request.urlopen(url + '?' + method + '&v=' + apiver).read()
    data = json.loads(connector.decode())
    if 'error' in data:
        print(data)
        return list()
    return data['response']

def get_friends(vkid):
    pass

