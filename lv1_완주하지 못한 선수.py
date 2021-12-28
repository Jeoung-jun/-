from collections import Counter
def solution(participant, completion):
    count = Counter(participant)
    for per in completion:
        count[per]-=1
    return count.most_common()[0][0]