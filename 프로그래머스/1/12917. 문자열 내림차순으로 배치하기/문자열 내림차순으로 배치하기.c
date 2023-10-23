#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * strlen(s));
    int check;
    strcpy(answer, s);
    for (int i = 1; i<strlen(s); i++){
        int j;
        check = answer[i];
        for (j = i; j>0 && answer[j - 1]<check; j--)
            answer[j] = answer[j - 1];
        answer[j] = check;
    }
    return answer;
}