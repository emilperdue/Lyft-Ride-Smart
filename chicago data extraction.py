from csv import reader
import csv
# open file in read mode

dict = {}
skip = 1
with open('Chicago Rides.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        if skip:
            skip = 0
            continue
        date = row[1].split(" ")[0]
        if date in dict.keys():
            dict[date] = dict[date] + 1
        else:
            dict[date] = 1

with open('output.csv', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(["Date", "Count"])
    for key, value in dict.items():
        csvwriter.writerow([key, value])