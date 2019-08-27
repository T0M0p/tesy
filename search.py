# -*- coding: utf-8 -*-
import sys

search_word = sys.stdin.readline()#探す値の入力値の設定
conv_search_word = search_word.strip()

filenames=['file1.txt','file2.txt','file3.txt']#ページのまとまり
pagenum = len(filenames)#ページ数
answer = []#最終的な出力
for i in range(pagenum):
    page = open(filenames[i], "r")#ファイル読み込み
    lines = page.readlines()
    word = lines[0].split()#文字列を1つづつに変換
    wordnum = len(word)
    for x in range(wordnum):
        conv_word = word[x].strip()
        if conv_search_word == conv_word:
            answer.append(filenames[i])
            break

if answer == []:
    print("not exist.")
else:
    print(answer)
page.close()

