import string
import random
import pandas as pd
from pandas import DataFrame

fName = input("Enter the user's first name: ")
lName = input("Enter the user's last name: ")
# Optional: Uncomment this line to ask for a job title
# jobTitle = input("Enter the user's job title: ")
pEmail = input("Enter the user's personal email: ")
pNumber = input("Enter the user's phone number: ")
# Optional: Uncomment this line to ask for an ID number
# sId = input("Enter the user's Staff ID Number: ")

# Optional: format username as fexample@example.com
nameFormatted = (fName[0]+lName).lower()
nameNet = (fName[0]+lName+"@gmail.com").lower()

# function to generate random password


def randomPassword():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    # Optional: uncomment this line to include special characters
    # Note: Including special characters may break Markdown formatting
    # special = string.punctuation

    allCharacters = lower + upper + number
    tempString = random.sample(allCharacters, 16)
    password = "".join(tempString)
    return password


# Build the Pandas Dataframe
df = pd.DataFrame(
    data={'Service': ['Meta', 'Apple ID', 'Amazon', 'Google'], 'Username': [pEmail, pEmail, pEmail, pEmail], 'Password': [randomPassword(), randomPassword(), randomPassword(), randomPassword()], 'Updated?': ['', '', '', '']
          })

print(5 * "\n")
print("## User: "+fName+" "+lName)
# Optional: uncomment this line to include user's ID number
# print("ID: "+sId)
print("#### "+pEmail+" "+pNumber)
print(df.to_markdown())
print(5 * "\n")
