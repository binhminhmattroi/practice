Daily temperatures: Given a list of daily temperatures, return a list where each entry is how many days you have to wait for a warmer temperature. Use 0 if there is no warmer day ahead.

Example: [70, 73, 72, 75] → [1, 2, 1, 0]

Day 0 (70): the next day is 73, which is warmer, so 1 day.
Day 1 (73): 72 is not warmer, 75 is, so 2 days.
Day 2 (72): 75 is next, so 1 day.
Day 3 (75): nothing is warmer after it, so 0.

First, write the simple version with two loops, and say what its time complexity is. Then I’ll show you how a stack gets it down to O(n).


#temp_list=[}

array=[]
length=len(temp_list)
for i in range(length):
    warmer=False
    for j in range (i+1, length):
        if temp_list[i] <  temp_list[j]:
            array.append(j-i)
            warmer = True
            break
    if not warmer:
        array.append(0)
return array
above is O(n^2)


#to answer with O(n)
n = len(temp_list)
result = [0] * n    # every answer starts at 0
stack = []          # days still waiting

for i in range(0, n):
        while stack and (temp_list[i]>temp_list[stack[-1]):
            day_top_of_stack=stack[-1]
            #result.append(i-day_top_of_stack)
            result[day_top_of_stack]=i-day_top_of_stack
            stack.pop()
        stack.append(i)
#process the last day by add 0 to the list
#result.append(0)  # not needed because result already starts at 0

The pattern to remember is that this is a monotonic stack. Use it when the question is “for each item, find the next bigger or smaller item.” The stack holds the items still waiting for an answer.
