
def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        final_price= price-(discount_percent*0.01*price)
    else:
        final_price=price
        
    print(f"The final price is: {final_price}")
price=int(input("Please input the price in numbers: "))
discount_percent=int(input("Please input the discount percentage: "))
calculate_discount(price, discount_percent)