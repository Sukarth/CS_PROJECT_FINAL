#!/usr/bin/env python3
"""
RNA Codon Table Module

This module contains the standard genetic code mapping RNA codons to amino acids.
The genetic code is universal across most organisms and is used for protein synthesis.

Author: Sukarth Acharya (Originally by Utsav Choudhury)
Date: 2025
Project: LCOM.e
"""

from typing import Dict, List, Set

# Standard RNA Codon Table - Maps RNA triplets to amino acids
# Based on the universal genetic code used in most organisms
RNA_CODON_TABLE: Dict[str, str] = {
    # Phenylalanine (Phe, F)
    "UUU": "Phe", "UUC": "Phe",
    
    # Leucine (Leu, L)
    "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu",
    "CUA": "Leu", "CUG": "Leu",
    
    # Isoleucine (Ile, I)
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    
    # Methionine (Met, M) - Start codon
    "AUG": "Met",
    
    # Valine (Val, V)
    "GUU": "Val", "GUC": "Val",
    "GUA": "Val", "GUG": "Val",
    
    # Serine (Ser, S)
    "UCU": "Ser", "UCC": "Ser",
    "UCA": "Ser", "UCG": "Ser",
    "AGU": "Ser", "AGC": "Ser",
    
    # Proline (Pro, P)
    "CCU": "Pro", "CCC": "Pro",
    "CCA": "Pro", "CCG": "Pro",
    
    # Threonine (Thr, T)
    "ACU": "Thr", "ACC": "Thr",
    "ACA": "Thr", "ACG": "Thr",
    
    # Alanine (Ala, A)
    "GCU": "Ala", "GCC": "Ala",
    "GCA": "Ala", "GCG": "Ala",
    
    # Tyrosine (Tyr, Y)
    "UAU": "Tyr", "UAC": "Tyr",
    
    # Histidine (His, H)
    "CAU": "His", "CAC": "His",
    
    # Glutamine (Gln, Q)
    "CAA": "Gln", "CAG": "Gln",
    
    # Asparagine (Asn, N)
    "AAU": "Asn", "AAC": "Asn",
    
    # Lysine (Lys, K)
    "AAA": "Lys", "AAG": "Lys",
    
    # Aspartic acid (Asp, D)
    "GAU": "Asp", "GAC": "Asp",
    
    # Glutamic acid (Glu, E)
    "GAA": "Glu", "GAG": "Glu",
    
    # Cysteine (Cys, C)
    "UGU": "Cys", "UGC": "Cys",
    
    # Tryptophan (Trp, W)
    "UGG": "Trp",
    
    # Arginine (Arg, R)
    "CGU": "Arg", "CGC": "Arg",
    "CGA": "Arg", "CGG": "Arg",
    "AGA": "Arg", "AGG": "Arg",
    
    # Glycine (Gly, G)
    "GGU": "Gly", "GGC": "Gly",
    "GGA": "Gly", "GGG": "Gly",
    
    # Stop codons (translation termination signals)
    "UAA": "STOP",  # Amber stop codon
    "UAG": "STOP",  # Ochre stop codon
    "UGA": "STOP",  # Opal stop codon
}

# Additional useful constants for bioinformatics applications
START_CODONS: Set[str] = {"AUG"}
STOP_CODONS: Set[str] = {"UAA", "UAG", "UGA"}

