import evaluate

def if_(s):
    stringArr = s.split(" ")
    condArr = []
    if stringArr[0] == "if":
        for j in range(1, len(stringArr)):
            condArr.append(stringArr[j])

    condFinal = " ".join(condArr)
    finalStatement = "if " + evaluate.evaluate(condFinal)

    print finalStatement
    return finalStatement




def _equals_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'equals':
            index = i
            for j in range(0,index):
                condArr1.append(stringArr[j])
            for k in range (index,len(stringArr)):
                condArr2.append(stringArr[k])
            break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = (condFinal1) + "==" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _greater_than_or_equal_to_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'greater':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'to':
            end = j
            for b in range(end,len(stringArr)):
                condArr2.append(stringArr[b])
            break
        break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = (condFinal1) + ">=" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement


def _greater_than_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'greater':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'than':
            end = j
            for b in range(end,len(stringArr)):
                condArr2.append(stringArr[b])
            break
        break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + ">" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _less_than_or_equal_to_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'less':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'to':
            end = j
            for b in range(end,len(stringArr)):
                condArr2.append(stringArr[b])
            break
        break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "<=" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _less_than_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'less':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'than':
            end = j
            for b in range(end,len(stringArr)):
                condArr2.append(stringArr[b])
            break
        break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "<" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _and_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'and':
            index = i
            for j in range(0,index):
                condArr1.append(stringArr[j])
            for k in range (index,len(stringArr)):
                condArr2.append(stringArr[k])
            break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "and" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _or_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'or':
            index = i
            for j in range(0,index):
                condArr1.append(stringArr[j])
            for k in range (index,len(stringArr)):
                condArr2.append(stringArr[k])
            break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "or" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement

def _does_not_equal_(s):
    stringArr = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'does':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'equal':
            end = j
            for b in range(end,len(stringArr)):
                condArr2.append(stringArr[b])
            break
        break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "!=" + evaluate.evaluate(condFinal2)

    print finalStatement
    return finalStatement



if_("if x equals 2")
_equals_("x equals 2")
_greater_than_or_equal_to_("x greater than or equal to")
