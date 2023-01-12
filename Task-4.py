import sys

def dec(c_text, shift):
    """Decrypt the ciphertext by changing the position of the letters according to the given shift."""
    # Declaring a empty string to store decrypted text
    plain_text = ""          
    # Looping through each character of given ciphertext    
    for i in c_text:
        # Checking whether current character is alphabetic or not             
        if i.isalpha():          
            # To determine if current character is an uppercase character
            if i.isupper():
                # Formulae to shift the position of current character       
                plain_text += chr((ord(i) - 65 - shift) % 26 + 65)  
            else:
                plain_text += chr((ord(i) - 97 - shift) % 26 + 97)  
        # Checking whether the current character is digit or not
        elif i.isdigit():         
            plain_text += chr((ord(i) - 48 - shift) % 10 + 48)   
        # If current character is neither an alphabetic nor a digit   
        else:
            # Append the non-alphabetic character to plain_text variable                     
            plain_text += i      
    return plain_text           

# Check if filename is provided as command line argument
if len(sys.argv) < 2:
    sys.exit()

# Opening given file, decrypting it for all shifts from 1 to 25 and printing the results  
try:
    #Opening the file in command line arguement
    with open(sys.argv[1], "r") as f:
        #Read all the contents of the cipher text
        c_text = f.read()  
            
    # Loop through shifts
    for s in range(1,22):
        # Decrypt the ciphertext with given shift        
        shift_result = dec(c_text, s)      
        print(f"Shift {s}: {shift_result}") 

# If file not found
except FileNotFoundError:
    print(f"Cannot open '{sys.argv[1]}' Sorry about that.")
    
"""
Sample messages decrypted with various shifts
Shift 14: sample_message_1
Shift 11: sample_message_2
Shift 21: sample_message_3
Shift 14: sample_message_4
"""
