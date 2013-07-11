#!/usr/bin/env python3

import collections
import string
import sys

def get_rate(i):
    return i[1]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
for word in reversed(sorted(words.items(),key=get_rate)):
    print("'{0}' occurs {1} times".format(word[0], word[1]))
