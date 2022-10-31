import csv
import os
import re 

def write_node_file(reader, filenum):
    print(filename)
    print(filenum)
    nodes = set()
    rows = []
    for row in reader:
        row[0].strip()
        row[1].strip()
        nodes.add(row[0])
        nodes.add(row[1])
        rows.append(row)
    print("Number of nodes", len(nodes))

    with open('./data/real_user_nodes/real_bot_user_nodes_{}.csv'.format(filenum), 'w') as f:
        writer = csv.writer(f)
        for node in nodes:
            writer.writerow([node])

def get_numbers_from_filename(filename):
    return re.search(r'\d+', filename).group(0)

directory = './data/bot_user_edge'

files = [file for file in os.listdir(directory)]
print(len(files))

for filename in files:
    try:
        if os.path.getsize(os.path.join(directory,filename)) > 0:
            with open(os.path.join(directory,filename), 'r') as openfile:
                reader = csv.reader(openfile)
                print(filename)
                write_node_file(reader, get_numbers_from_filename(filename))
    except Exception as e:
        print(filename)
        print("error:",e)

