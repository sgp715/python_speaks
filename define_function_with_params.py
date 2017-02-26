def define_function_with_params(stringer):
    stringArr = stringer.split(" ")
    index = 0
    functionNameArr = []
    varNameArr = []

    for i in range(0, len(stringArr)):
        if stringArr[i] == "function":
            for j in range (i + 1, len(stringArr)):
                if stringArr[j] == "of":
                    index = j
                    break
                functionNameArr.append(stringArr[j])
            for k in range (index + 1, len(stringArr)):
                if stringArr[k] == "and":
                    continue
                varNameArr.append(stringArr[k])
            break

    functionName = "_".join(functionNameArr)
    varName = ",".join(varNameArr)

    statement = "def " + functionName + "(" + varName + "):"


    return statement
