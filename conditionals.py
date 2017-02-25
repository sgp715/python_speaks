import evaluate

def if_(stringer):
    stringArr = stringer.split(" ")
    condArr = []

    for i in range(0, len(stringArr)):
        if stringArr[i] == "if":
            for j in range(i + 1, len(stringArr)):
                condArr.append(stringArr[j])
            break

    condFinal = " ".join(condArr)
    finalStatment = "if " + evaluate(condFinal)
    return finalStatement

def _equals_(stringer):
    stringArr = stringer.split(" ")
    condArr1 = []
    condArr2 = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == 'equals':
            index = i
            for j in range(0,index):
                condArr1.append(stringArr[j])
            for k in range (index,len(stringArr))
                condArr2.append(stringArr[k])
            break
    condFinal1 = " ".join(condArr1)
    condFinal2 = " ".join(condArr2)
    finalStatement = evaluate(condFinal1) + "equals" + evaluate(condFinal2)
