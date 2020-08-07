#!usr/bin/python
import sys
from readfa import Fasta
ag = sys.argv

fasta = Fasta(ag[1])

def getseq(genename, fragname, fnum, tnum):
    num1 = int(fnum) - 1
    num2 = int(tnum)
    seq=''.join(fasta.fragments[fragname][num1:num2])
    writefile = '>' + genename + '\n' + seq
    return(writefile)

f2 = open(ag[2], 'r')

with open(ag[3], 'w') as fobj:
    for line in f2:
        comp = line.split('\t')
        geneseq = getseq(comp[0], comp[1], comp[2], comp[3])
        print(comp[0])
        fobj.write(geneseq + '\n')
