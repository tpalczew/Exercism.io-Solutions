def to_rna(dna_strand):
    # G -> C
    # C -> G
    # T -> A
    # A -> U
    rna_strand = []
    for element in list(dna_strand):
        if element is 'G':
            rna_strand.append('C')
        if element is 'C':
            rna_strand.append('G')
        if element is 'T':
            rna_strand.append('A')
        if element is 'A':
            rna_strand.append('U')
    return ''.join(map(str, rna_strand))     
