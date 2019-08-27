# -*- coding: utf-8 -*-
import sys

search_word = sys.stdin.readline()#探す値の入力値の設定
conv_search_word = search_word.strip()#値を使いやすいように変換する

filenames=['file1.txt','file2.txt','file3.txt']#ページのまとまり
pagenum = len(filenames)#ページ数
answer = []#最終的な出力
for i in range(pagenum):
    page = open(filenames[i], "r")#ファイル読み込み
    lines = page.readlines()
    word = lines[0].split()#文字列を1つづつに変換
    wordnum = len(word)
    for x in range(wordnum):
        conv_word = word[x].strip()#5行目と同じように綺麗な形にする
        if conv_search_word == conv_word:#存在するかを比較して確かめる
            answer.append(filenames[i])#あった場合に、ページ情報を追加する
            break

if answer == []:
    print("not exist.")#なかった場合
else:
    print(answer)#あった場合
page.close()

