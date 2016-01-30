import csv

filename = 'input.csv'

print "---Battle Tower CSV Parser---"
print "        version 0.0.2        "
print
print "Loading " + filename + "..."
print

#list to store the items
floors = [None] * 10


with open(filename, 'r') as chart:
    #filter out commented lines (start with #)
    reader = csv.reader(filter(lambda row: row[0]!='#', chart))

    #get the names of each floor (because i'm lazy)
    floor_names = next(reader)

    #initialize floors
    for i, name in enumerate(floor_names):
        floors[i] = []

    #iterate over csv and add items to table
    for row in reader:
        for i, item in enumerate(row):
            if len(item) > 0:
                floors[i].append(item)

print "Preparing Config File..."
config = open("config.txt", "w")
config.write("battletowerchestitems {\n")
for i in range(0,9):
    config.write('    ')
    config.write('S:"Floor %s"=' % str(i+1))
    for item in floors[i]:
        config.write(item)
        config.write(';')
    config.write('\n')
config.write('    S:"Top Floor"=')
for item in floors[9]:
    config.write(item)
    config.write(';')
config.write('\n}')
