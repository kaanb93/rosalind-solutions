import collections

s="CTGATGTGTTGGGGGGGGGACGCTGGATAGTTTCTTTTCGGTACGAACGCGTGTCTTACTATGGCTACCTGAGCATGCGCGGGGGGTCGACATGCGTATATTGAGTTAGACGGGCATGCACGGCTACTCCGCTGTTCGATAGTAATTTGAGTCGTCGCCCGGCAATAGCGGATAACTCTCGAGAAACCGCTGCTCGCGGGGGCCGTCACCTCACATGGGCTGGTAGCAGGCACTTCGACACTAACTTGGCCGATTAACCTTAAAGTAACTATCTACATTGGACTTTTGTCCGCTTAATGAAGCTTGATGCGTCTAAAAGGGAGTAAACTATCGTTGTTCACTTCCAAGTTGGGGGATTGGTGGGTGAGGGCAGAACACTGATTTGAGACGGCTGCCAAGGCCTATGTTCTTCTCAAGTGAGGTAGCATAGGTGAGGCCCATAACTTTTGTGGCTATGGTGGGGCATATTCAATCGGAACCACTCACGGAGACAGGTATCCTAGCCTTCTCCTATAGAGAACCGATAAAGGCACTGAAAGGGCAGATCCGGCTTACAAGGATTGACGCAATGTCTGAGCGGTGTTGGCCAAAGATAAAGTTCGGTTGCAGCCTTTTTTTAGCGCTTTGAGGCAGATGAAAAGTTAAACGAGCTCCTGTAAGAGGTTAAGGTTTGAACCCTATAAGCTTGCGATTCTTTTCACCTCGGGCGTAAATCCAGCCAACGGTTTTGCCGCTACTAAAACAATCCGAATGCTTCCACACCTCCCGCTGTATAATTGCCGCCTACAATAACTGTAGTGCAACTAGGGGACTTAAATAAGTTGTAAAGTCCAATACCTTGAAGTTGTAACCTCACGCCCGACCACATACATAACGTCGT"

sdict=dict(collections.Counter(s))
print(str(sdict["A"])+" "+str(sdict["C"])+" "+str(sdict["G"])+" "+str(sdict["T"]))