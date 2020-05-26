import datetime
from datetime import date
import csv


def counter():
    datelist = []  # initialize list to store date and message count pairs
    currdate = datetime.datetime(2015, 10, 8)  # set current date to the start date of message counting

    todaystring = date.today().strftime("%b %d, %Y")  # convert today's date to a string. used as end date
    datestring = currdate.strftime("%b %d, %Y")  # put date into MMM dd, YYYY format
    f = open("messages.html").read()  # read the messages file

    while datestring != todaystring:
        if datestring[4] == "0":
            datestring = datestring[:4] + datestring[5:]

        number = f.count(datestring)  # count the number of times the date appears in the file
        print datestring, " - ", number, " messages"  # debugging check
        datelist.append((datestring, number))  # add to list

        currdate += datetime.timedelta(days=1)  # next date
        datestring = currdate.strftime("%b %d, %Y")  # put date into MMM dd, YYYY format

    with open('messagecsv.csv', 'wb') as f:
        wr = csv.writer(f)
        for each in datelist:  # convert the list to a .csv file
            wr.writerow([each[0], each[1]])


if __name__ == '__main__':
    counter()