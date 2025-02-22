"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    totals = calculate_total_income(incomes)
    print_income_report(incomes, totals)

def calculate_total_income(incomes):
    """Calculate total income."""
    totals = []
    total = 0
    for income in incomes:
        total += income
        totals.append(total)
    return totals


def print_income_report(incomes, totals):
    """Print the formatted income report."""
    print("\nIncome Report\n-------------")
    for month, (income, total) in enumerate(zip(incomes, totals), start=1):
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
