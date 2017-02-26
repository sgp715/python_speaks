
def evaluate(s):
    """Evaluates speech to text string into python code
    Input: String"""
    words = s.split(" ")
    for i, word in enumerate(words):
        return 0





def check_bucket(s):
    """Determines what bucket the string falls into
    Input: String
    Ouput: String"""
    words = string.split(" ")

def define_function_with_params(s):
    return 0

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
    return 0

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
     return 0

def _greater_than_(s):
    return 0

def _greater_than_or_equal_to_(s):
    return 0

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

test = "if one plus one equals two"

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
                '-' : _less_than_
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

print evaluate(test)
