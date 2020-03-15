def gauss_addition(): 
    frist_number = int(input("Enter the first number : "))
    last_number = int(input("Enter the first number : "))
    result = 0
    for i in range(frist_number, last_number+1):
        result += i
    print('The reesult is : ' + str(result))

c = input("Enter the c? ")
while c != "q":
    if c == "1":
       gauss_addition()
    c = input("Enter the c? ")

print("Thanks for playing the game ")





        



