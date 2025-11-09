import hashlib

def find_password_from_md5(password_file_path, target_md5_hash):
    """
    Reads a file of plain-text passwords, encrypts each one with MD5, 
    and compares it to a target MD5 hash.

    Args:
        password_file_path (str): The path to the file containing one password per line.
        target_md5_hash (str): The MD5 hash to search for (case-insensitive).

    Returns:
        str: The plain-text password if found, otherwise "Password not found".
    """
    try:
        # Normalize the target hash to lowercase for case-insensitive comparison
        target_md5_hash = target_md5_hash.lower().strip()
        
        print(f"Starting comparison for hash: {target_md5_hash}")

        with open(password_file_path, 'r', encoding='utf-8') as file:
            # Iterate through each line in the file
            for line in file:
                # Clean the line: remove leading/trailing whitespace and newlines
                password = line.strip()
                
                # Skip empty lines
                if not password:
                    continue

                # Encrypt the plain-text password using MD5
                # Hashlib requires bytes, so we encode the string to utf-8
                hash_object = hashlib.md5(password.encode('utf-8'))
                hashed_password = hash_object.hexdigest()

                # Compare the generated hash with the target hash
                if hashed_password == target_md5_hash:
                    print(f"Match found! Hashed '{password}' matches target hash.")
                    return password # Return the plain-text password immediately upon finding a match
        
        # If the loop finishes without returning, the password was not found
        return "Password not found"

    except FileNotFoundError:
        return f"Error: Password file '{password_file_path}' not found."
    except IOError as e:
        return f"An I/O error occurred: {e}"

if __name__=="__main__":
    print(find_password_from_md5("candidate_pass.txt","09f8316e29649a7f795f414ba3860fc0"))
