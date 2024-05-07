import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation
#print(charValues)

pwd_len = int(input("Enter desired length: "))
#Method 1:
# password = ""
# for i in range(pwd_len):
#     #print(random.choice(charValues))
#     password += random.choice(charValues)

#Method 2: Using List Comprehension syntax
#We use list comprehension when we want to call a function 
#repeatedly and store values in a list
password = "".join([random.choice(charValues) for i in range(pwd_len)])
#Added an empty string("") and .join method to join all values in 
#the list to make a single string
print(password)


# print("Your random pwd is:", password)