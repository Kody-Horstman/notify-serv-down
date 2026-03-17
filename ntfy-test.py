#!/bin/python3

import requests
import time

endpoint = "https://ntfy.sh/RK8K58mfzYO3LhjT"
message = "This is a test from ntfy-test.py running with 'nohup /home/kody/Dev/ntfy-test.py'."

time.sleep(60)

requests.post(endpoint, message.encode(encoding='utf-8'))
