
# importing the libraries needed for the project. The "from" simply imports a smaller piece of a larger library.
import random
from datetime import date

# importing the RNA_CODON_TABLE contained in Codon_Table.py. The list is not included in this file, as it is long.
from Codon_Table import RNA_CODON_TABLE


def write_to_report(data, name):
    """
    Utility function to write information into a text file.

    :param: data (str): The data to be written to the file.
    :param: name (str): The name of the file where the data will be stored (without file extension).
    :return: None.
    """
    with open(f'{name}.txt', 'a') as file:
        # The 'a' mode is used to append data to the file, preserving previous content.
        # with() automatically closes the file after execution, conserving system resources.
        # This is important, as it will be used many times in the program, helping to keep the code clean and conserve resources.
        file.write(data)


def validate_custom_sequence():
    """
    Prompts the user for a custom DNA sequence and validates the input according to the given criteria.

    :return: Valid DNA and RNA sequences.
    """
    base_transcription = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}  # Mapping of DNA to RNA bases with a dictionary.
    # This makes it easy to access a value from another, e,g accessing U from A.
    while True:
        user_input = input(
            "Enter your custom DNA sequence (A, C, G, T). Length must be 9-30 and divisible by 3: ").upper()
        if 9 <= len(user_input) <= 30 and len(user_input) % 3 == 0:
            if all(base in "ACGT" for base in user_input):
                # The all() function takes in one parameter, an iterable, and returns a boolean value (True or False).
                # E.g. in this case, the function iterates over user_input.
                # The function checks if user_input is only made up of a sequence of the letters "A" "G" "C" "T".
                # If the value comes back as "True", the if statement will progress to return.
                # If the value comes back as "False", the loop will continue.
                rna_sequence = "".join(base_transcription[base] for base in user_input)
                # Transcripts to RNA with the dictionary defined in the function.
                return user_input, rna_sequence  # Returns both DNA and RNA in a tuple.
        print("Invalid input. Please follow the criteria.")


def get_sequence_input():
    """
    Prompts the user to choose between entering a custom sequence or generating a random sequence.

    :return: Returns either custom DNA and RNA sequences or the string "RANDOM" to indicate random sequence generation.
    """
    while True:
        choice = input("Enter 'CUSTOM' for a custom sequence or 'RANDOM' for a random sequence: ").upper()
        if choice == "CUSTOM":
            return validate_custom_sequence()  # If CUSTOM is chosen, validates the input.
        elif choice == "RANDOM":
            return "RANDOM"  # If RANDOM is chosen, returns the string "RANDOM".
        else:
            print("Invalid choice. Please enter 'CUSTOM' or 'RANDOM'.")


def generate_random_sequence():
    """
    The function accepts user input regarding the length of a random sequence.

    :return: Returns the random DNA chain and its corresponding RNA chain.
    """
    base_transcription = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}  # mapping DNA to RNA with dictionary
    # This makes it easy to access a value from another, e,g accessing U from A.
    while True:
        try:  # Tries some operation. This is important, as users may decide to input strings instead of numbers.
            sequence_length = int(input("Enter a length (9-30, divisible by 3) for the random sequence: "))
            # Converts the string to an integer. If the string is made up of text, it will throw a ValueError.
            # We deliberately try to trigger a ValueError with int() so that we can deal with it in the ValueError block.
            if 9 <= sequence_length <= 30 and sequence_length % 3 == 0:
                break
            else:
                print("Length must be between 9-30 and divisible by 3.")
        except ValueError:
            # Triggered in the case of a ValueError e.g. "Hello" was inputted instead of "9".
            # "Hello" can obviously not be converted to an integer like we tried to do in line 67.
            # Important as we can address the error without it crashing the program.
            print("Invalid input. Please enter a valid number.")
    dna_sequence = "".join(random.choice("ACGT") for _ in range(sequence_length))  # Forms the DNA sequence.
    # random.choice() is randomly choosing between characters in the "ACGT" expression.
    # It does this 'n' times, where 'n' is the length of the sequence.
    rna_sequence = "".join(base_transcription[base] for base in dna_sequence)  # Transcribes to RNA.
    return dna_sequence, rna_sequence  # Returns both values as a tuple.


def convert_to_codons(sequence):
    """
    Takes in an RNA sequence, and breaks it up into codons (groups of 3 e.g. "AUG"), putting them into a list.
    Furthermore, modifies the list, deleting "STOP" codons, which do not have a corresponding amino acid.
    A "START" codon is also added.

    :param: sequence (str): RNA sequence: a string of the letters "A" "C" "G" "U".
    :return: Returns a processed list of codons.
    """
    codon_list = [sequence[i:i + 3] for i in range(0, len(sequence), 3)]  # Split the sequence into groups of 3.
    codon_list.insert(0, "AUG")  # Add the start codon "AUG" at the beginning.
    codon_list_processed = [codon for codon in codon_list if codon not in {"UAA", "UAG", "UGA"}] # Remove stop codons.
    # This is accurate, as in biology, stop codons are removed, and sequences typically start with AUG.
    return codon_list_processed


def get_file_names():
    """
    Takes input regarding the names of the files in which to store data.
    :return: The name of the file
    """
    # Prompts the user for report filename
    while True:
        # Asks the user for a filename for the report file.
        # Ensures the input is not empty and warns about overwriting existing files.
        text_file_name = input("Enter a filename for your report\n"
                               "No file extension needed. However, please note that if a file "
                               "with this name already exists, it will be overwritten: ")
        if text_file_name != "":
            break

    return text_file_name


