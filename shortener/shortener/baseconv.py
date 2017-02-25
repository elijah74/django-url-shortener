# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BaseConverter(object):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, num):
        """
        Encode a positive number in Base X

        Arguments:
        - `num`: The number to encode
        - `alphabet`: The alphabet to use for encoding
        """
        alphabet = self.BASE62
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def decode(self, text):
        """
        Decode a Base X encoded string into the number

        Arguments:
        - `string`: The encoded string
        - `alphabet`: The alphabet to use for encoding
        """
        alphabet = self.BASE62
        base = len(alphabet)
        strlen = len(text)
        num = 0

        idx = 0
        for charator in text:
            power = (strlen - (idx + 1))
            num += alphabet.index(charator) * (base ** power)
            idx += 1
        return num

Base62 = BaseConverter()
