#翻訳するテキストを聞く
text = input("Enter:")
#エンコードして"encoded"に代入する(バイト列)
encoded = text.encode("ISO-2022-JP")
#"encodedを出力する"
print(encoded)

#バイト列を整数にしてリスト"hex_representation"に代入
hex_representation = [f'{byte:02X}' for byte in encoded]
#リスト"hex_representation"の前後三つを削除して代入
del hex_representation[:3]
del hex_representation[-3:]

first_hex = hex_representation[1::2]
second_hex = hex_representation[::2]
first_hex = [int(x) for x in first_hex]
second_hex = [int(x) for x in second_hex]
first_hex_a = [x - 32 if 21 <= x <= 28 else x - 39 if 30 <= x <= 74 else x for x in first_hex]
second_hex_a = [x - 32 for x in second_hex]

print(first_hex)
print(second_hex)
print(first_hex_a)
print(second_hex_a)
