'''
Given a list of log lines like "2026-10-22 ERROR payments timeout", return how many ERROR lines each service has.

Input: ["... ERROR payments ...", "... INFO orders ...", "... ERROR payments ..."]. Output: {payments: 2}.
It’s close to your logging work, so a natural warm-up for the real interview.
'''

line_list = ["", "", ""]
for line in line_list:
    print (line)
    if ERROR in line:
        #use regex to grab the next word
        word = r'[*ERROR [\w]*]
        ###should be r"ERROR (\w+)".group(1)
        list[word]+=1

for word, count in enumerate (list):
    print ("{"+word: count+"}")


def count_errors(lines):
    counts = {}                          # service -> number of ERROR lines
    for line in lines:
        parts = line.split()             # ["2026-10-22", "ERROR", "payments", "timeout"]
        if len(parts) >= 3 and parts[1] == "ERROR":
            service = parts[2]
            counts[service] = counts.get(service, 0) + 1
    return counts

