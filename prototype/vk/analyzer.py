#!/usr/bin/env python
"""
Analyzer module for Vkontakte downloader.
Works with Python 3.4
Uses vk.py on the first step
"""
__author__ = 'Yuliy Lobarev'
__name__ = 'Analyzer module for Vkontakte downloader'
import json

def extract_wall_items(user: str, json_handle: dict):
    """
    Function to convert JSON data for one user to a simple list.
    :param user: VK user id, as mentioned in the JSON file, as string
    :param json_handle: handle to JSON data
    :return: List of dictionaries, each dictionary has text of post, number
    of likes and reposts, "is_copy" flag
    """
    output = []
    wall_item = {}
    try:
        wall = json_handle[user]['wall']['items']
    except:
        return []  # Sometimes wall is null

    for item in wall:
        if 'copy_history' in item.keys():         # Extract text
            text = item['copy_history'][0]['text']
        else:
            text = item['text']
        wall_item['text'] = text
        wall_item['likes'] = item['likes']['count']
        wall_item['reposts'] = item['reposts']['count']
        wall_item['is_copy'] = 'copy_history' in item.keys()
        output.append(wall_item)
    return output

def extract_friends(json_handle: dict):
    """
    Extracting list of friends.
    :param json_handle: data handle
    :return: List with friends IDs
    """
    list = []
    for item in json_handle.keys():
        list.append(int(item))
    return sorted(list)

def text_analyzer(text: str):
    """
    Function to analyze text
    :param text: A text string.
    :return: Analyzing parameters:
    number of words, lenght, (not now)
    uniqueness factor
    """
    words = len(sorted(set(text.split())))
    lenght = len(text)
    uniqueness = lenght + words
    return uniqueness

def friend_rank(wall: list):
    """
    Calculates user rank, based on the wall posts
    :param wall: List of posts from wall, as an output of extract_wall_items()
    :return: Rank
    """
    # wall = extract_wall_items(user, json_handle)
    factor = 0.2  # A factor of decreasing values of reposts
    lenght = len(wall)
    counter = 0.0
    for item in wall:
        if item['is_copy']:
            counter += text_analyzer(item['text']) * factor
        else:
            counter += text_analyzer(item['text'])
    return counter / lenght

with open('vk2.json') as f:
    data = json.load(f)

friends = extract_friends(data)
ranks = {}
for person in friends:      # The main ranking loop
    extracted = extract_wall_items(str(person), data)
    if len(extracted) == 0:
        rank = 0
    else:
        rank = friend_rank(extracted)
    ranks[person] = rank

result = sorted(ranks.items(), key=lambda x: x[1])  # Do some sorting

if len(result) < 10:        # The number of items to show
    number = len(result)
else:
    number = 10

final_result = result[-number:-1]
final_result.reverse()
for item in final_result:       # Showing top N items
    print(item)

