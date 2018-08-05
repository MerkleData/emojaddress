import os
import re
import binascii
from .dictionaries.unicode_codes import EMOJI_UNICODE

class Address(object):

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dictionaries', 'english.txt') 
    WORDS_ENGLISH = [w.strip() for w in open(path, "r").readlines()]
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dictionaries', 'chinese.txt') 
    WORDS_CHINESE = [w.strip() for w in open(path, "r").readlines()]

    LIMIT = 24
    DICTIONARY_SIZE = 2048

    SUPPORTED_COINS = ['btc', 'eth']

    def __init__(self):
        self.MNEMONIC_EMOJI = list(EMOJI_UNICODE.values())[0:self.DICTIONARY_SIZE]
        self.MNEMONIC_ENGLISH = self.WORDS_ENGLISH[0:self.DICTIONARY_SIZE]
        self.MNEMONIC_CHINESE = self.WORDS_CHINESE[0:self.DICTIONARY_SIZE]

    def mnemonic(self, val, coin=None, emoji=True, language=None):
        if coin is not None and coin.lower() not in self.SUPPORTED_COINS:
            coin = coin.lower()
            raise NotImplementedError("Only supports {}".format(self.SUPPORTED_COINS))

        if coin == 'eth' or val.startswith("0x"):
            self._nr = int(val.lower(), 16)
        else:
            self._nr = self._b58decode(val)

        words = []
        if emoji:
            mnemonics = self.MNEMONIC_EMOJI
            join_sep = ''
        else:
            if language in ['chinese', 'Chinese']:
                mnemonics = self.MNEMONIC_CHINESE
                join_sep = ''
            else:
                mnemonics = self.MNEMONIC_ENGLISH
                join_sep = ' '
        size = len(mnemonics)
        i = self._nr
        words = []
        while i > 0 and len(words) < self.LIMIT:
            rem, i = i % size, i // size
            words.append(mnemonics[rem])
        return join_sep.join(words)


    B58_CODE_STR = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    def _b58decode(self, b58_str):
        acc, base = 0, 58
        nr_1_s = len(re.match("^1*", b58_str).group(0))
        for ch in b58_str:
            acc *= base
            idx = self.B58_CODE_STR.find(ch)
            if idx < 0:
                raise ValueError("Invalid char from base58check string {}".format(ch))
            acc += idx
        # skip checksum validation
        r_bytes = b'\x00' * nr_1_s + self._encode_base256(acc)
        return int.from_bytes(r_bytes[1:-4], byteorder="big")


    B256_CODE_STR = "".join([chr(x) for x in range(256)])

    def _encode_base256(self, nr):
        acc, base = bytes(), 256
        while nr > 0:
            b, nr = self.B256_CODE_STR[nr % base], nr // base
            acc = bytes([ord(b)]) + acc
        return acc


