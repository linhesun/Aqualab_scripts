import sys, getopt
ag = sys.argv
#print(ag)
names = locals()
for i in range(1, len(ag)):
    names['n' + str(i) ] = []
    with open(ag[i], 'r') as f:
        for line in f:
            names['n' + str(i) ].append(line)

overl = set(names['n1'])
#print(overl)
for i in range(2, len(ag)):
    overl = overl & set(names['n' + str(i)])

overl = list(overl)
print(overl)
with open('result.txt', 'w') as f:
    for line in overl:
        f.write(line)

exit()
#print(names)
#print(names['n1'])