def initialize_report(text_file_name):
    """
    Creates and initializes a new report file with a header and current date.

    :param: text_file_name (str): Name of the text file to create the report in.
    :return: None.

    """
    # Opens the report file in write mode.
    # This creates a new file or overwrites an existing file with the specified name.
    with open(f'{text_file_name}.txt', 'w') as file:
        # Write the report header, including the current date.
        file.write("REPORT\n\n")
        file.write(f'DATE: {date.today()}\n\n')


def process_user_input(text_file_name):
    """
    Processes user input for DNA/RNA sequence, either randomly generated or custom... :param: text_file_name (str): Name of the report file to write input details

    :return: A tuple containing the original sequence and RNA sequence
    """
    # Gets the user's choice for DNA sequence input or requests a random sequence.
    user_choice = get_sequence_input()
    if user_choice == "RANDOM":
        # Generates a random RNA sequence if the user opts for RANDOM.
        # Also uses user input for the length of the random sequence.
        input_sequence = generate_random_sequence()
        # Writes the randomly generated sequence to the report.
        write_to_report(f'BASE ARRANGEMENT: {input_sequence[0]}\n\n', text_file_name)
    else:
        # If the user provides their own valid sequence, uses it as is.
        input_sequence = user_choice
        # Writes the user-provided sequence to the report.
        write_to_report(f'Your DNA sequence choice was: {input_sequence[0]}\n\n', text_file_name)
    return input_sequence


def process_rna_sequence(input_sequence, text_file_name):
    """
    Processes the RNA sequence by converting it to codons and writing to report.

    :param: input_sequence (tuple): Tuple containing original and RNA sequences
    :param: text_file_name (str): Name of the report file to write sequence details

    returns: List of codons derived from the RNA sequence
    """
    # Converts the RNA sequence into codons (triplets of bases).
    codons = convert_to_codons(input_sequence[1])
    # Writes the RNA sequence and its codons to the report.
    write_to_report(f'RNA sequence: {input_sequence[1]}\n\n', text_file_name)
    write_to_report(f'Codons: {codons}\n\n', text_file_name)
    return codons


def translate_and_process_codons(codons, text_file_name):
    """
    Translates codons to amino acids and filters out unknown or STOP codons.

    :param: codons (list): List of codons to translate
    :param: name of text file

    :return: Processed list of amino acids
    """
    # Translates the codons into their corresponding amino acids using the RNA_CODON_TABLE.
    translated_sequence = [RNA_CODON_TABLE.get(codon, "Unknown") for codon in codons]
    # Unknown is used if no match is found.
    # Filters out "Unknown" and "STOP" codons from the translated sequence for clarity.
    # At this stage, "STOP" and "Uknown" are unlikely to exist; however, this filtering condition is just for safety.
    # "STOP" would be for "STOP" codons.
    translated_list_processed = [AA for AA in translated_sequence if AA not in {"Unknown", "STOP"}]
    write_to_report(f'Amino Acids: {translated_list_processed}\n\n', text_file_name)
    return translated_list_processed


def create_and_write_final_chain(translated_list_processed, text_file_name):
    """
    Creates a final protein chain by joining amino acids and writes to report.

    :param: translated_list_processed (list): List of amino acids
    :param: text_file_name (str): Name of the report file

    :return: Final protein chain with amino acids separated by hyphens
    """
    # Combines the amino acids into a final protein chain, separated by hyphens.
    final_chain = "-".join(translated_list_processed)
    # Writes the final protein chain to the report.
    write_to_report(f'FINAL CHAIN: {final_chain}\n\n', text_file_name)
    return final_chain


def finalize_report(text_file_name):
    """
    Adds final notes and author information to the report.

    :param: text_file_name (str): Name of the report file
    """
    # Adds a disclaimer to the report about the accuracy and context of the results.
    write_to_report('NOTE: NOT A FULLY ACCURATE REPRESENTATION. NOT APPLICABLE TO REAL LIFE CONTEXTS.\n\n',
                    text_file_name)
    # Includes author information in the report for attribution.
    write_to_report('UTSAV CHOUDHURY 2025\n\n', text_file_name)


def print_completion_message(text_file_name):
    """
    Prints completion messages.

    :param: text_file_name (str): Name of the text report file
    """
    print(f'Process completed. Check {text_file_name}.txt for information.')


def main():
    text_file_name = get_file_names() # Gets the file names and stores them in different variables.
    initialize_report(text_file_name) # Adds some basic information into the report.
    input_sequence = process_user_input(text_file_name) # Gets the RNA and DNA sequences and writes them into the report.
    codons = process_rna_sequence(input_sequence, text_file_name) # Returns codons and writes them into text file.
    translated_list_processed = translate_and_process_codons(codons, text_file_name)
    # Returns the translated list from the codons and writes them into the text document.
    final_chain = create_and_write_final_chain(translated_list_processed, text_file_name)
    # Creates the final chain and writes it into a text document.
    # Fetches compound info and writes it in the text document if possible.
    finalize_report(text_file_name)
    # Adds finishing touches to the report.
    print_completion_message(text_file_name)
    # Alerts user of completed process.

if __name__ == "__main__":  # Ensures that the script’s main logic runs only when the script is executed directly.
    main()  # Prevents main() from running automatically when the script is imported as a module in another script.
