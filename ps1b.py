
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of the salary you want to save, in decimal: "))
total_cost = float(input("Enter the total cost of the house: "))
semi_annual_raise = float(input("Enter the semi annual raise as a decimal:"))

current_savings = 0.0
r = 0.04
month = 0


portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

monthly_savings = (annual_salary/12) * portion_saved




while current_savings < down_payment:
  current_savings += ((current_savings * r) / 12) + monthly_savings
  month += 1
  #while the current savings is less the down payment(time until it reachs down payment, the current savings will increment by that plus the monthly savings and the annual return. every time it does that, the month will go up by 1 and it will loop until current savings is = to down payment [the current savings wll increase everytime])
  if month % 6 == 0:
    #when the month reaches the 6th month(multiples of 6, every 6 months)
    annual_salary += annual_salary * semi_annual_raise
    #every time it reachs the 6th month, the salary will increase
    monthly_savings = (annual_salary/12) * portion_saved
#monthly_savings need to update along with that

print("It will take " + str(month) + " months.")
