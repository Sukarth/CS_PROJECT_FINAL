#!/usr/bin/env python3
"""
Test Suite for DNA to Protein Translation Tool

This module contains comprehensive tests for all components of the DNA translation tool.
It uses Python's built-in unittest framework to ensure code reliability.

Author: Sukarth Acharya
Date: 2025
Project: LCOM.e
"""

import unittest
import tempfile
import os
from pathlib import Path
from main import DNAProcessor, ReportGenerator
from Codon_Table import (
    RNA_CODON_TABLE, get_amino_acid_full_name, get_amino_acid_type,
    get_codons_for_amino_acid, is_start_codon, is_stop_codon
)


class TestDNAProcessor(unittest.TestCase):
    """
    Test cases for the DNAProcessor class.
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.processor = DNAProcessor()
    
    def test_validate_dna_sequence_valid(self):
        """Test validation of valid DNA sequences."""
        valid_sequences = [
            "ATCGATCGA",  # 9 nucleotides
            "ATCGATCGATCG",  # 12 nucleotides
            "ATCGATCGATCGATCGATCGATCGATC",  # 30 nucleotides
            "atcgatcga",  # lowercase should work
        ]
        
        for seq in valid_sequences:
            with self.subTest(sequence=seq):
                self.assertTrue(self.processor.validate_dna_sequence(seq))
    
    def test_validate_dna_sequence_invalid(self):
        """Test validation of invalid DNA sequences."""
        invalid_sequences = [
            "",  # empty
            "ATCG",  # too short
            "ATCGATCGATCGATCGATCGATCGATCGATC",  # too long (33)
            "ATCGATCGAT",  # not divisible by 3 (10)
            "ATCGATCGX",  # invalid character
            "123456789",  # numbers
            "ATCGATCGU",  # RNA base U instead of T
        ]
        
        for seq in invalid_sequences:
            with self.subTest(sequence=seq):
                self.assertFalse(self.processor.validate_dna_sequence(seq))
    
    def test_transcribe_dna_to_rna(self):
        """Test DNA to RNA transcription."""
        test_cases = [
            ("ATG", "AUG"),
            ("ATCG", "AUCG"),
            ("TTAAGGCC", "AAUUCCGG"),
            ("atg", "AUG"),  # lowercase input
        ]
        
        for dna, expected_rna in test_cases:
            with self.subTest(dna=dna, expected=expected_rna):
                result = self.processor.transcribe_dna_to_rna(dna)
                self.assertEqual(result, expected_rna)
    
    def test_convert_to_codons(self):
        """Test RNA to codon conversion."""
        test_cases = [
            ("AUCGAU", ["AUG", "AUC", "GAU"]),  # Start codon added, no stop codons
            ("AUCGAUUAA", ["AUG", "AUC", "GAU"]),  # Stop codon removed
            ("GGGUAG", ["AUG", "GGG"]),  # Stop codon UAG removed
        ]
        
        for rna, expected in test_cases:
            with self.subTest(rna=rna, expected=expected):
                result = self.processor.convert_to_codons(rna)
                self.assertEqual(result, expected)
    
    def test_translate_codons_to_amino_acids(self):
        """Test codon to amino acid translation."""
        test_codons = ["AUG", "UUU", "CCC", "UAA"]  # Met, Phe, Pro, STOP
        expected_aa = ["Met", "Phe", "Pro"]  # STOP codon filtered out
        
        result = self.processor.translate_codons_to_amino_acids(test_codons)
        self.assertEqual(result, expected_aa)
    
    def test_generate_random_sequence(self):
        """Test random sequence generation."""
        lengths = [9, 12, 15, 18, 21, 24, 27, 30]
        
        for length in lengths:
            with self.subTest(length=length):
                sequence = self.processor.generate_random_sequence(length)
                
                # Check length
                self.assertEqual(len(sequence), length)
                
                # Check all characters are valid DNA bases
                self.assertTrue(all(base in 'ACGT' for base in sequence))
                
                # Check sequence is valid
                self.assertTrue(self.processor.validate_dna_sequence(sequence))


class TestCodonTable(unittest.TestCase):
    """
    Test cases for the Codon_Table module functions.
    """
    
    def test_rna_codon_table_completeness(self):
        """Test that the RNA codon table contains all 64 possible codons."""
        # There should be 64 codons (4^3)
        expected_codons = 64
        self.assertEqual(len(RNA_CODON_TABLE), expected_codons)
        
        # Check some known mappings
        known_mappings = {
            "AUG": "Met",  # Start codon
            "UUU": "Phe",  # Phenylalanine
            "UAA": "STOP",  # Amber stop
            "UAG": "STOP",  # Ochre stop
            "UGA": "STOP",  # Opal stop
        }
        
        for codon, expected_aa in known_mappings.items():
            with self.subTest(codon=codon, amino_acid=expected_aa):
                self.assertEqual(RNA_CODON_TABLE[codon], expected_aa)
    
    def test_get_amino_acid_full_name(self):
        """Test getting full amino acid names."""
        test_cases = [
            ("Met", "Methionine"),
            ("Phe", "Phenylalanine"),
            ("Gly", "Glycine"),
            ("XYZ", "Unknown"),  # Invalid amino acid
        ]
        
        for short_name, expected_full_name in test_cases:
            with self.subTest(short=short_name, full=expected_full_name):
                result = get_amino_acid_full_name(short_name)
                self.assertEqual(result, expected_full_name)
    
    def test_get_amino_acid_type(self):
        """Test getting amino acid chemical types."""
        test_cases = [
            ("Phe", "Aromatic"),
            ("Leu", "Aliphatic"),
            ("Lys", "Basic"),
            ("Asp", "Acidic"),
            ("XYZ", "Unknown"),  # Invalid amino acid
        ]
        
        for aa, expected_type in test_cases:
            with self.subTest(amino_acid=aa, type=expected_type):
                result = get_amino_acid_type(aa)
                self.assertEqual(result, expected_type)
    
    def test_get_codons_for_amino_acid(self):
        """Test getting all codons for a specific amino acid."""
        # Test some amino acids with known codon counts
        test_cases = [
            ("Met", 1),  # Only AUG
            ("Trp", 1),  # Only UGG
            ("Phe", 2),  # UUU, UUC
            ("Leu", 6),  # UUA, UUG, CUU, CUC, CUA, CUG
        ]
        
        for aa, expected_count in test_cases:
            with self.subTest(amino_acid=aa, count=expected_count):
                codons = get_codons_for_amino_acid(aa)
                self.assertEqual(len(codons), expected_count)
                
                # Verify all returned codons actually code for the amino acid
                for codon in codons:
                    self.assertEqual(RNA_CODON_TABLE[codon], aa)
    
    def test_is_start_codon(self):
        """Test start codon identification."""
        self.assertTrue(is_start_codon("AUG"))
        self.assertTrue(is_start_codon("aug"))  # lowercase
        self.assertFalse(is_start_codon("UUU"))
        self.assertFalse(is_start_codon("UAA"))
    
    def test_is_stop_codon(self):
        """Test stop codon identification."""
        stop_codons = ["UAA", "UAG", "UGA"]
        
        for codon in stop_codons:
            with self.subTest(codon=codon):
                self.assertTrue(is_stop_codon(codon))
                self.assertTrue(is_stop_codon(codon.lower()))  # lowercase
        
        # Test non-stop codons
        non_stop_codons = ["AUG", "UUU", "GGG"]
        for codon in non_stop_codons:
            with self.subTest(codon=codon):
                self.assertFalse(is_stop_codon(codon))


class TestReportGenerator(unittest.TestCase):
    """
    Test cases for the ReportGenerator class.
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_filename = "test_report"
        self.report_gen = ReportGenerator(self.test_filename)
        
        # Override filepath to use temp directory
        self.report_gen.filepath = Path(self.temp_dir) / f"{self.test_filename}.txt"
    
    def tearDown(self):
        """Clean up after each test method."""
        # Remove test file if it exists
        if self.report_gen.filepath.exists():
            self.report_gen.filepath.unlink()
        
        # Remove temp directory
        os.rmdir(self.temp_dir)
    
    def test_initialize_report(self):
        """Test report initialization."""
        self.report_gen.initialize_report()
        
        # Check file was created
        self.assertTrue(self.report_gen.filepath.exists())
        
        # Check file content
        content = self.report_gen.filepath.read_text(encoding='utf-8')
        self.assertIn("DNA TO PROTEIN TRANSLATION REPORT", content)
        self.assertIn("Generated on:", content)
        self.assertIn("Tool version:", content)
    
    def test_write_section(self):
        """Test writing sections to report."""
        self.report_gen.initialize_report()
        
        test_title = "Test Section"
        test_content = "This is test content"
        
        self.report_gen.write_section(test_title, test_content)
        
        content = self.report_gen.filepath.read_text(encoding='utf-8')
        self.assertIn(test_title.upper() + ":", content)
        self.assertIn(test_content, content)
    
    def test_write_final_notes(self):
        """Test writing final notes to report."""
        self.report_gen.initialize_report()
        self.report_gen.write_final_notes()
        
        content = self.report_gen.filepath.read_text(encoding='utf-8')
        self.assertIn("IMPORTANT NOTES:", content)
        self.assertIn("educational tool", content)
        self.assertIn("Utsav Choudhury", content)
        self.assertIn("Sukarth Acharya", content)


