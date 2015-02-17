#!/usr/bin/env python
"""
Vkontakte downloader module. Uses API.
"""
__author__ = 'Yuliy Lobarev'
__name__ = 'Vkontakte downloader (via API)'
import urllib.request, urllib.error, urllib.parse
import json
import sys

def vk(meth, vkid = 0):
    """
    VK API access function.
    Don't forget to add time.sleep(0.36) between requests or VK will stop to respond!
    :vkid meth: Method to send to API.
    :vkid vkid: User ID.
    :return: Response from API as a dictionary. Check for 'items' key in the response.
    """
    token = '123' # If group.get method is used
    apiver = '5.28' # version of VK API
    url = 'https://api.vk.com/method/%s' % meth
    if vkid == 0:
        print('Sorry, no ID, exiting...')
        return list()
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

def getfriends(vkid = 0):
    """
    Function to get friends from a particular user by ID
    :param vkid: User ID.
    :return: List of friends IDs
    """
    if vkid == 0:
        print('Sorry, no ID, exiting...')
        return list()
    userlist = (vk('friends.get', vkid))
    if len(userlist) == 0:
        print('Something happened, VK API returned an error for this user.')
        print('Possibly the user prohibited access to the wall.')
        return list()
    return userlist['items']

