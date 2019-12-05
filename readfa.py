# !usr/bin/python
# a script read fasta file and it can extract the sequence with index and range
# with liudan's script, now it's much more sufficient
# version 4.0
# Linhe Sun

# usage:
# py readfa3.py -d 87_1cdsallseq.fasta -i Traes_5AL_D8DC40ABF.2 -o gene.txt -f 2 -t 1000 -h -l

import sys, getopt
helptxt = "ReadFa --version 2\nA script read fasta file and it can extract the sequence with index and range\nby Linhe Sun\nUsage: readfa2.py -d <database> -i <index> -f <startnum> -t <endnum> -o <outputfile> -l <indexlistoutput>\n-d & --data\tData file in fasta format.\n-i & --index\tThe index of the sequence you want to extract. If you do not know, you can get the index list with -l & --list.\n-f and -t\tThe range of the sequence you want to extract. -f must be less than -t. If you ignore this two parameter you will get the full length.\n-o & --out\tThe output file name. If you ignaore this parameter. The seq you want will be printed on the screen.\n-l & --list\tIf you want a list of the index of your fasta file, please add this parameter with a filename followed.\n-h & --help\tRead the help file."

class Fasta():
    def __init__(self, filename):
        self.filename = filename
        self.writefile = ''
        self.readfile()
        self.keyprint()

    # read the file and creat a self.fragmentst save index and sequence as key and value:
    def readfile(self):
        tmp_seq = []
        self.fragments = {}
        with open(self.filename) as file_object:
            seq_id = next(file_object).strip().split()[0][1:]

            for line in file_object:
            	if line[0] != '>':
            		tmp_seq.append(line.strip())
            	else:
            		self.fragments[seq_id] = [x for y in tmp_seq for x in y]
            		seq_id = line.strip().split()[0][1:]
            		tmp_seq = []
            self.fragments[seq_id] = [x for y in tmp_seq for x in y]
        
    # to print and save the keys:
    def keyprint(self): 
        self.keylist = ''
        for key in self.fragments.keys():
            self.keylist += key + '\n'

    # to get the whole seq of an id:
    def getall(self, fragname):
        seq=''.join(self.fragments[fragname])
        self.writefile = '>' + fragname + '\n' + seq

    # to get part of the seq of an id:
    def getpart(self, fragname, fnum, tnum):
        num1 = int(fnum) - 1
        num2 = int(tnum)
        seq=''.join(self.fragments[fragname][num1:num2])
        self.writefile = '>' + fragname + ' ' + fnum + ' ' + tnum + '\n' + seq
        

# main body of the scripts
def main(argv):
    filename = ''
    fragname = ''
    outname = ''
    fnum = ''
    tnum = ''
    keyoutname = ''

    try:
        opts, args = getopt.getopt(argv,"hl:d:i:o:f:t:",["help","list=","data=","index=","out="])
    except getopt.GetoptError:
        print(helptxt)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(helptxt)
            sys.exit()
        elif opt in ('-d', '--data'):
            filename = arg
        elif opt in ('-i', '--index'):
            fragname = arg
        elif opt in ('-o', '--out'):
            outname = arg
        elif opt == '-f':
            fnum = arg
        elif opt == '-t':
            tnum = arg
        elif opt in ('-l', '--list'):
            keyoutname = arg

    fasta = Fasta(filename)

    if fragname:
        if fnum and tnum:
            fasta.getpart(fragname, fnum, tnum)
        elif fnum or tnum:
            print('Both from num and to num are required.' )
        else:
            fasta.getall(fragname)
    
    if outname:
        with open(outname, 'w') as file_object:
            file_object.write(fasta.writefile)
    else:
        print(fasta.writefile)
    
    if keyoutname:
        with open(keyoutname, 'w') as file_object:
            file_object.write(fasta.keylist)
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(helptxt)
    else:
        main(sys.argv[1:])
else:
    print("The function is from model readfa4.py.")
