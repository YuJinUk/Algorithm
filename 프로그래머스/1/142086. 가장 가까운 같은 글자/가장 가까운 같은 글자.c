#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * strlen(s));
    int t;
    for (int i=0; i<strlen(s); i++) {
        t = -1;
        if (!i) {
            answer[i] = -1;
            continue;
        }
        for (int j=0; j<i; j++) {
            if (s[j] == s[i]) {
                t = j;
                
            }
        }
        if (t == -1) {
            answer[i] = t;            
        } else {
            answer[i] = i - t;
        }

    }
    return answer;
}