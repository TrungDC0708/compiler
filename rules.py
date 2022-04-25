import csv

char_rules = list()
with(open('rules.csv')) as f:
    reader = csv.reader(f)
    for row in reader:
        char_rules.append(row)



startingState = char_rules[0]
endingState = char_rules[1]
wType = char_rules[2]
print(wType)
print(startingState)
print(endingState)
print(char_rules[4])
print(wType.index("<"))