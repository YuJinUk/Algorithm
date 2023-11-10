#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int static asc_compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

int static desc_compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return -1;
    else if (*(int*)first < *(int*)second)
        return 1;
    else
        return 0;
}
int solution(int A[], size_t A_len, int B[], size_t B_len) {
    int answer = 0;
    
    qsort(A, A_len, sizeof(int), asc_compare);
    qsort(B, B_len, sizeof(int), desc_compare);
    
    for (int i=0; i<A_len; i++) {
        answer += A[i] * B[i];
    }
    return answer;
}