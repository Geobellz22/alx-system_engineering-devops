#!/usr/bin/python3
""" Script that extend python script"""

import csv
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open('{}.csv'.format(user.get("Id")), 'w', newline='') as readfile:
        data_writer = csv.writer(readfile, quoting=csv.QUOTE_ALL)
        [data_writer.writerow(
            [user.get("Id"),
             user.get("username"),
             item.get("completed"),
             item.get("title")]
            ) for item in todos]
