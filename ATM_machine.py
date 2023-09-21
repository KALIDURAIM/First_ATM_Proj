# variables
ATM_card = "card"
pin = 1234
Money = 1000
Temp = 0

for outer in range(1, 2):  # 1,2
    # outer for loop you are the person

    print("You are in front of ATM Machine")
    print("Insert your card")
    print("Enter your pin")

    if (ATM_card == "card") & (pin == 1234):  # True

        if outer == 1:
            # ATM Machine
            while Temp <= Money:  # 0 <= 1000
                print("count", Temp, "Total amount", Money)
                Temp = Temp + 100
            print("Take your cash", Money, "rupee")

        else:
            print("User can use This card once a day")
    elif (ATM_card == "card") & (pin == 1234):
        print("Any one value is wrong")
    else:
        print("Both values are wrong")

    print("Thank you for Use !")