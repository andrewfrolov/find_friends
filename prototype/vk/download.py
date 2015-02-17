#!/usr/bin/env python
"""
Vkontakte downloader module. Uses API.
"""
__author__ = 'Yuliy Lobarev'
__name__='Vkontakte downloader (via API)'
import urllib.request, urllib.error, urllib.parse
import json
# import sys

def vk(meth, param):
    """
    VK API access function.
    :param meth: Method to send to API.
    :param param: User ID.
    :return: Response from API.
    """
    url  = 'https://api.vk.com/method/%s' %meth
    print(url)
    method = {
        'friends.get'    : 'user_id=%s',
        'users.get'      : 'user_ids=%s' ,
        'groups.get'     : 'user_id=%s' ,
        'groups.getById' : 'group_ids=%s&fields=contacts,description,members_count',
    }[meth] % param
    print(method)
    #connector  = urllib2.urlopen(url, method).read()
    connector = urllib.request.urlopen(url, method).read()
    data = json.loads( connector)

    if 'error' in data:
        print (data)
        return list()
    return data['response']


