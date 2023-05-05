import os
import csv

# 创建一个空字典
d = {}
i = 0
folder_path = 'final'
s = "null"
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        with open(os.path.join(folder_path, filename), newline='') as f:
            lst= list(csv.reader(f))
            i = i + 1
            # 遍历第一个列表，以第一个元素为键，以整个元组为值
            if i == 1:
                d['name'] = ['name', filename]
                for k, v in lst:
                    d[k] = [k, v]
            else:
                d['name'].append(filename)
                # 遍历第i个列表，如果键存在，则添加第二个元素到值中，否则创建一个新的键值对
                for k, v in lst:
                    if k in d:
                        d[k].append(v)
                    else:
                        d[k] = [k,]
                        for j in range(i-1):
                            # 添加到列表中
                            d[k].append(s)
                        d[k].append(v)
            for row in d.values():
                if len(row) < i+1:
                    d[row[0]].append(s)

file_name = "output.csv"
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in d.values():
        writer.writerow(row)
