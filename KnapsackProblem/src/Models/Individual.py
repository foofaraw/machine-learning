class Individual:
    def __init__(self, items, task):
        self.items = items
        self.number_of_items = len(items)
        self.task = task

    def evaluate(self):
        sum = 0
        if (self.get_total_weight() < self.task.weight_max and self.get_total_size() < self.task.size_max):
            for i in range(self.number_of_items):
                if (self.items[i] == 1):
                    sum += int(self.task.c[i])
        return sum

    def get_total_weight(self):
        sum = 0
        for i in range(self.number_of_items):
            if (self.items[i] == 1):
                sum += int(self.task.w[i])
        return sum

    def get_total_size(self):
        sum = 0
        for i in range(self.number_of_items):
            if (self.items[i] == 1):
                sum += int(self.task.s[i])
        return sum