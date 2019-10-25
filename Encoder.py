#!/usr/local/bin/python3
b64_char_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b64encoder(input_string):
    binary_list=''.join(format(ord(x),'08b') for x in input_string)
    splited_binary=['00'+binary_list[i:i+6] for i in range(0, len(binary_list), 6)]
    concated_encoded=''.join(format(b64_char_table[int(y,2)]) for y in splited_binary)+'=='
    return concated_encoded
