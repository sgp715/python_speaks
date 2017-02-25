codemap = {}
with open('dict.txt', 'r') as f:
    for each in f:
        temp = each.split(",")
        temp[len(temp)-1] = temp[len(temp)-1].replace("\n", "")
        codemap[temp[0]] = temp[1]

print codemap
