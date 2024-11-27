#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.

def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)  

    total=round(total)
    print(f"Please pay my salary ${total}")


total_calc(500,5)

