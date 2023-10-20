#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start, int end) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*(start-end+1));
    for(int i=0; i<start-end+1; i++)
        answer[i] = start-i;
    return answer;
}