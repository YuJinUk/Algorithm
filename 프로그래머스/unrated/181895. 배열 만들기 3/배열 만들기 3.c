#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// intervals_rows는 2차원 배열 intervals의 행 길이, intervals_cols는 2차원 배열 intervals의 열 길이입니다.
int* solution(int arr[], size_t arr_len, int** intervals, size_t intervals_rows, size_t intervals_cols) {
    int left, right;
    int check = 0;
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*(arr_len)*intervals_cols);
    for (int i=0; i<intervals_cols; i++){
        left = intervals[i][0];
        right = intervals[i][1];
        for (int k=0; left < right+1; k++){
            answer[check] = arr[left];
            check++;
            left++;
        }
    }
    return answer;
}