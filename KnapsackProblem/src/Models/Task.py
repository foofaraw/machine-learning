import numpy as np

class Task:
    def __init__(self, data):
        self.number_of_items = int(data[0][0])
        self.weight_max = int(data[0][1])
        self.size_max = int(data[0][2])
        
        # First row is headers, pop it
        data.pop(0)
        
        self.w, self.s, self.c = [], [], []
        for row in data:
            self.w = np.append(self.w, row[0])
            self.s = np.append(self.s, row[1])
            self.c = np.append(self.c, row[2])