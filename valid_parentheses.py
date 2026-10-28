#input = "()[]{}"

#find the midpoint of the array
size=len(input)
#push the top onto the array
array1=[]
for i in range(0,size/2):
    array1.push(input[i]
#push the other end onto another array
array2=[]
for i in range(1,size/2)
    array2.push(input[i*-1])
#compare the two array
if array1 == array2:
    return true
else:
    return false

The above won't work because Your approach only handles strings that mirror around the middle. Trace "()[]{}" (size 6): and Also, ( and ) are never equal, so comparing characters directly can’t work even for "([])". You’d have to check that each ( pairs with a ).


Here’s one on stacks, to go with the dictionary questions you’ve done.

Valid parentheses: Write a function is_valid(s) that returns True if every bracket in the string is closed in the right order, and False otherwise. The brackets are (), [] and {}.

Examples:

"()[]{}" → True
"([])" → True
"(]" → False
"([)]" → False
"((" → False

Try it yourself first, then paste your code. If you get stuck, tell me what you’re thinking and I’ll give a hint without giving away the answer.

One thing to think about first: in "([)]", when you reach the ), which bracket should you have most recently opened?

def is_valid(input):
    array=[]
    for item in input:
        if (item == "(" or item == "[" or item == "{"):
            array.append(item)
        elif (item == ")"): 
            if (array) and  (array[-1] == "("):
                array.pop("(")
            else:
                return False
        elif (item == "]"):
            if (array) and (array[-1] == "["):
                array.pop("[")
            else:
                return False
        elif (item == "}"):
            if (array) and (array[-1] == "{"):
                array.pop("{")
            else
                return False
        else:
            continue

    if (len(array)==0):
        return True
    else:
        return False
