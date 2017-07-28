'''Write a  program that indicates whether a  specified month has 28, 30, or 31 days.'''
#(hint: something goes here)
print("Enter a month and I'll tell you the number of days in that month")
month = input()

day28 = [February]
day30 = [April, June, September, November]
day31 = [January, March, May, July, August, October, December]

def numDays(month):
#Your code here
    for month in day28:
        day = 28
    for month in day30
        day = 30
    for month in day31
        day = 31





    if (month = day28)
        days = 28
    elif (month = day30)
        days = 30
    elif (month = day31)
        days = 31
return days


def main():
    days =  numDays(September)
    print(days)
main()
