import evaluate

def for_evaluate(string):
    words = string.split()
    if words[0] != "for":
        print "Error with for"

    #search for "in"
    string1 = words[1] #assume there is a variable there
    string2 = ""
    s1 = 1
    s2 = 0 #booleans for filling which string
    for w in words[2:]:
        if w=="in":
            s1=0
            s2=1
            continue
        elif s1:
            string1 += " " + w
        elif s2:
            string2 += w + " "

    output = "for " + evaluate.evaluate(string1) + " in " + evaluate.evaluate(string2) ":"
    return output

def while_evaluate(string):
    output = "while " + evaluate.evaluate(string[6:]) + ":"
    return output
