import networkx
import csv

r_user_file = open("./data/real_bot_user_edge_0.csv")

real_user_file = csv.reader(r_user_file)

print(type(real_user_file))

header = []
header = next(real_user_file)
print(header)

nodes = set()
rows = []
for row in real_user_file:
        row[0].strip()
        row[1].strip()
        nodes.add(row[0])
        nodes.add(row[1])
        rows.append(row)

print("Number of nodes", len(nodes))

with open('./data/real_bot_user_nodes_0.csv', 'w') as f:
    writer = csv.writer(f)
    for node in nodes:
        writer.writerow([node])


