#!/usr/local/bin/python3

from Encoder import b64encoder
from Decoder import b64decoder

print(b64encoder('It is a test messagge'))
print(b64decoder(b64encoder('It is a test messagge')))
