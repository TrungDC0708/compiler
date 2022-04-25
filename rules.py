import csv


class Rule:
    def __init__(self, file_path):
        self.file_path = file_path
        self.char_rules = list()


    def load_rule(self):
        with open(self.file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                self.char_rules.append(row)

        self.startingState = self.char_rules[0]
        self.endingState = self.char_rules[1]
        self.wType = self.char_rules[2]
