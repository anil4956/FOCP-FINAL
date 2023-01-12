import sys
import random

# If no command-line argument was provided, print an error message and exit the script
if len(sys.argv) == 1:
    print("Error: Missing command-line argument.")
    sys.exit()
    
filename = sys.argv[1]
# Try to open the file specified by the command-line argument
try:
    f = open(filename)
except IOError:
    # If the file cannot be opened, print an error message and exit the script
    print("Error Cannot open",filename,"Soory about that.")
    sys.exit()
            
# Read all the lines from the file into a list
lines = f.readlines()

# Create a list of tuples to store id/name pairs
# Each tuple consists of the first 8 characters (the student ID) and the rest of the line (the name)
student_data = [(line[:8], line[9:]) for line in lines]

# Create a list to store the generated emails
emails = []
# Loop through each student in the list of tuples
for entry in student_data:
    # Extract the initials from the name
    initials = []
    for x in entry[1].split(',')[1].split():
        # Append the first character of each word to the list of initials
        initials.append(x[0])
    # Extract the surname from the name
    surname = ""
    for c in entry[1].split(',')[0]:
        # If the character is a letter, add it to the surname string
        if c.isalpha():
            surname += c
    # Create the email by combining the student ID, initials, surname, and random 4-digit number
    email = entry[0] + " " + ".".join(initials) + "." + surname
    
    # Generate 4 random digits and add it to the end of the email string
    email += str(random.randint(1000, 9999))
    
    # Add the domain to the end of the email string
    email += '@poppleton.ac.uk'
    
    # Convert the email to lowercase and add it to the list of emails
    emails.append(email.lower())
    
# Open the file 'emails.txt' for writing
with open('emails.txt', 'w') as fh:
    # Write the list of emails to the file, separated by newlines
    fh.write('\n'.join(emails))
