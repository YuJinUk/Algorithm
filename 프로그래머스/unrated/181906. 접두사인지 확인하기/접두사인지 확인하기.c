#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* is_prefix) {
    int answer, check = 0;
    int l = strlen(is_prefix);
    for (int i=0; i<l; i++) {
        if (my_string[i] == is_prefix[i]) {
            check++;
        }
    }
    if (check == l) {
        answer = 1;
    } else {
        answer = 0;
    }
    return answer;
}