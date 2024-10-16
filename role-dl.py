#!/usr/bin/env python3
import sys
import json
import base64
import subprocess
import os
from urllib.parse import urlparse

ROLE_DIR = "/etc/ansible/roles/"

# struct must be defined as : https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
requirements = json.loads(str(sys.argv[1]))
username = sys.argv[2]
password = sys.argv[3]

# def build_credential(username, password):
#     credential = f"${username}:${password}"
#     credential_bytes = credential.encode('ascii')
#     base64_bytes = base64.b64encode(credential_bytes)
#     return base64_bytes.decode('ascii')
#
# credential = build_credential(username, password)

try:
    os.mkdir(ROLE_DIR)
except FileExistsError:
    pass
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")

for role in requirements:
    url_parsed = urlparse(role['src']) 
    reformed_url = url_parsed._replace(netloc=f"${username}:${password}@${netloc}")
    subprocess.call("git","clone",reformed_url, ROLE_DIR) 
    # if role['version']:

