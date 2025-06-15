"""
CP1404/CP5632 Practical
Simple income tracker - displays monthly and total earnings
"""


def main():
    """Collect and display income data over a number of months."""
    earnings = []
    months = int(input("How many months? "))

    for i in range(1, months + 1):
        monthly_income = float(input(f"Enter income for month {i}: "))
        earnings.append(monthly_income)

    display_report(earnings)


def display_report(earnings):
    """Show the income report with running totals."""
    print("\nIncome Report\n-------------")
    cumulative = 0
    for idx, amount in enumerate(earnings, start=1):
        cumulative += amount
        print(f"Month {idx:2} - Income: ${amount:10.2f} Total: ${cumulative:10.2f}")


main()
