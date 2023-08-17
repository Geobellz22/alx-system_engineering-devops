#!/usr/bin/python3
""" Script that extend python script"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open('{}.csv'.format(user.get("Id")), 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        completed_tasks = sum(1 for items in todos if item["completed"])
        data_writer.writerow([user_id, user.get("username"), completed_tasks])
