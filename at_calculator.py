"""Functions for calculating metrics of DNA sequences"""

from __future__ import division 

def calculate_at(dna): 
    """Return the AT content of the argument. 
    Only works for uppercase DNA sequences
    """
    
    length = len(dna)
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content 

for _ in range(1000000):
    calculate_at('ATCGACTACGACTAGCATCGACTAGCATCGACTACGATCAGCTAGCCTA')