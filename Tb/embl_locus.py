import sys

file = sys.argv[1]

include_locus = False

if len(sys.argv) > 2 and sys.argv[2] == 'locus':
    include_locus = True

count = 1
with open(file, 'r') as file:
    for line in file:
        if line[0:9] == 'FT   gene':
            # extract location
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
            
            for line in file:
                line = line.strip()
                if line.find('CDS') > 0:
                    raise Exception('Incorrect Parsing')
                    break
                if line.find('locus_tag') < 0: continue
                i, j = line.find('"'), line.rfind('"')
                locus_tag = line[i+1:j]
                break
            if include_locus:
                print('{:05}'.format(count) + ' ' + '{: >7}'.format(s) + ' ' + '{: >7}'.format(e) + ' ' + locus_tag)
            else:
                print('{:05}'.format(count) + ' ' + '{: >7}'.format(s) + ' ' + '{: >7}'.format(e))
            count += 1
