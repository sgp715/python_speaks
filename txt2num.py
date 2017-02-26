def txt2num(textnum, numwords={}):
   if not numwords:
     units = [
       "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
       "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
       "sixteen", "seventeen", "eighteen", "nineteen"
     ]

     tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
      "eighty", "ninety"]

     scales = ["hundred", "thousand", "million", "billion", "trillion"]

     for idx, word in enumerate(units):    numwords[word] = (1, idx)
     for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
     for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

   current = result = 0
   for word in textnum.split():
       if word not in numwords:
         raise Exception("Illegal word: " + word)

       scale, increment = numwords[word]
       current = current * scale + increment
       if scale > 100:
           result += current
           current = 0

   return str(result + current)

def num_fix(str):
    words= str.split()
    output=""
    lit_string = ""

    A = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",]

    B=["twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty", "ninety"]

    C=["hundred", "thousand","million", "billion", "trillion"]

    D = A + B + C

    for w in range(len(words)):
        if words[w] in D:
            lit_string += words[w] + " "
            if w == len(words) - 1:
                output+= txt2num(lit_string) + " "
            else:
                continue

        if words[w] not in D:
            if lit_string != "":
                output += txt2num(lit_string) + " " + words[w] + " "
            else:
                output += words[w] + " "
            lit_string = ""

    return output
