#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long n) {
    long long answer = 0;
    double x = sqrt(n); // double 형을 사용하여 실수 값을 저장

    if (n == (long long)(x + 0.5) * (long long)(x + 0.5)) {
        // x를 반올림한 값의 제곱이 n과 같다면
        answer = (long long)(x + 1.5) * (long long)(x + 1.5);
    } else {
        answer = -1;
    }

    return answer;
}