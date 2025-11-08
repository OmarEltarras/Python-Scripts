def insert_word_on_new_line(file_path, word_to_insert):
    """
    Reads a file, inserts a specific word on a new line after every line, 
    and overwrites the original file with the modified content.

    Args:
        file_path (str): The path to the text file.
        word_to_insert (str): The word to insert on its own new line.
    """
    try:
        # 1. Read all lines from the input file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 2. Modify the list of lines
        modified_lines = []
        for line in lines:
            # Ensure the original line keeps its newline terminator
            # and then append the new word followed by another newline
            modified_lines.append(line.strip('\n') + '\n') 
            modified_lines.append(word_to_insert + '\n')
        
        # 3. Write the modified content back to the same file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)
            
        print(f"Successfully modified file: '{file_path}'")
        print(f"Inserted '{word_to_insert}' on a new line after each original line.")

    except FileNotFoundError:
        print(f"Error: Input file '{file_path}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

if __name__=="__main__":
    insert_word_on_new_line("example.txt","peter")
