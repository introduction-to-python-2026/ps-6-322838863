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


def Test_Shoval(file_path):
    # Step 1: Read the file
    file = open(file_path)
    rows = file.readlines()
    file.close()
    # Step 2: Build the dictionary
    codon_dict = {}
    for row in rows:
        # Remove newline and spaces
        row = row.strip()
        # Skip empty lines
        if not row:
            continue
        # Split into cells
        parts = row.split('\t')
        # Expecting at least 3 columns: codon, name, abbreviation, full name
        codon = parts[0]          # e.g., "AAA"
        amino_acid = parts[2]     # e.g., "K"
        # Add to dictionary
        codon_dict[codon] = amino_acid
    return codon_dict
