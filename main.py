# -*- coding: utf-8 -*-
# coding: utf-8
from sys import argv
from time import sleep
def translate_letter(text :str, debug :bool):
    #エンコードして"encoded"に代入する(バイト列)
    encoded = text.encode("ISO-2022-JP")
    ##"encoded"を出力する
    if debug == True:
        print("encoded: "+str(encoded))

    #バイト列を整数にしてリスト"hex_representation"に代入
    hex_representation = [f'{byte:02X}' for byte in encoded]
    #リスト"hex_representation"の前後三つを削除して代入
    del hex_representation[:3]
    del hex_representation[-3:]
    #リスト"hex_representation"から偶数・奇数 番目を取り出してそれぞれリスト"first_hex""second_hexに代入する"
    first_hex = hex_representation[1::2]
    second_hex = hex_representation[::2]

    #それぞれのリストの文字列を数列に変換する
    first_hex = [int(x,16) for x in first_hex]
    second_hex = [int(x,16) for x in second_hex]

    ##減算後の値を出力する（3,4行目）
    if debug == True:
        print("first: "+str(second_hex))
        print("second: "+str(first_hex))
    
    #条件ごとにリスト内の数列から減算する
    first_hex_a = [x - 32 for x in first_hex]
    second_hex_a = [x - 32 for x in second_hex]
    #数値の出力
    print(second_hex_a)
    print(first_hex_a)
    #数値を変換
    tr = str.maketrans({"1":"ぱ","2":"り","3":"ろ","4":"ん","5":"ど","6":"パ","7":"リ","8":"ロ","9":"ン","0":"ド",})
    word = str(str(second_hex_a[0])+"ー"+str(first_hex_a[0])).translate(tr)
    word = word + " "
    #返す
    return word

translated = ""
try:
    word = argv[1]
except:
    word = input("翻訳する文字（全角）を入力：")
for c in word:
    t = translate_letter(c, False)
    translated += t

print(translated)

input("Enter to Exit.")