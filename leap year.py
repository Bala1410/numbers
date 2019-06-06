year = int(input(" Enter the Year : "))
if (( year%300 == 0)or (( year%3 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
