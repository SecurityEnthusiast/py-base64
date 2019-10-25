#!/usr/local/bin/python3
b64_char_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b64decoder(input_string):

    binary_list=[(format(b64_char_table.find(i),'06b')) for i in input_string.replace('=','')]
    concated_binary=''.join(x for x in binary_list)
    concated_decoded=''.join(chr(int(j,2)) for j in ([concated_binary[i:i+8] for i in range(0, len(concated_binary), 8)]))
    return concated_decoded
