DNA = "GAGTATCCCGATTAGCGCTCACAGGCACCTCTCACCGTAGCAACTTTCTTGTCTCGCTAAAGCCAATACCCCGCTCAGTATAGCGCGTCACATTTCCAGCGCTTTCACACGGTACGTATGTTGAGGGTAACCTTCAGCACCCTCTAACTTCGGATGACCGAATCCCTCGGCCTCTTCAACACTTAAAGAATGTCCCTATCAACTTAACTATTAGAGGTTCTCGCGATTACAAAATATTTTAAATATCTACTGACATAAACTTCTGTCCCGGTGACTCGCTTGTCTTGATAAGGTTACGCTATTTTCCTCCGGTTTTGGGTCGCAAAACAGTAAACTCGTTGGTGGAAGGCTTGTTTTCCACACGAAATCTTTCATCTGACTTTTCGCCCTCAGCTGGTAAGAAATCTATGTGTCAAGGCCGCTGCTCCTCATAAGGCGTATAACGGCAGGAGAGAACTCCACTGCCTGAAACCCCCTCTCTGGAAGGGACATTATATGCTACTCGGAGAGATAGTCCATACGTTAGAGTTAATCAATGGGATATACACATCAAATCTTGACGCTCATATTGATTACTTCAGGAATTGCTCTGAAGAATCTTAATGCCTGCCCGCATACCACTGATTGTTACTTCTGGCCAAGGTGATTTCACTTTTGCCCACCCGCACTGAATCAGTGGCGTCATAGTATATTTGACCTCCCTCGGTAGTCGGTGCCCTTATCTAAACCTATTCTTAAGCCGGCCCTCTTTGCGGACCAGGCACCAGTAGTTAGGTTCTTGGTCGTCTCTCGGATCCCTCCTTCGAGACGGGTTTGATGTGAAGCAGTACAGACAAGGATTTACAATCAGCGGTATTTTGTTCTGTCATCTAAG"

DNA_new = ""

DNA_list = list(DNA)

while len(DNA_list) != 0:
    DNA_new += DNA_list.pop()

DNA_complement = ""
DNA_new = list(DNA_new)

for char in DNA_new:
    if char == 'A':
        DNA_complement += 'T'
    elif char == 'T':
        DNA_complement += 'A'
    elif char == 'C':
        DNA_complement += 'G'
    else:
        DNA_complement += 'C'

print(DNA_complement)
