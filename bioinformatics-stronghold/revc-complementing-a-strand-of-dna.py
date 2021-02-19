import re

s="ATTTCCGACACGCCGTACAAGCGTGGGTCAGAATATGATCGACCGGCTCTAGGGGTTCCATACTGGTATCTAGCGTATAATATATGTTGCGGTGGATGTGTGGGGGGTCGAAAAAGGCCTCTCTCGTAATTTGCAACACCACAAGGGTCTAGTCAACATTCCTGGCCGATACCGCCCTGGTCGACTCCCCGTCTAAGCGTGGCAAGCCCAAATCATAGGTAGCTAGCATCGGTATGTGTTACATTTTCATTAGCGTTGGTGCTCAGAACAGACCTGATGTTTCAGAGCCACTTTGGTATCCGCGGTCTCAGACTGGACTCCTCTTCGTACTTTGGATCACGTCTCCACTATGTCCTATGCTGCGGGAAACGGACAAACGATTAGATGCCGAGAGCTTACCGACAAGACGCGCCGACCGTAGCAGCTAAACACCCATGCATCAAAGAACGTTGTCCTCCTGCCTCGTCGAGGTTCCTAAACGCCCTACAGATGGACAACTAATACGTTCTTTGTGAAAATTCGCTCGCTCCTGGCGCCCCGGCCATCGTACCGAGCCGTTGTGTCACGAGCTGTGAGCGCCTCGACTTACTGCCCGCGGAGACCTGGTGGAGACGCGAAGGGGATGACTGGGGGCTCGGAAGCCCTATTGCTGGATCGGCGTGTTAGTCCCAAGTGGCACAATGATGTGGGGAACTACCCAAATGAATGCATCGACGCGATTCGGTTCATAAAGGATGAGATCTTCGGTCGCCAACCTTTAAGCGACAGTATCAGCGAACTTCCGTCACGCCTATTACACCCTAGGGCAGCTGGTGTTCATGTACGTCCAGATGCGGTACATCAGACGGTTTACTTTTTCTGAACGAATACTCACCAATGGCTGGGCTTTAGAGCGGAGTCGTAATAGGCCAACATGGAGGACCAACGGAGAGACCAGCAACATCAAGCGAAGCGTGGCTGCAGCGGCATTGTAAGCAGGACCGGGGGA"
res=[]
for i in s:
    if i=="A":
        res.append("T")
    elif i=="T":
        res.append("A")
    elif i=="C":
        res.append("G")
    elif i=="G":
        res.append("C")
    else:
        raise KeyError("WTF!?")
res=res[::-1]
print("".join(res))