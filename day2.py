
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('welcome to the tip calculator')
total=float(input('what was the total bill? $'))
percentage=int(input('what percentage tip would you like to give? 10, 12, or 15? '))
people=int(input('how many people to split the bill? '))
result=(total / people) * (1+(percentage/100))

result=round(result,2)
result='{:.2f}'.format(result)
print(f'each person should pay: ${result}')