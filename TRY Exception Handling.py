

def div():

    a = int(input("Please enter 1st number"))
    b = int(input("Please enter 2st number"))

    try:
        c = a/b
        print(c)
    except Exception:
        print("The number should not be ZERO.")


div()
