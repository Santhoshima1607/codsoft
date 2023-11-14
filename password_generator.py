#import random module to generate random numbers
import random

lower_chars="abcdefghijklmnopqrstuvwxyz"
upper_chars=lower_chars.upper()
symbols="!@#$%^&*()_+<>?:.{}[],"
numbers="0123456789"

weak=lower_chars+upper_chars
medium=weak+numbers
strong=lower_chars+upper_chars+symbols+numbers

#generation of passwords according to its complexity
while True:
    print("\n")
    print("enter the complexity of the password\n1.Weak\n2.Medium\n3.Strong")

    choice=int(input("enter your choice:"))

    length=int(input("enter the length of the password:"))

    password=""

    def generate(word,length):
        global password
        for i in range(length):
            password=password+random.choice(word)
        print("the generated password is:",password)

    if choice==1:
        generate(weak,length)
    elif choice==2:
        generate(medium,length)
    elif choice==3:
        generate(strong,length)
    else:
        print("invalid choice")

    continue_input=input("do you want to generate another password?(yes/no):")
    if continue_input.lower()!='yes':
        break
