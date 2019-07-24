#!/usr/bin/env python3

calc1 = 0.0
calc2 = 0.0
operation = ""
while(calc1 != "q"):
    print("\nWhat is the first oeprator? Or, enter q to quit:")
    calc1 = input()
    if str(calc1).lower() == "q":
        break
    elif str(calc1).isnumeric() == False:
        print("calc1 is not numeric, enter numbers only...")
        calc1 = input()
        if str(calc1).isnumeric() == False:
            print("You have been given too many tries.. now exiting")
            break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit:")
    calc2 = input()
    if str(calc2).lower() == "q":
        break
    elif str(calc2).isnumeric() == False:
        print("calc2 is not numeric, exiting...")
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -):")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == "-":
        print("\n" + str(calc1) + " - " + str(calc2) + " =" + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting....")


