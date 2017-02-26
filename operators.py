import evaluate
import txt2num
#TODO:
    #nested sum speech!!! #decimal notation

def keywords():
    return ['plus','sum','add','minus','subtract','product','multiply','times','divide','divided','quotient','to','power','mod','modulus'];

def sum_evaluate(string):
    words = txt2num.num_fix(string)
    words = string.split(words)

    prefix_flag = 0
    operator_keywords = keywords()
    operator_keywords.remove('plus')
    operator_keywords.remove('sum')
    operator_keywords.remove('add') #specify for sum evaluate

    if words[0] == "sum":
        prefix_flag = 1
        if words[1] == "of":
            words = words[2:]
        elif words[1] == "up":
            words = words[2:]
        else:
            words = words[1:]

    elif words[0] == "add":
        prefix_flag = 1
        if words[1] == "up":
            words = words[2:]
        else:
            words = words[1:]

    output = words[0] #initialize the first summand
    words = words[1:]
    num_words = len(words)

    if prefix_flag: #we need to add in the plus symbols
        for w in range(num_words):
            if words[w] == "and":
                output += "+" + words[w+1]
                break
            else:
                output += "+"+words[w]

    else: #we don't need to add the plus symbols
        for w in range(num_words):
            if words[w] == "plus":
                output += "+"
            elif words[w] in operator_keywords:
                output += evaluate.evaluate(words[w:]) #pass the rest of words to evaluate
                print output
                return output
            else:
                output += words[w]
    print output
    return output

sum_evaluate('four plus zero')
sum_evaluate('four plus one plus four')
sum_evaluate('four plus two plus twenty five plus one hundred four plus four')
sum_evaluate('four plus one hundred three minus four')
sum_evaluate('sum of four four and four')
sum_evaluate('add five four and four')

def subtract_evaluate(string):
    words = txt2num.num_fix(string)
    words = string.split(words)

    prefix_flag = 0
    operator_keywords = keywords()
    operator_keywords.remove('subtract')
    operator_keywords.remove('minus') #specify for subtract evaluate

    if words[0] == "subtract": #add take away?
        prefix_flag = 1
        words = words[1:]

    output = words[0] #initialize the first difference
    words = words[1:]
    num_words = len(words)

    if prefix_flag: #we need to add in the minus symbols
        if words[1] == "from":
            output += "-"+words[2]
        else:
            output += '-'+words[1]

    else: #we don't need to add the minus symbols
        for w in range(num_words):
            if words[w] == "minus":
                output += "-"
            elif words[w] in operator_keywords:
                output += evaluate.evaluate(words[w:]) #pass the rest of words to evaluate
                print output
                return output
            else:
                output += words[w]
    print output
    return output

subtract_evaluate('one minus twenty five')
subtract_evaluate('thirty two minus one hundred nine minus one hundred and four')
subtract_evaluate('four minus three minus seventy two minus forty nine minus zero')
subtract_evaluate('seven minus six plus five')
subtract_evaluate('subtract ten from ten')

def multiply_evaluate(string):
    words = txt2num.num_fix(string)
    words = string.split(words)
    prefix_flag = 0
    operator_keywords = keywords()
    operator_keywords.remove('times')
    operator_keywords.remove('product')
    operator_keywords.remove('multiply') #specify for sum evaluate

    if words[0] == "product":
        prefix_flag = 1
        if words[1] == "of":
            words = words[2:]
        else:
            words = words[1:]

    elif words[0] == "multiply":
        prefix_flag = 1
        words = words[1:]

    output = words[0] #initialize the first summand
    words = words[1:]
    num_words = len(words)

    if prefix_flag: #we need to add in the plus symbols
        for w in range(num_words):
            if words[w] == "and":
                output += "*" + words[w+1]
                break
            if words[w] == "by":
                output += "*" + words[w+1]
                break
            else:
                output += "*"+words[w]

    else: #we don't need to add the plus symbols
        for w in range(num_words):
            if words[w] == "times":
                output += "*"
            elif words[w] in operator_keywords:
                output += evaluate.evaluate(words[w:]) #pass the rest of words to evaluate
                print output
                return output
            else:
                output += words[w]
    print output
    return output

multiply_evaluate('one times twenty five')
multiply_evaluate('thirty two times one hundred nine times one hundred and four')
multiply_evaluate('four times three times seventy two times forty nine times zero')
multiply_evaluate('seven times six plus five')
multiply_evaluate('product of one hundred and one hundred')
multiply_evaluate('multiply ten and ten')
multiply_evaluate('multiply eleven by eleven')

def mod_evaluate(string): #do txt2num
    words = txt2num.num_fix(string)
    words = string.split(words)
    output = words[0] + "%" + words[2]
    print output
    return output

mod_evaluate("four mod seven")
mod_evaluate("four thousand mod seventy six")

def exp_evaluate(string): #do txt2num
    words = txt2num.num_fix(string)
    words = string.split(words)
    output = words[0] + "**" + words[2]
    print output
    return output

exp_evaluate("four mod seven")
exp_evaluate("four thousand mod seventy six")
