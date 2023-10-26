#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char) * (strlen(s) + 1));
    int j = 0;
    for (int i=0; i<strlen(s); i++) {
        if (s[i] == ' '){
            answer[i] = s[i];
            j = 0;
            continue;
        }
        if (j % 2 == 1) {
            answer[i] = tolower(s[i]);
        } else {
            answer[i] = toupper(s[i]);
        }
        j++;
    }
    answer[strlen(s)] = NULL;
    return answer;
}