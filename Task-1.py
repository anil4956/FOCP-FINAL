import random

# Constants
MARVEL = ["SpiderMan","IronMan","CaptainAmerica","DoctorStrange","BlackPanther","BlackWidow","Thor","Hulk","Loki"]
          
DC = ["Superman", "Batman", "WonderWoman", "Aquaman", "Cyborg", "Flash", "GreenLantern", "MartianManhunter"]

CARS_BRANDS = ["Audi", "BMW", "Toyota", "MercedesBenz", "Volkswagen", "Ford", "Honda", "Hyundai", "Nissan", "Kia"] 
            


#Printing a welcome message.
print("Password Generator")
print("==================")
print("\n")

#Creates an empty set named passwords
passwords = set()

#Input from the user asking for the number of passwords to generate    
while True:
    password_gen = input("How many passwords are needed?:")

    #Check if the input is numeric 
    if password_gen.isnumeric():
        password_gen = int(password_gen)

        #Check if the input is in the range of 1 to 24, if not an error message will be shown.
        if password_gen==0:
            print("Please enter a value between 1 and 24")

        #Looping through the input number and generate passwords
        elif password_gen in range(1,24):
            break
        
        else:
            #Error message if the input is not between 1-24
            print("Please enter a value between 1 to 24")

    #Error message if the input is not a number    
    else:
        print("Please enter a number.")

for i in range(password_gen):
    #Loop until a unique password is generated
    while True:
        #Choose one element randomly from each list
        psd_1 = random.choice(MARVEL)
        psd_2 = random.choice(CARS_BRANDS)
        psd_3 = random.choice(DC)

        #Concatenate the elements selected to generate passwords
        password = psd_1+psd_2+psd_3 

        #Check if the password is already added in the set
        if password not in passwords:
            #Print the generated passwords
            print(f"{i+1:3} --> {password:1}")
            passwords.add(password)
            break
        
#Shows the total number of unique passwords generated
#print(len(passwords))
