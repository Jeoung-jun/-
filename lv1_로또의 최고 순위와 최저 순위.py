def solution(lottos, win_nums):
    base = 0
    for num in lottos:
        if num in win_nums:
            base += 1
    case = lottos.count(0)
    high = 6-(base + case) + 1
    low = 6-base + 1
    if high >6:
        high = 6
    if low>6:
        low = 6
    answer = [high,low]
    return answer
    