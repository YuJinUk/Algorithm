import sys
input = sys.stdin.readline

answer = 0
for _ in range(int(input())) :
    word = input()
    error = 0
    for idx in range(len(word)-1) :
        if word[idx] != word[idx+1] :
            new_word = word[idx+1:]
            if new_word.count(word[idx]) :
                error += 1
    if error == 0:  
        answer += 1
print(answer)