# -*- coding: utf-8 -*-
# @Author: Moming

def add_to_dict(word):
    dic = root
    for letter in word:
        if letter not in dic.keys():
            dic[letter] = [0, {}]

        dic[letter][0] = dic[letter][0] + 1
        dic = dic[letter][1]

def get_num(word):
    dic = root
    for letter in word[ : len(word) - 1]:
        if letter not in dic.keys():
            print '0'
            return

        dic = dic[letter][1]

    letter = word[len(word) - 1]
    if letter in dic.keys():
        print dic[letter][0]
        return

    print '0'

# main
root = {}
Ans = int(input())
for i in range(Ans):
    add_to_dict(raw_input())

Ans = int(input())
for i in range(Ans):
    get_num(raw_input())
