#3. Top K frequent items (heap or sort)
#Given a list of ad campaign IDs, return the K most frequent. Input: [a, b, a, c, a, b], K = 2. Output: [a, b] (counts 3 and 2).

#Hint: count with a map, then sort or use a heap. Discuss the time complexity of both.
'''
dictionary={}
for i,value in enumerate (input):
    if value in dictionary:
        dictionary[value] += 1
    else:
        dictonary[value] = 1

sorted_dict = dictionary.sort_by_value_in_descending order

for i in (0:K):
    print dictionary
'''
def top_k_frequent(items, k):
    counts = {}
    for value in items:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return [value for value, count in ranked[:k]]


optional for the last return
result = []
for value, count in ranked[:k]:
    result.append(value)
return result

for pair in ranked[:k]:
    value = pair[0]
    count = pair[1]
