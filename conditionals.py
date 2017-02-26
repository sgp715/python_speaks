import evaluate
import txt2num

def if_(s):
    if s != "":

        stringArr = txt2num.num_fix(s)
        stringArr = stringArr.split(" ")

        original = s.split(" ")
        condArr = []
        if stringArr[0] == "if":
            for j in original[1:]:
                condArr.append(j)

        condFinal = ""
        for each in condArr:
            if condFinal == "":
                condFinal = each
            else:
                condFinal = condFinal + " "+each

        finalStatement = "if " + evaluate(condFinal) + ":"

    return finalStatement




def _equals_(s):
    if s != "":

        stringArr = txt2num.num_fix(s)
        stringArr = stringArr.split(" ")
        original = s.split(" ")
        condArr1 = []
        condArr2 = []

        for i in range(0, len(stringArr)):
            if stringArr[i] == 'equals':
                index = i
                condArr1.append(stringArr[i-1])
                for k in range (index+1,len(stringArr)-1):
                    condArr2.append(original[k])
                break
        condFinal1 = "".join(condArr1)
        condFinal2 = "".join(condArr2)
        finalStatement = (condFinal1) + "==" + evaluate(condFinal2)
    return finalStatement

def _greater_than_or_equal_to_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    while "" in stringArr:
        stringArr.remove("")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'greater':
            start = i
            for a in range(0,start):
                condArr1.append(stringArr[a])
            break
    end = stringArr[start:].index('to')
    for each in stringArr[start:][end+1:]:
        condArr2.append(each)



    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)

    finalStatement = (condFinal1) + ">=" + evaluate(condFinal2)


    return finalStatement


def _greater_than_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'greater':
            start = i
            for a in range(0,start):
                condArr1.append(original[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'than':
            end = j+1
            for b in range(end,len(stringArr)):
                condArr2.append(original[b])
            break
        break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + ">" + evaluate.evaluate(condFinal2)

    return finalStatement

def _less_than_or_equal_to_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'less':
            start = i
            for a in range(0,start):
                condArr1.append(original[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'to':
            end = j+1
            for b in range(end,len(stringArr)):
                condArr2.append(original[b])
            break
        break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "<=" + evaluate.evaluate(condFinal2)


    return finalStatement

def _less_than_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'less':
            start = i
            for a in range(0,start):
                condArr1.append(original[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'than':
            end = j+1
            for b in range(end,len(stringArr)):
                condArr2.append(original[b])
            break
        break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "<" + evaluate.evaluate(condFinal2)


    return finalStatement

def _and_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'and':
            index = i
            for j in range(0,index):
                condArr1.append(original[j])
            for k in range (index+1,len(stringArr)):
                condArr2.append(original[k])
            break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "and" + evaluate.evaluate(condFinal2)


    return finalStatement

def _or_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'or':
            index = i
            for j in range(0,index):
                condArr1.append(original[j])
            for k in range (index+1,len(stringArr)):
                condArr2.append(original[k])
            break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "or" + evaluate.evaluate(condFinal2)


    return finalStatement

def _does_not_equal_(s):
    stringArr = txt2num.num_fix(s)
    stringArr = stringArr.split(" ")
    original = s.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0,len(stringArr)):
        if stringArr[i] == 'does':
            start = i
            for a in range(0,start):
                condArr1.append(original[a])
            break
    for j in range(start,len(stringArr)):
        if stringArr[j] == 'equal':
            end = j+1
            for b in range(end,len(stringArr)):
                condArr2.append(original[b])
            break
        break
    condFinal1 = "".join(condArr1)
    condFinal2 = "".join(condArr2)
    finalStatement = evaluate.evaluate(condFinal1) + "!=" + evaluate.evaluate(condFinal2)


    return finalStatement



# if_("if x equals 2")
# _equals_("x equals 2")
# _greater_than_or_equal_to_("x greater than or equal to")
