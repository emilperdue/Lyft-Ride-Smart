from csv import reader
import csv
# open file in read mode

lines = 0
valid = []
with open('60GB Rideshare Data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        #print(row)
        if lines == 0:
            header = row
            lines += 1
            continue
        # row variable is a list that represents a row in csv
        hp = False
        try:
            pickX = float(row[15])
            pickY = float(row[16])
            if (pickX >= 41.781 and pickX <= 41.803) and (pickY >= -87.606 and pickY <= -87.581):
                hp = True
        except:
            nothing = 1
            #print("Pick Not valid")

        try:
            dropX = float(row[18])
            dropY = float(row[19])
            if (dropX >= 41.781 and dropX <= 41.803) and (dropY >= -87.606 and dropY <= -87.581):
                hp = True
        except:
            nothing = 1
            #print("Drop Not valid")

        if hp == True:
            #print("IN HYDE PARK")
            valid.append(row)
        lines += 1

with open('output.csv', 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(header)
    for line in valid:
        csvwriter.writerow(line)