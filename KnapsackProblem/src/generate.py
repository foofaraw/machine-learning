import numpy as np
import csv

'''
n - number of object to choose (int)
w - maximum carrying capacity of the knapsack (int)
s - maximum knapsack size (int)
output_file - name of the file into which the task is to be saved (csv)
'''
def generate(n, w, s, output_file):
    validate_input(n, w, s)

    rows = generate_rows(n, w, s)
    val_sum = np.sum(rows, axis=0)
    while not validate_weight(val_sum[0], w) and validate_size(val_sum[1], s):
        print('Constraints not met. Generating another set of rows...')
        rows = generate_rows(n, w, s)
        val_sum = np.sum(rows, axis=0)
    
    save_file(rows, output_file)

def validate_input(n, w, s):
    if (n < 1000 or n > 2000):
        raise ValueError('n has to be in range 1000 - 2000')
    if (w < 10000 or w > 20000):
        raise ValueError('w has to be in range 10000 - 20000')
    if (s < 10000 or s > 20000):
        raise ValueError('s has to be in range 10000 - 20000')

def generate_rows(n, w, s):
    rows = [[n, w, s]]
    for _ in range(n):
        rows.append([
            np.random.randint(2, (10 * w / n) - 1), # weight w
            np.random.randint(2, (10 * s / n) - 1), # size s
            np.random.randint(2, n - 1),            # price c
        ])
    return rows

def validate_weight(sum_w, w):
    return sum_w > w * 2

def validate_size(sum_s, s):
    return sum_s > s * 2

def save_file(rows, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
