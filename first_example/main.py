"""
This is the main code for learning bioinformatics.
"""

import random
from dna_toolkit import *


# DNA_SEQUENCE = "".join([random.choice(NUCLEOTIDES) for _ in range(20)])
DNA_SEQUENCE = "GATGGAACTTGACTACGTAAATT"
# print(count_freq(DNA_SEQUENCE))
# print(dna_to_rna(DNA_SEQUENCE))
a, b = 946, 903
h2 = a**2 + b**2
print(h2)

def str_test(s: str, a, b, c, d):
    return f"{s[a:b+1]} {s[c:d+1]}"

def conds_test(a, b):
    total = 0
    for i in range(a, b):
        if i%2 == 1:
            total += i
    return total

def txt_test(txt_file):
    with open(txt_file, "r") as f:
        lines = f.readlines()
        f.close()
    with open(txt_file, "w") as f:
        for idx, line in enumerate(lines):
            if idx%2 == 1:
                f.write(line)
        f.close()
    

# print(str_test("bKuOMwYxUNbTdwbf0mqTfb8LBkVVzqHFP9IFX5kCyvfX2ONFNkfsxBRhacophorus7PJM19mUgYHbn1oZKH91tardaBm3VULpsPEwCAfRqgJQkbxmFnPU9Hmj7dExziVHE0DRCDjoo1RFlJEsQ82eimxLpyEiiOBmp.", 54, 64, 85, 89))
# print(conds_test(4713, 9270))
# txt_test("test.txt")


import collections
sentence = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
dict_freq = dict(collections.Counter(sentence.split(" ")))
for key, value in dict_freq.items():
    print(key, value)
