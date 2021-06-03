#!/usr/bin/python3
"""
script that adds all arguments to a Python list.
"""


from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_file = load_from_json_file("add_item.json")

except FileNotFoundError:
    json_file = []

for i in range(1, len(argv)):
    json_file.append(argv[i])
save_to_json_file(json_file, "add_item.json")
