annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of the salary you want to save, in decimal: "))
total_cost = float(input("Enter the total cost of the house: "))

current_savings = 0.0
r = 0.04
month = 0

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

monthly_savings = (annual_salary/12) * portion_saved

while current_savings < down_payment:
    current_savings += ((current_savings * r) / 12) + monthly_savings
    month += 1
print("The number of months it will take is: " + str(month))

