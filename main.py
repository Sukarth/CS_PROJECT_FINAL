#!/usr/bin/env python3
"""
DNA to Protein Translation Tool

A bioinformatics tool that converts DNA sequences to protein chains through
transcription and translation processes.

Author: Sukarth Acharya (Originally by Utsav Choudhury)
Date: 2025
Project: LCOM.e
"""

import random
import sys
from datetime import date
from pathlib import Path
from typing import List, Tuple, Optional

# Import the RNA codon table
from Codon_Table import RNA_CODON_TABLE


class DNAProcessor:
    """
    A class to handle DNA sequence processing and protein translation.
    """
    
    def __init__(self):
        self.base_transcription = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        self.valid_bases = set('ACGT')
        self.stop_codons = {'UAA', 'UAG', 'UGA'}
        self.start_codon = 'AUG'
    
    def validate_dna_sequence(self, sequence: str) -> bool:
        """
        Validate DNA sequence format and constraints.
        
        Args:
            sequence (str): DNA sequence to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not sequence:
            return False
        
        # Check length constraints
        if not (9 <= len(sequence) <= 30):
            return False
        
        # Check if length is divisible by 3
        if len(sequence) % 3 != 0:
            return False
        
        # Check if all characters are valid DNA bases
        return all(base in self.valid_bases for base in sequence.upper())
    
    def transcribe_dna_to_rna(self, dna_sequence: str) -> str:
        """
        Transcribe DNA sequence to RNA sequence.
        
        Args:
            dna_sequence (str): DNA sequence
            
        Returns:
            str: RNA sequence
        """
        return ''.join(self.base_transcription[base] for base in dna_sequence.upper())
    
    def convert_to_codons(self, rna_sequence: str) -> List[str]:
        """
        Convert RNA sequence to list of codons and add start codon.
        
        Args:
            rna_sequence (str): RNA sequence
            
        Returns:
            List[str]: List of codons with start codon added
        """
        codons = [rna_sequence[i:i + 3] for i in range(0, len(rna_sequence), 3)]
        codons.insert(0, self.start_codon)
        
        # Filter out stop codons
        return [codon for codon in codons if codon not in self.stop_codons]
    
    def translate_codons_to_amino_acids(self, codons: List[str]) -> List[str]:
        """
        Translate codons to amino acids.
        
        Args:
            codons (List[str]): List of codons
            
        Returns:
            List[str]: List of amino acids
        """
        amino_acids = [RNA_CODON_TABLE.get(codon, "Unknown") for codon in codons]
        
        # Filter out unknown and stop codons
        return [aa for aa in amino_acids if aa not in {"Unknown", "STOP"}]
    
    def generate_random_sequence(self, length: int) -> str:
        """
        Generate a random DNA sequence of specified length.
        
        Args:
            length (int): Length of sequence to generate
            
        Returns:
            str: Random DNA sequence
        """
        return ''.join(random.choice('ACGT') for _ in range(length))


class ReportGenerator:
    """
    A class to handle report generation and file operations.
    """
    
    def __init__(self, filename: str):
        self.filename = filename
        self.filepath = Path(f"{filename}.txt")
    
    def initialize_report(self) -> None:
        """
        Create and initialize a new report file with header.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.write("=" * 50 + "\n")
            file.write("DNA TO PROTEIN TRANSLATION REPORT\n")
            file.write("=" * 50 + "\n\n")
            file.write(f"Generated on: {date.today()}\n")
            file.write(f"Tool version: 2.0\n\n")
            file.write("-" * 50 + "\n\n")
    
    def write_section(self, title: str, content: str) -> None:
        """
        Write a section to the report file.
        
        Args:
            title (str): Section title
            content (str): Section content
        """
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.write(f"{title.upper()}:\n")
            file.write(f"{content}\n\n")
    
    def write_final_notes(self) -> None:
        """
        Add final notes and disclaimer to the report.
        """
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.write("-" * 50 + "\n")
            file.write("IMPORTANT NOTES:\n")
            file.write("• This is an educational tool for learning purposes\n")
            file.write("• Results are simplified and not suitable for real research\n")
            file.write("• Does not account for reading frames or regulatory sequences\n\n")
            file.write("-" * 50 + "\n")
            file.write("Original concept by: Utsav Choudhury (2025)\n")
            file.write("Enhanced by: Sukarth Acharya (2025)\n")
            file.write("Project: LCOM.e\n")


