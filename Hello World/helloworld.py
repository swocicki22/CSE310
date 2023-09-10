print('Well, hello there buddy, I hope you are ready for this')

value = "Hello World"

question = input("Would you like to see the program? (Y/N) ")
if question == "Y":
    print(value)
elif question == "N":
    print("Well thats too bad, goodbye. ")
    quit()
else:
    print("Input not accepted. ")