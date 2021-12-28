def solution(new_id):
    ans = new_id.lower()
    answer =''
    for char in ans:
        if char.isalnum() or char in "-_.":
            answer += char
    while '..' in answer:
        answer = answer.replace('..','.')
    if answer[0] == '.':
        answer = answer[1:]
    if answer == '':
        answer = 'a'
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) >= 16:
        answer = answer[0:15]
    if answer[-1] =='.':
        answer = answer[:-1]
    if len(answer) <=2:
        answer = answer[:-1] + (answer[-1] * (4-len(answer)))
    return answer