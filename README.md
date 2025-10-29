# DNA to Protein Translation Tool

A Python-based bioinformatics tool that converts DNA sequences to protein chains through transcription and translation processes.

## 🧬 Overview

This project simulates the central dogma of molecular biology by:
- Converting DNA sequences to RNA (transcription)
- Breaking RNA into codons (triplets of nucleotides)
- Translating codons to amino acids using the genetic code
- Assembling amino acids into protein chains

## ✨ Features

- **Custom DNA Input**: Enter your own DNA sequence (9-30 nucleotides, divisible by 3)
- **Random Sequence Generation**: Generate random DNA sequences for testing
- **Automatic Validation**: Input validation ensures proper DNA sequence format
- **Detailed Reports**: Generate comprehensive text reports with step-by-step process
- **Error Handling**: Robust error handling for invalid inputs

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Sukarth/CS_PROJECT_FINAL.git
cd CS_PROJECT_FINAL
```

2. Run the program:
```bash
python main.py
```

## 📖 Usage

1. **Run the program**: Execute `python main.py`
2. **Choose input method**:
   - Enter `CUSTOM` to input your own DNA sequence
   - Enter `RANDOM` to generate a random sequence
3. **Provide filename**: Enter a name for the output report file
4. **View results**: Check the generated `.txt` file for detailed analysis

### Example

```
Enter a filename for your report: my_analysis
Enter 'CUSTOM' for a custom sequence or 'RANDOM' for a random sequence: CUSTOM
Enter your custom DNA sequence (A, C, G, T). Length must be 9-30 and divisible by 3: AGTCCCTCT
Process completed. Check my_analysis.txt for information.
```

## 📁 Project Structure

```
CS_PROJECT_FINAL/
├── main.py              # Main program logic
├── Codon_Table.py       # RNA codon to amino acid mapping
├── README.md            # Project documentation
├── Documentation.pdf    # Detailed project documentation
├── Example_Input        # Sample program input
├── Example_Output       # Sample program output
└── test.txt            # Test file for development
```

## 🧪 Scientific Background

This tool implements the biological process of protein synthesis:

1. **Transcription**: DNA → RNA (A→U, T→A, C→G, G→C)
2. **Codon Formation**: RNA sequence split into triplets
3. **Translation**: Codons mapped to amino acids using genetic code
4. **Protein Assembly**: Amino acids linked to form protein chain

## 🔬 Technical Details

- **DNA Validation**: Accepts only A, C, G, T nucleotides
- **Length Requirements**: 9-30 nucleotides, must be divisible by 3
- **Start Codon**: Automatically adds AUG (Methionine) at sequence start
- **Stop Codons**: Filters out UAA, UAG, UGA codons
- **Output Format**: Amino acids joined with hyphens (e.g., Met-Ser-Gly-Arg)

## 📊 Output Report

Generated reports include:
- Original DNA sequence
- Transcribed RNA sequence
- Codon breakdown
- Amino acid sequence
- Final protein chain
- Date and author information

## ⚠️ Limitations

This is an educational tool with simplified biological modeling:
- Does not account for reading frames
- Simplified start/stop codon handling
- No consideration for post-translational modifications
- Not suitable for real-world bioinformatics applications

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Code optimization

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Sukarth Acharya** (Originally by Utsav Choudhury)
- GitHub: [@Sukarth](https://github.com/Sukarth)

## 🙏 Acknowledgments

- Based on the original work by Utsav Choudhury (L24i)
- Created as part of LCOM.e project
- Educational tool for understanding molecular biology concepts