#  Lab 5(ii)
# Handle Divided by Zero Exception.

def divider(dividend, divisor):
    return dividend / divisor


if __name__ == "__main__":
    a = int(input("Enter Dividend: "))
    b = int(input("Enter Divisor: "))
    try:
       quotient =  divider(a, b)
       print(f"Quotient is: {quotient}")
    except ZeroDivisionError:
        print("Zero is big mystery, Enter other divisor")
    finally:
        print("END")
