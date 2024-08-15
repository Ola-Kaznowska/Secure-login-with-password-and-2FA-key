import random 
import time 
from alive_progress import alive_bar 
import os


os.system("cls")

print("Welcome to password menager")

print()  

user = input("Enter the site you want to log in to: ")

My_list = ["25!v@eg_5", 
           "Juni0r Pyth0n D3v3l0p3r125",
           "3v_45@!564",
           "665431_!@h3llo W0rl8",
           "NAO 5@4_4 Vxe8725" 
           ]

Kay_2FA = ["66754", 
           "55580",
           "12950",
           "42085",
           "63064", 
           "77605",
           "65790"
           ]

for i in range(3): 
    

    print("Please wait. Password selection and 2FA one-time key is in the prograss...")

    print() 


    with alive_bar(100) as bar:
            for i in range(100):
                time.sleep(0.03)
                bar()
            
            
            
            
            
    Password = random.choice(My_list)
    Single_use_key = random.choice(Kay_2FA)

    print(f"Your one-time password for the site {user} is: {Password} One-time security key 2FA: {Single_use_key}")


    print()  

    print("Time until password expiration: ")


    with alive_bar(100) as bar:
        for i in range(100): 
            time.sleep(1.55)
            bar()
        
    print("If you didn't succeed retry")