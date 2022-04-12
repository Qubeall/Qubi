# task 7

income = int(input("Enter your income: "));

if 0 <= income <= 15527:
  income = income = int(input())

elif 15527 <= income <= 42708:
  income = income * 0.15

elif 42708 <= income <= 132406:
  income = income * 0.25

elif 132406 <= income:
  income = income * 0.28

else:
   print("Please select a valid input.");

print('Your tax is %d' % (income))