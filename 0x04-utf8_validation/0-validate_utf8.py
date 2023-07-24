#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Function to check if the most significant bit (MSB) is set"""
    def is_most_significant_bit_set(byte):
        return byte & 0b10000000 == 0b10000000

    """Function to check if the next byte follows UTF-8 rules"""
    def follows_utf8_rules(start, num_bytes):
        """Check if the next num_bytes-1 bytes start with '10'"""
        for i in range(start + 1, start + num_bytes):
            if i >= len(data) or not is_most_significant_bit_set(data[i]) \
                    or data[i] & 0b11000000 != 0b10000000:
                return False
        return True

    """Iterate through the data list"""
    i = 0
    while i < len(data):
        """Check the number of bytes for the current character"""
        if data[i] & 0b10000000 == 0:
            """1-byte character"""
            num_bytes = 1
        elif data[i] & 0b11100000 == 0b11000000:
            """2-byte character"""
            num_bytes = 2
        elif data[i] & 0b11110000 == 0b11100000:
            """3-byte character"""
            num_bytes = 3
        elif data[i] & 0b11111000 == 0b11110000:
            """4-byte character"""
            num_bytes = 4
        else:
            return False

        """Check if the next bytes follow UTF-8 rules"""
        if not follows_utf8_rules(i, num_bytes):
            return False

        """Move to the next character"""
        i += num_bytes

    return True
