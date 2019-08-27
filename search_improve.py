# -*- coding: utf-8 -*-
import sys

#探す単語を扱いやすように設定
search_word = sys.stdin.readline()
new_search_word = search_word.split()#.split()でスペースなどの無駄を省く
search_word_length = len(new_search_word)

#ページのまとまり
filenames=['file1.txt','file2.txt','file3.txt']

#ページ数を格納
pagenum = len(filenames)

#最終的な出力
answer = []

#全てのページを読み込む
for i in range(pagenum):
    
    #削除分の埋め合わせカウント
    Delete_count = 0
    
    #ファイル読み込み
    page = open(filenames[i], "r")
    lines = page.readlines()
    
    #文字列を1つづつに変換してword[]に格納する
    word = lines[0].split()
    
    #読み込んだページの単語数をwordnumに格納
    wordnum = len(word)
    
    #1ページ分の単語数だけfor文を回す
    for x in range(wordnum):
        
        #削除した分だけ全体の単語数が減るため、その埋め合わせ
        x = x - Delete_count
        
        #6行目と同じように綺麗な形にする
        conv_word = word[x].strip()
        print(conv_word)
        
        #入力単語数分for文を回して確かめる
        for y in range(search_word_length):
            
            #存在するかを比較して確かめる
            if new_search_word[y] == conv_word:
                
                #存在した場合に、ページ情報を追加する
                answer.append(filenames[i])
                print(answer)
                
                #被りがないように同じものをword[]から削除しておく
                while conv_word in word: word.remove(conv_word)
                
                #削除後のword[]の要素数を格納する
                wordnum = len(word)

                #削除された分の埋め合わせ
                Delete_count = 1
                print(word)
                print(wordnum,x,y)


if answer == []:
    print("not exist.")#なかった場合
else:
    print(answer)#あった場合
page.close()

