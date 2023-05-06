import os
import csv

folder_path = 'data/*'
outcome_path = 'Intermediate/*'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        with open(os.path.join(folder_path, filename), newline='') as f:
            data = list(csv.reader(f))
            data2 = data[1:len(data)]
            first_elements = []
            int_list = []
            for row in data2:
                first_elements.append(row[0])
                int_list.append(list(map(int, row[2:-2])))
            my_list = [[first_elements[i]] + int_list[i] for i in range(len(first_elements))]
            result = {}
            for row in my_list:
                if row[0] not in result:
                    result[row[0]] = row[1:]
                else:
                    if sum(row[1:]) > sum(result[row[0]]):
                        result[row[0]] = row[1:]
                        with open(os.path.join(outcome_path, filename), 'w', newline='') as outcomes:
                            writer = csv.writer(outcomes)
                            for key, value in result.items():
                                writer.writerow([key, value])
