#Compound Interest Calculator

Principle = (float(input ("Enter the principle amount:")))
Rate = (int(input("Enter the interest rate:")))
Time = (int(input("Enter the time in years:")))

while Principle <= 0:
    Principle = (float(input ("Enter the principle amount:")))
    if Principle <= 0:
        print("Principle can't be zero or negative")

while Rate <= 0:
    Rate = (float(input ("Enter the interest rate:")))
    if Rate <= 0:
        print("Interest rate can't be zero or negative")


while Time <= 0:
    Time = (int(input ("Enter the Time:")))
    if Time <= 0:
        print("Time can't be zero or negative")

Total = Principle *  pow((1 + Rate / 100), Time)

print(f"Your Total Amount is Rs. {Total:,.2f}")
