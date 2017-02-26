from define_function_with_params import define_function_with_params
import txt2num
def paths(tree, cur=()):
    if not tree:
        yield cur
    else:
        if isinstance(tree, dict):
            for n, s in tree.items():
                for path in paths(s, cur+(n,)):
                    yield path
        else:
            yield cur, tree



def walk(s, node, keylist=[]):
    for key, item in node.items():
        if isinstance(item, dict):
            keylist.append(key)
            walk(s,item, keylist)
            keylist = []
        else:
            keylist.append(key)

            return item(s)

def check_bucket(s):
    """Determines what bucket the string falls into
    Input: String
    Ouput: String"""
    words = string.split(" ")


def define_class(s):
    return 0

def for_loop(s):
    return 0

def while_loop(s):
    return 0

def let_equal(s):
    return 0

def make_new_list(s):
    return 0

def make_new_dictionary(s):
    return 0

def list_object(s):
    return 0

def dictionary_object(s):
    return 0

def sum_of(s):
    return 0

def product_of(s):
    return 0

def subtract_from(s):
    return 0

def divide_by(s):
    return 0

def add_(s):
    return 0

def multiply_(s):
    return 0

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






def call_function(s):
    return 0

def call_dot_function(s):
    return 0

def _plus_(s):
    return 0

def _minus_(s):
    return 0

def _times_(s):
    return 0

def _divided_by_(s):
    return 0

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

def _greater_than_(s):
    return 0

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

def _less_than_(s):
    return 0

def _less_than_or_equal_to_(s):
    return 0

def _and_(s):
    return 0

def _or_(s):
    return 0

def _does_not_equal_(s):
    return 0

def _mod_(s):
    return 0

def _to_the_power_of_(s):
    return 0

def _dot_access(s):
    return 0

def _index_(s):
    return 0
wordmap = {
    'define' : {
        'function' : {
            '_' : {
                'of': {
                    '_' : define_function_with_params
                }
            }
        },
        'class' : {
            '_' : define_class
        },
    },
    'for' : {
        '_' : {
            'in' : {
                '_' : for_loop
            }
        }
    },
    'while' : {
        '_' : while_loop
    },
    'let' : {
        '_' : {
            'equal' : {
                '_': let_equal
            }
        }
    },
    'make' : {
        '_' : {
            'a' : {
                'new' : {
                    'list' : make_new_list,
                    'dictionary' : make_new_dictionary
                }
            }
        }
    },
    'list' : {
        '_' : list_object
    },
    'dictionary' : {
        '_' : dictionary_object
    },
    'sum' : {
        'of' : {
            '_' : sum_of
        }
    },
    'product' : {
        'of' : {
            '_' : product_of
        }
    },
    'subtract' : {
        '_' : {
            'from' : {
                '_' : subtract_from
            }
        }
    },
    'divide' : {
        '_' : {
            'by' : {
                '_' : divide_by
            }
        }
    },
    'add' : {
        '_' : add_
    },
    'multiply' : {
        '_' : multiply_
    },
    'if' : {
        '_' : if_
    },
    'call' : {
        '_' : {
            'with' : {
                '_' : call_function
            },
            'dot' : {
                '_' : {
                    'with' : {
                        '_' : call_dot_function
                    }
                }
            }
        }
    },
    '_' : {
        'plus' : {
            '_' : _plus_
        },
        'times' : {
            '_' : _times_
        },
        'minus' : {
            '_' : _minus_
        },
        'divided' : {
            'by' : {
                '_' : _divided_by_
            }
        },
        'equals' : {
            '_' : _equals_
        },
        'greater' : {
            'than' : {
                'or' : {
                    'equal' : {
                        'to' : {
                            '_' : _greater_than_or_equal_to_
                        }
                    }
                },
                '_' : _greater_than_
            }
        },
        'less' : {
            'than' : {
                'or': {
                    'equal' : {
                        'to' : {
                            '_' : _less_than_or_equal_to_
                        }
                    }
                },
                '_' : _less_than_
            }
        },
        'and' : {
            '_' : _and_
        },
        'or' : {
            '_' : _or_
        },
        'does' : {
            'not' : {
                'equal' : {
                    '_' : _does_not_equal_
                }
            }
        },
        'mod' : {
            '_' : _mod_
        },
        'to' : {
            'the' : {
                'power' : {
                    'of' : {
                        '_' : _to_the_power_of_
                    }
                }
            }
        },
        'dot' : {
            '_' : _dot_access
        },
        'index' : {
            '_' : _index_
        }
    }
}


def evaluate(testn):
    test = testn.split(" ")
    for each in list(paths(wordmap)):
        check = True
        index = 0
        for i,key in enumerate(each[0]):
            if key == test[i]:
                index = index + 1
                continue
            elif key == '_' and i < len(each[0]) -1:
                while index <= len(test)-1 and test[index] != each[0][i+1]:
                    index = index + 1
                if index == len(test):
                    check = False
                break
            elif key == '_' and i == len(each[0])-1:
                break
            else:
                check = False
                break
        if check :
            return each[1](testn)
    return txt2num.num_fix(testn)

print evaluate("if x equals two")
print evaluate("define function foo of x y z")
print evaluate("if x greater than or equal to y")
print evaluate("if x greater than or equal to 2")
