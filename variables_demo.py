"""
1- Create a customer information system that includes the following details:

Customer name
Customer surname
Customer name + surname
Customer gender
Customer tc identity
Customer birth year
Customer address information
Customer age
"""
customerName = "Mehmet"
customerSurname = "Kaya"
customerNameSurname = customerName + " " + customerSurname
customerGender = True #True for male, False for female
customerTcIdentity = "11111111111"
customerBirthYear = 1987
customerAddressInformation = "Ankara"
customerAge = 2026 - customerBirthYear

"""
2- Calculate the total order amount for a customer who has placed three orders with the following amounts:

Order 1: 110 TL
Order 2: 1100.5 TL
Order 3: 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95

totalOrder = order1 + order2 + order3
print("Total Order:", totalOrder) #1567.45


