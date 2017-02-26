def wildcard(l1, l2):
    index1 = 0
    index2 = 0
    while (index1 < len(l1) and index2 < len(l2)):
        if l1[index1] == l2[index2]:
            if index1 == len(l1) - 1 and index2 < len(l2) - 1:
                index2 += 1
                continue
            if index2 == len(l2) - 1 and index1 < len(l1) - 1:
                index1 += 1
                continue
            index1 += 1
            index2 += 1
            continue
        if l1[index1] == "_":
            if len(l2) < len(l1):
                print "false"
                return False
            if index1 == len(l1) - 1 and index2 < len(l2):
                print "true"
                return True
            if index1 < len(l1) and index2 >= len(l2):
                print "False"
                return False
            index1 += 1
            index2 += 1
            for i in range(index2, len(l2)):
                if l1[index1] == l2[i]:
                    index2 = i + 1
                    index1 += 1
                    break
                if i == len(l2) - 1:
                    print "false"
                    return False
        if l2[index2] == "_":
            if len(l1) < len(l2):
                print "false"
                return False
            if index2 == len(l2) - 1 and index1 < len(l1):
                print "true"
                return True
            if index2 < len(l2) and index1 >= len(l1):
                print "False"
                return False
            index1 += 1
            index2 += 1
            for i in range(index1, len(l1)):
                if l2[index2] == l1[i]:
                    index1 = i + 1
                    index2 += 1
                    break
                if i == len(l1) - 1:
                    print "false"
                    return False
        if index1 == len(l1) - 1 or index2 == len(l2) - 1:
            print "true"
            return True



wildcard(["_", "bottom", "jeans"], ["apple", "pear", "bottom", "jeans"]) #-> true
wildcard(["apple", "bottom", "_"], ["apple", "bottom"]) #-> false
wildcard(["apple", "_", "bottom", "_", "jeans"], ["apple", "pear", "chipotle", "bottom", "shirts", "jeans"])
wildcard(["apple", "bottom", "_"], ["apple", "bottom", "jeans", "pants"]) #-> true
wildcard(["apple", "bottom", "jeans"], ["apple", "_", "jeans"]) #-> true
wildcard(["apple", "_", "jeans"], ["apple", "jeans"]) #-> false
wildcard(["apple", "_", "jeans"], ["apple", "pear", "bottom", "jeans"]) #-> true
