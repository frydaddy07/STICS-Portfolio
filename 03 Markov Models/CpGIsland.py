A = {'AA':2, 'AT':3, 'AG':2, 'AC':5}
T = {'TT':2, 'TA':1, 'TG':7, 'TC':2}
G = {'GG':1, 'GA':3, 'GT':3, 'GC':5}
C = {'CC':4, 'CA':2, 'CT':2, 'CG':4}

test_sequence = list('ATCGCGATTACGCGTA')

master_dictionary = {'A':A, 'T':T, 'G':G, 'C':C}

def training1(seq):
    acc = 1
    while len(seq) > 1:
        x = master_dictionary[seq[0]]
        pair = seq[0] + seq[1]
        acc = acc * x[pair]
        seq = seq[1:]
    return acc

# normalize counts

#####
counts = {}
probs = {}
seth = list('ABCDCABCABBABCABBCABCDABCABDCBADBCABDBCABDBCADCABCBADBCABDCBADBCADBCADBACBDABCABCBDABCBDABCABDCA')

def training2(seth):
    for i in range(1, len(seth)):
        step = str(seth[i - 1]) + str(seth[i])
        if step not in counts:
            counts[step] = 1
        else:
            counts[step] += 1
    for key in counts:
        probs[key] = float(counts[key]) / len(seth)

training2(seth)

print(probs)
print(len(probs))


"""
hs_ref_GRCh38.p7_chr19.mfa.gz
from
ftp://ftp.ncbi.nih.gov/genomes/Homo_sapiens/Assembled_chromosomes/seq/
"""
