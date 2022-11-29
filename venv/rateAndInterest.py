def bankInterestPercentage(amount, interest, duration):
    return (amount+duration*(interest*amount/100))

amount = int(input("Please enter the amount of the loan: "))
interest = int(input("Please enter the bank interest % "))
duration = int(input("Please enter the duration of the loan: "))

print("With provided values and duration, total payment will be equal to: ", bankInterestPercentage(amount,interest,duration))