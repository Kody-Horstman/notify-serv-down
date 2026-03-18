#!/bin/python3

import subprocess
import requests
import time
from datetime import datetime


def ping_serv(serv):
    """
    ping_serv : pings a provided server 1 time and returns the returncode of the command.

    serv : server IP address or DNS name.

    returns : subprocess return code from ping command
    """
    command = ["ping", "-c", "1", serv]

    result = subprocess.run(command, capture_output=True)
    
    return result.returncode


def ntfy(endpoint, message):
    """
    nfty : sends message to a ntfy.sh topic.
    
    endpoint : https address for ntfy.sh topic.
    message : Message to be sent to endpoint.

    returns : None
    """
    requests.post(endpoint, data=message.encode(encoding='utf-8'))


def main():
    """
    main : Loops infinitely until one server becomes unreachable, at which point, a notification is sent to ntfy.sh endpoint and the program exits. 

    returns : None
    """
    server = "192.168.1.2"
    ntfy_endpoint = "https://ntfy.sh/RK8K58mfzYO3LhjT" 
    sleep_for = 60

    ntfy(ntfy_endpoint, f"Info: notify-serv-down activated {datetime.now()}")

    while True:
        if (ping_serv(server) != 0):
            ntfy(ntfy_endpoint, f"Server: {server} is unreachable as of {datetime.now()}")
            break
        time.sleep(sleep_for)


if __name__ == "__main__":
    main()
