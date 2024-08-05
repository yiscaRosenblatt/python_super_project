


class Administrator_UI:

    def __init__(self):
        pass

    print("hello Administor. Choose your option:\n ")
    A = "A. List of products"
    B = "B. Add or update employees"
    C = "C. List of customers who bought that day"
    D = "D. How much money was put in today?"

    print(A + "\n" + B + "\n" + C + "\n" + D)

    optionAdministor = input("Enter the letter corresponding to your choice (A, B, C, or D): ")
    if optionAdministor == 'A':
        print("Which section? ")
        A = "A. Vegetables section "
        B = "B. Hygiene section"
        C = "C. Meat section"
        print(A + "\n" + B + "\n" + C)
        optionSection = input("Which section? (A, B or C): ")
        if optionSection == 'A':
            print("Products of the Vegetables section")
        elif optionSection == 'B':
            print("Products of the Hygiene section")
        elif optionSection == 'C':
            print("Products of the Meat section")

    elif optionAdministor == 'B':
        print("אנחנו צריכות לעשות רשימה של עובדים")

    elif optionAdministor == 'C':
        print("אנחנו צריכות לעשות רשימת לקוחות ")

    else:
        print("אנחנו צריכות לעשות רשימת מוצרים(בשביל לדעת כמה כל מוצר עולה בשביל לחשב סכום הכנסה יומי)")
