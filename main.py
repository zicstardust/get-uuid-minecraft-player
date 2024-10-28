import sys
import uuid
import requests
import os
import shutil

def get_online_uuid(player: str) -> str:
    """Return the *online* UUID of a player name"""
    online_uuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{player}').json()['id']
    online_uuid = online_uuid[:8] + '-' + online_uuid[8:]
    online_uuid = online_uuid[:13] + '-' + online_uuid[13:]
    online_uuid = online_uuid[:18] + '-' + online_uuid[18:]
    online_uuid = online_uuid[:23] + '-' + online_uuid[23:]
    return online_uuid


class NULL_NAMESPACE:
    """This garbage is needed to replicate the behavior of the UUID.nameUUIDfromBytes function present in Java."""
    bytes = b''
def get_offline_uuid(player: str):
    """Return the *offline* UUID of a player name"""
    return uuid.uuid3(NULL_NAMESPACE, f'OfflinePlayer:{player}')

def main(username):
    print (f'username: {username}')
    print (f'Online UUID: {get_online_uuid(username)}')
    print (f'Offline UUID: {get_offline_uuid(username)}')


if __name__ == '__main__':
    main(sys.argv[1])
    