class TestIntegration(unittest.TestCase):
    """
    Integration tests for the complete DNA to protein translation workflow.
    """
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DNAProcessor()
    
    def test_complete_workflow(self):
        """Test the complete DNA to protein translation workflow."""
        # Test with a known DNA sequence
        dna_sequence = "ATGTTCCCG"  # 9 bases, divisible by 3
        
        # Step 1: Transcription
        rna_sequence = self.processor.transcribe_dna_to_rna(dna_sequence)
        expected_rna = "AUGAAGGGC"
        self.assertEqual(rna_sequence, expected_rna)
        
        # Step 2: Convert to codons
        codons = self.processor.convert_to_codons(rna_sequence)
        # Should have start codon AUG + original codons AUG, AAG, GGC
        expected_codons = ["AUG", "AUG", "AAG", "GGC"]
        self.assertEqual(codons, expected_codons)
        
        # Step 3: Translate to amino acids
        amino_acids = self.processor.translate_codons_to_amino_acids(codons)
        expected_aa = ["Met", "Met", "Lys", "Gly"]
        self.assertEqual(amino_acids, expected_aa)
        
        # Step 4: Create protein chain
        protein_chain = '-'.join(amino_acids)
        expected_chain = "Met-Met-Lys-Gly"
        self.assertEqual(protein_chain, expected_chain)
    
    def test_workflow_with_stop_codons(self):
        """Test workflow with stop codons that should be filtered out."""
        # DNA sequence that will produce stop codons in RNA
        dna_sequence = "ATGTTCATT"  # -> AUG AAG UAA (Met-Lys-STOP)
        
        rna_sequence = self.processor.transcribe_dna_to_rna(dna_sequence)
        codons = self.processor.convert_to_codons(rna_sequence)
        amino_acids = self.processor.translate_codons_to_amino_acids(codons)
        
        # Stop codon should be filtered out
        self.assertNotIn("STOP", amino_acids)
        
        # Should contain Met (start) + Met + Lys (UAA stop codon filtered)
        expected_aa = ["Met", "Met", "Lys"]
        self.assertEqual(amino_acids, expected_aa)


def run_tests():
    """
    Run all tests and print results.
    """
    print("🧪 Running DNA Translation Tool Test Suite")
    print("=" * 50)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestDNAProcessor,
        TestCodonTable,
        TestReportGenerator,
        TestIntegration,
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"⚠️ {len(result.errors)} error(s) occurred")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
