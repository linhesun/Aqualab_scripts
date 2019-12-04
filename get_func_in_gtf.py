#!usr/bin/python
import sys
ag = sys.argv

if len(ag) == 1:
    print('Usage: python get_func_in_gtf.py <gtf_file_name> <output_file_name>')
    sys.exit(2)
    
def get_dict(fname):
# open the gtf file
    gtff = open(fname, 'r')
    genedicts = []
    for line in gtff:
        tsplit = line.split('\t')
        try:
            if tsplit[2] == 'gene':
                name = tsplit[-1].split(';')[0].split('"')[1]
                scaffold = tsplit[0]
                start = tsplit[3]
                end = tsplit[4]
                genedic = {'name': name, 'scaffold': scaffold, 'start': start, 'end': end, 'product': False}
            else:
                if genedic['product']:
                    pass
                else:
                    comps = tsplit[-1].split(';')
                    for comp in comps:
                        if 'product' in comp:
                            genedic['product'] = comp.split('"')[1]
                            genedicts.append(genedic)
        except IndexError:
            pass
    return(genedicts)

genedicts = get_dict(ag[1])

with open(ag[2], 'w') as fobj:
    for genedict in genedicts:
        fobj.write(genedict['name'] + '\t' + genedict['scaffold']+ '\t' + genedict['start']+ '\t' + genedict['end']+ '\t' + str(genedict['product'])+ '\n')
