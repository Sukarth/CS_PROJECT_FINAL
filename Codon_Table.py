# Creating a dictionary, so that it is easy to access different amino acids.
# E.g. "Phe" and "Leu" from RNA sequences like "UUU" and "UUA.
# This simply maps different keys and values together, for easy access.

RNA_CODON_TABLE = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu",
    "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile",
    "AUA": "Ile", "AUG": "Met",  # Start codon
    "GUU": "Val", "GUC": "Val",
    "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser",
    "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro",
    "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr",
    "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala",
    "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "UAA": "STOP", "UAG": "STOP",  # Stop codons (these will be overwritten later in the code)
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys",
    "UGA": "STOP", "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg",
    "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser",
    "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly",
    "GGA": "Gly", "GGG": "Gly"
}
