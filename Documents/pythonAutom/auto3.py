"""This is the applicaiton for tips and spliting the check by the numbner of individuals 
on the resturant """

def tips_calculator():
    sub_totap_amount = float(input("Enter the sub-totla amount: "))
    tax = float(input("Enter the state tax : "))
    total_amount = sub_totap_amount + ((tax/100)* sub_totap_amount)
    return total_amount



choise = input("Enter the user choise : ")
while choise != 'q':
    if choise != 'q':
        total = tips_calculator()
        print(total)
    use_input = input("Do you wanna dive the check? ")
    if use_input == "Yes" or "Y" or "y":
        number_individual = int(input("Enter the number of individual you waan dive this check: "))
        each_individual = float(int(total)/number_individual)
        final_totpa = round(each_individual,2)
        print(final_totpa)
    choise = input("Enter the user choise : ")

print("Thansk for the tips")