# Amino acid properties for advanced analysis
AMINO_ACID_PROPERTIES: Dict[str, Dict[str, str]] = {
    "Phe": {"name": "Phenylalanine", "type": "Aromatic", "charge": "Neutral"},
    "Leu": {"name": "Leucine", "type": "Aliphatic", "charge": "Neutral"},
    "Ile": {"name": "Isoleucine", "type": "Aliphatic", "charge": "Neutral"},
    "Met": {"name": "Methionine", "type": "Sulfur-containing", "charge": "Neutral"},
    "Val": {"name": "Valine", "type": "Aliphatic", "charge": "Neutral"},
    "Ser": {"name": "Serine", "type": "Polar", "charge": "Neutral"},
    "Pro": {"name": "Proline", "type": "Cyclic", "charge": "Neutral"},
    "Thr": {"name": "Threonine", "type": "Polar", "charge": "Neutral"},
    "Ala": {"name": "Alanine", "type": "Aliphatic", "charge": "Neutral"},
    "Tyr": {"name": "Tyrosine", "type": "Aromatic", "charge": "Neutral"},
    "His": {"name": "Histidine", "type": "Basic", "charge": "Positive"},
    "Gln": {"name": "Glutamine", "type": "Polar", "charge": "Neutral"},
    "Asn": {"name": "Asparagine", "type": "Polar", "charge": "Neutral"},
    "Lys": {"name": "Lysine", "type": "Basic", "charge": "Positive"},
    "Asp": {"name": "Aspartic acid", "type": "Acidic", "charge": "Negative"},
    "Glu": {"name": "Glutamic acid", "type": "Acidic", "charge": "Negative"},
    "Cys": {"name": "Cysteine", "type": "Sulfur-containing", "charge": "Neutral"},
    "Trp": {"name": "Tryptophan", "type": "Aromatic", "charge": "Neutral"},
    "Arg": {"name": "Arginine", "type": "Basic", "charge": "Positive"},
    "Gly": {"name": "Glycine", "type": "Aliphatic", "charge": "Neutral"},
}


def get_amino_acid_full_name(short_name: str) -> str:
    """
    Get the full name of an amino acid from its 3-letter abbreviation.
    
    Args:
        short_name (str): 3-letter amino acid abbreviation
        
    Returns:
        str: Full amino acid name
    """
    return AMINO_ACID_PROPERTIES.get(short_name, {}).get("name", "Unknown")


def get_amino_acid_type(short_name: str) -> str:
    """
    Get the chemical type of an amino acid.
    
    Args:
        short_name (str): 3-letter amino acid abbreviation
        
    Returns:
        str: Chemical type of the amino acid
    """
    return AMINO_ACID_PROPERTIES.get(short_name, {}).get("type", "Unknown")


def get_codons_for_amino_acid(amino_acid: str) -> List[str]:
    """
    Get all codons that code for a specific amino acid.
    
    Args:
        amino_acid (str): 3-letter amino acid abbreviation
        
    Returns:
        List[str]: List of codons that code for the amino acid
    """
    return [codon for codon, aa in RNA_CODON_TABLE.items() if aa == amino_acid]


def is_start_codon(codon: str) -> bool:
    """
    Check if a codon is a start codon.
    
    Args:
        codon (str): RNA codon sequence
        
    Returns:
        bool: True if it's a start codon, False otherwise
    """
    return codon.upper() in START_CODONS


def is_stop_codon(codon: str) -> bool:
    """
    Check if a codon is a stop codon.
    
    Args:
        codon (str): RNA codon sequence
        
    Returns:
        bool: True if it's a stop codon, False otherwise
    """
    return codon.upper() in STOP_CODONS


if __name__ == "__main__":
    # Example usage and testing
    print("RNA Codon Table Module")
    print("=" * 30)
    
    # Test some functions
    test_codons = ["AUG", "UUU", "UAA", "UGG"]
    
    for codon in test_codons:
        aa = RNA_CODON_TABLE.get(codon, "Unknown")
        print(f"Codon {codon} -> {aa}")
        
        if aa != "Unknown" and aa != "STOP":
            full_name = get_amino_acid_full_name(aa)
            aa_type = get_amino_acid_type(aa)
            print(f"  Full name: {full_name}")
            print(f"  Type: {aa_type}")
        
        print(f"  Start codon: {is_start_codon(codon)}")
        print(f"  Stop codon: {is_stop_codon(codon)}")
        print()
