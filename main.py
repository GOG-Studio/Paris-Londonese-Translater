# -*- coding: utf-8 -*-
# coding: utf-8

from time import sleep
def translate_letter(text):
    #エンコードして"encoded"に代入する(バイト列)
    encoded = text.encode("ISO-2022-JP")
    #"encodedを出力する"
    #print(encoded)

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
    #条件ごとにリスト内の数列から減算する
    first_hex_a = [x - 32 if 0x21 <= x <= 0x28 else x - 39 if 0x30 <= x <= 0x90 else x for x in first_hex]
    second_hex_a = [x - 32 for x in second_hex]

    #減算後の値を出力する（3,4行目）
    print(second_hex_a)
    print(first_hex_a)

    tr = str.maketrans({"1":"ぱ","2":"り","3":"ろ","4":"ん","5":"ど","6":"パ","7":"リ","8":"ロ","9":"ン","0":"ド",})
    word = str(str(second_hex_a[0])+"ー"+str(first_hex_a[0])).translate(tr)
    return word

translated = ""
word = input("翻訳する文字（全角）を入力：")
for c in word:
    t = translate_letter(c)
    translated += t

print(translated)
while True:
    sleep(60)