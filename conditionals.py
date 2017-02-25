conditionalFlag = 0

def lessThan(inputText): {
    textStrings = inputText.split(" ")
    if (textStrings[0] == "if"):
        conditionalFlag = 1
        var1 = textStrings[1]

    if (textStrings[2,6] == "less than or equal to"):
        var2 = textStrings[7]

    text = "if (" + var1 + "<=" + var2 + "):"


    return text
}

def greaterThan(inputText): {
    textStrings = inputText.split(" ")
    if (textStrings[0] == "if"):
        var1 = textStrings[1]
        conditionalFlag = 1
    if (textStrings[2,6] == "greater than or equal to"):
        var2 = textStrings[7]

    text = "if (" + var1 + "=>" + var2 + "):"


    return text

}

def equalTo(inputText): {
    textStrings = inputText.split(" ")
    if (textStrings[0] == "if"):
        var1 = textStrings[1]
        conditionalFlag = 1
    if (textStrings[2,3] == "equal to"):
        var2 = textStrings[4]

    text = "if (" + var1 + "==" + var2 + "):"


    return text

}
