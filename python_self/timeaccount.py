#It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
#Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.
#Examples
#(8, 7) ➞ "588 minutes and 0 seconds"
#(0, 0) ➞ "0 minutes and 0 seconds"
#(7, 9) ➞ "661 minutes and 30 seconds"
#Notes
#Consider a month has 30 days.
#Wash your hands.


per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes  = total_seconds // 60 
seconds = total_seconds % 60

print("{} minutes and {} seconds".format(minutes, seconds))