class UserInterface:
    """
    A class to handle user interaction and input validation.
    """
    
    def __init__(self, dna_processor: DNAProcessor):
        self.dna_processor = dna_processor
    
    def get_filename(self) -> str:
        """
        Get filename for the report from user.
        
        Returns:
            str: Filename for the report
        """
        while True:
            filename = input("\nEnter filename for your report (no extension needed): ").strip()
            if filename:
                if Path(f"{filename}.txt").exists():
                    overwrite = input(f"File '{filename}.txt' already exists. Overwrite? (y/n): ")
                    if overwrite.lower().startswith('y'):
                        return filename
                else:
                    return filename
            print("Please enter a valid filename.")
    
    def get_sequence_choice(self) -> str:
        """
        Get user choice for sequence input method.
        
        Returns:
            str: User choice ('CUSTOM' or 'RANDOM')
        """
        print("\nSequence Input Options:")
        print("1. CUSTOM - Enter your own DNA sequence")
        print("2. RANDOM - Generate a random DNA sequence")
        
        while True:
            choice = input("\nEnter your choice (CUSTOM/RANDOM or 1/2): ").strip().upper()
            if choice in ['CUSTOM', '1']:
                return 'CUSTOM'
            elif choice in ['RANDOM', '2']:
                return 'RANDOM'
            else:
                print("Invalid choice. Please enter 'CUSTOM', 'RANDOM', '1', or '2'.")
    
    def get_custom_sequence(self) -> str:
        """
        Get and validate custom DNA sequence from user.
        
        Returns:
            str: Valid DNA sequence
        """
        print("\nCustom DNA Sequence Requirements:")
        print("• Length: 9-30 nucleotides")
        print("• Must be divisible by 3")
        print("• Only use A, C, G, T characters")
        
        while True:
            sequence = input("\nEnter your DNA sequence: ").strip().upper()
            
            if self.dna_processor.validate_dna_sequence(sequence):
                return sequence
            else:
                print("❌ Invalid sequence. Please check the requirements and try again.")
                
                # Provide specific feedback
                if len(sequence) < 9 or len(sequence) > 30:
                    print(f"   Length is {len(sequence)}, must be between 9-30.")
                elif len(sequence) % 3 != 0:
                    print(f"   Length {len(sequence)} is not divisible by 3.")
                elif not all(base in 'ACGT' for base in sequence):
                    invalid_chars = set(sequence) - set('ACGT')
                    print(f"   Invalid characters found: {', '.join(invalid_chars)}")
    
    def get_random_sequence_length(self) -> int:
        """
        Get length for random sequence from user.
        
        Returns:
            int: Valid sequence length
        """
        print("\nRandom Sequence Length:")
        print("• Must be between 9-30")
        print("• Must be divisible by 3")
        print("• Available options: 9, 12, 15, 18, 21, 24, 27, 30")
        
        while True:
            try:
                length = int(input("\nEnter sequence length: "))
                if 9 <= length <= 30 and length % 3 == 0:
                    return length
                else:
                    print("❌ Length must be between 9-30 and divisible by 3.")
            except ValueError:
                print("❌ Please enter a valid number.")


def main() -> None:
    """
    Main function to run the DNA to Protein translation tool.
    """
    print("🧬 DNA to Protein Translation Tool")
    print("=" * 40)
    print("Welcome! This tool converts DNA sequences to protein chains.")
    
    try:
        # Initialize components
        dna_processor = DNAProcessor()
        ui = UserInterface(dna_processor)
        
        # Get user inputs
        filename = ui.get_filename()
        report_generator = ReportGenerator(filename)
        
        choice = ui.get_sequence_choice()
        
        if choice == 'CUSTOM':
            dna_sequence = ui.get_custom_sequence()
            sequence_source = "Custom input"
        else:
            length = ui.get_random_sequence_length()
            dna_sequence = dna_processor.generate_random_sequence(length)
            sequence_source = f"Randomly generated (length: {length})"
        
        # Process the sequence
        print("\n🔄 Processing sequence...")
        
        # Transcription: DNA to RNA
        rna_sequence = dna_processor.transcribe_dna_to_rna(dna_sequence)
        
        # Convert to codons
        codons = dna_processor.convert_to_codons(rna_sequence)
        
        # Translation: codons to amino acids
        amino_acids = dna_processor.translate_codons_to_amino_acids(codons)
        
        # Create final protein chain
        protein_chain = '-'.join(amino_acids)
        
        # Generate report
        print("\n📝 Generating report...")
        report_generator.initialize_report()
        report_generator.write_section("Sequence Source", sequence_source)
        report_generator.write_section("Original DNA Sequence", dna_sequence)
        report_generator.write_section("Transcribed RNA Sequence", rna_sequence)
        report_generator.write_section("Codons (with start codon)", str(codons))
        report_generator.write_section("Amino Acids", str(amino_acids))
        report_generator.write_section("Final Protein Chain", protein_chain)
        report_generator.write_final_notes()
        
        # Display results
        print("\n✅ Process completed successfully!")
        print(f"\n📊 Results Summary:")
        print(f"   DNA Sequence: {dna_sequence}")
        print(f"   RNA Sequence: {rna_sequence}")
        print(f"   Protein Chain: {protein_chain}")
        print(f"   Report saved as: {filename}.txt")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
