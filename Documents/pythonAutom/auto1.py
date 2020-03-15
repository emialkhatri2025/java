#create the funcation 
def burger():
    print('here is burger! Enjoy')

def soda():
    print('here is soda! Enjoy')
def cock():
    print('here is cock! Enjoy')
def combo():
    print('here is combo! Enjoy')



print("""Welsocme to the Nepal Resturant. What ould you like to do?
    1:ordered the burger'
    '2:order the soda'
    '3:order the  cock'
    '4:order the combo'
    '0: to quite the menuw'
""")
choises = ''
while choises != '0':
   
    choises = input("What do you want to do ?")
    if choises =='1':
        burger()
    elif choises =='2':
        soda()
    elif choises =='3':
        cock()
    elif choises =='4':
        combo()
    elif choises =='0':
        print(' You did not order anything')
else:
    print("tThank you")