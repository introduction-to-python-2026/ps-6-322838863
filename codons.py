def create_codon_dict(file_path):
    #file_path = "data/codons.txt" 
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    codon_dict = {} 
    for l in lines:
        l = l.strip()
        cells = l.split("\t")
        if len(cells) < 4:
          continue

        key = cells[0]
        value = cells[2]
        codon_dict[key] = value
    return codon_dict

