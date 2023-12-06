import datetime

alarmHour = int(input("Enter the hour: "))
alarmMinute = int(input("Enter the minutes: "))
ampm = str(input("am or pm"))

if (ampm == "pm"):
    alarmHour = alarmHour + 12

while (1 == 1):
    if (alarmHour == datetime.datetime.now().hour and
            alarmMinute == datetime.datetime.now().minute):
        print('IT IS TIME TO WAKE UP \U0001F62D')
        break
print("EXIT")

