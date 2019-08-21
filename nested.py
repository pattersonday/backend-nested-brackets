#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This checks if each line is properly nested.
"""
__author__ = "Patterson Day"

import sys

def read_file():
    with open('input.txt', 'r') as file:
        data = file.read()
    split_data = data.split('\n')
    return split_data

def main(data):
    openers = ["(", "[", "{", "<", "(*"]
    closers = [")", "]", "}", ">", "*)"]
    stack = []
    index_count = 0

    while data:
        token = data[0]
        if data.startswith("(*"):
            token = "(*"
        if data.startswith("*)"):
            token = "*)"
        if token in openers:
            stack.append(token)
        if token in closers:
            corresponding_bracket = openers[closers.index(token)]
            if stack[-1] == corresponding_bracket:
                stack.pop()
            else:
                return "No " + str(index_count + 1)
        index_count += 1
        data = data[len(token):]
    if not stack:
        return "Yes"
    else:
        # index_count += 1
        return "No " + str(index_count + 1)
        
def write_file(text):
    filename = "output.txt"
    with open(filename, 'a') as output_file:
        output_file.write(text)


if __name__ == '__main__':
    string_list = read_file()
    for string in string_list:
        result = main(string) + '\n'
        write_file(result) 

