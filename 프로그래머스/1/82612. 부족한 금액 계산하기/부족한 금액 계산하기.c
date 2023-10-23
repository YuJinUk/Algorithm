#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long price, long long money, long long count) {
    long long answer = 0;
    long long result = price * count * (count + 1) / 2;
    if (money < result){
        return result - money;
    }
    return 0;
}