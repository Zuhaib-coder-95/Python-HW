def calculate_change(bill, paid):
    change = paid - bill
    return change

bill_amount = 2.50
paid_amount = 4.00

change_to_return = calculate_change(bill_amount, paid_amount)

print("Change to return: $", change_to_return)