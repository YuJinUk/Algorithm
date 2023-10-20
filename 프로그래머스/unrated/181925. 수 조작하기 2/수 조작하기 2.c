#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numLog_len은 배열 numLog의 길이입니다.
char* solution(int numLog[], size_t numLog_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int signal01, signal02, check;
    char* answer = (char*)malloc(sizeof(char)*numLog_len);
    for (int i=1; i<numLog_len; i++){
        signal01 = numLog[i-1];
        signal02 = numLog[i];
        check = signal02 - signal01;
        if (check == 1){
            answer[i-1] = 'w';
        } else if (check == -1) {
            answer[i-1] = 's';
        } else if (check == 10) {
            answer[i-1] = 'd';
        } else if (check == -10) {
            answer[i-1] = 'a';
        }
    }
    answer[numLog_len-1] = NULL;
    return answer;
}