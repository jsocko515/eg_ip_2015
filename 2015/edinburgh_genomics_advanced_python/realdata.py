from __future__ import division
import random

def at_content(dna):
    return (dna.count('A') + dna.count('T')) / len(dna)

def same_start(dna1, dna2):
    return dna1[0:5] == dna2[0:5]

def random_dna(length):
    return "".join([random.choice(['A','T','G','C']) for _ in range(length)])

dnas = [random_dna(1000) for _ in range(1000)]
cutoff = 0.525

@profile
def find_interesting(dnas):
    interesting = set()
    for one in dnas:
        at = at_content(one)
        if at > cutoff:
            for two in dnas:
                if one != two and same_start(one, two):
                    interesting.add(one)

    return(interesting)

find_interesting(dnas)
