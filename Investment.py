# Created a program that allows user to access 2 different calculators 

# inserted import math function as instructed 
import math 

# printed out to 2 options for the user to choose from 
print("investment - to calculate the amount of interest you'll earn on your bond")
print("investment bond - to calculate the amount you'll have to pay on a home loan")
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()

# created variables to store data
opt1 ='investment'
opt2 ='bond'

# used if statement and boolean values and operators 
if user_input != opt1 and user_input != opt2:
    print("invalid option please try again")
    user_input = input(" Enter either 'investment' or 'bond': ")

 # used if statment,input(function),int(function) 
if user_input == opt1:
    amount_being_deposit = int(input("Enter the Deposited amount:"))
    actual_interest = int(input("Enter the interest rate:")) /100
    years_of_investment = int(input("Enter the number of years of the investment:"))
    
     # used .lower(function) and input function 
    interest = input("Do you want 'simple' or 'compound interest' ?: ").lower()
    
# used if,elif,else statments,.format,round function to calculate the interests.  
    if interest == 'simple':
       simple_amount = amount_being_deposit * (1 + (actual_interest*years_of_investment))
       print("Your Simple interest investment is R {}".format(round(simple_amount,2)))
    
    elif interest =='compound':
        compound_amount = amount_being_deposit * math.pow((1 + actual_interest ),years_of_investment)
        print("Your compound interest investment is R {}".format(round(compound_amount,2)))
    
    else:
        print("invalid option please try again")
        alternative_option = input("Enter either Simple or Compound interest:").lower()
        print(alternative_option)

# used if statement to caluclate the repayment    
if  user_input == opt2:
    present_value = int(input("Enter the Present value of the house:R"))
    bond_interest = int(input("Enter the interest rate:")) /100 /12
    bond_months = int(input("Enter the number of months to repay the bond:"))
    
    Repayment = ((bond_interest * present_value) / ( 1 - ( 1 + bond_interest ) ** (- bond_months)))
    print("Your repayment amount is R {}".format(round(Repayment,2)))
   











    








 




 
