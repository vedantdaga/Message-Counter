import datetime
from datetime import date
import csv


def counter():
    startyear = int(raw_input("Enter the year the messages begin (YYYY): "))
    startmonth = int(raw_input("Enter the month the messages begin (mm): "))
    startday = int(raw_input("Enter the day the messages begin (dd): "))

    currdate = datetime.datetime(startyear, startmonth, startday)  # set current date to the start date of messages
    datestring = currdate.strftime("%b %d, %Y")  # put date into MMM dd, YYYY format
    todaystring = date.today().strftime("%b %d, %Y")  # convert today's date to a string. used as end date

    """add section to allow user to read multiple files 
        and add section that reads multiple files and combines them into one
    OR
        add section that allows multi-file read/scan/search"""

    f = open("messages.html").read()  # read the messages file

    with open('messagecsv.csv', 'wb') as outputfile:
        wr = csv.writer(outputfile)
        while datestring != todaystring:
            if datestring[4] == "0":
                datestring = datestring[:4] + datestring[5:]

            number = f.count(datestring)  # count the number of times the date appears in the file
            print datestring, " - ", number, " messages"  # debugging check
            wr.writerow([datestring, number])

            currdate += datetime.timedelta(days=1)  # next date
            datestring = currdate.strftime("%b %d, %Y")  # put date into MMM dd, YYYY format


if __name__ == '__main__':
    counter()