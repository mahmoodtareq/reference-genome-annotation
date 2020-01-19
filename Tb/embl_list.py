import sys

file = sys.argv[1]

count = 1
with open(file, 'r') as file:
    for line in file:
        if line[0:9] == 'FT   gene':
            complement = False
            coord = line[9:].strip()
            if len(coord) == 0: continue
            if 'join' in coord: continue
            if 'complement' in coord:
                coord = coord[11:-1]
                complement = True
            if len(coord) == 0: continue
            s, e = coord.split('..')
            s = s.strip('<>')
            e = e.strip('<>')
            if complement: s, e = e, s
            print('{:05}'.format(count) + ' ' + '{: >7}'.format(s) + ' ' + '{: >7}'.format(e))
            count += 1
