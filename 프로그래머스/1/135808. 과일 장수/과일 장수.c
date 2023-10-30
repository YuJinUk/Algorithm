#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(int* x, int* y)
{
    if(*x>*y)
        return -1;
    else if(*x == *y)
        return 0;
    else
        return 1;
}
// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;

    qsort(score, score_len, sizeof(int), compare);

    for(int i=m-1; i<score_len;){
        answer += score[i] * m;
        i += m;
    }
    return answer;
}