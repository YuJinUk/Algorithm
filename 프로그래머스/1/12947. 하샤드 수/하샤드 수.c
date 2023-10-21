#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int summ = 0, check = x;
    while (check > 0){
        summ += check % 10;
        check /= 10;
    }
    if (x % summ != 0){
        answer = false;
    }
    return answer;
}