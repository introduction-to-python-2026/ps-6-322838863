def create_codon_dict(file_path):
    file_path = "data/codons.txt" 
    f = open(file_path, "r")
    lines = f.readlines()
    f.close
    dict = {} 
    for l in lines:
        dict += l.strip()
        lines.split()
        cells = l.find_all("td")
        key = cells[0].text
        value = cells[3].text
        dict[key] = value
    return dict
