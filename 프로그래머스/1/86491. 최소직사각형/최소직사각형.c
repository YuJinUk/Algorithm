#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// sizes_rows는 2차원 배열 sizes의 행 길이, sizes_cols는 2차원 배열 sizes의 열 길이입니다.
int solution(int** sizes, size_t sizes_rows, size_t sizes_cols) {
    int answer = 0;
    int maxx = -1;
    int minn = -1;
    int check_max, check_min;
    for (int i=0; i<sizes_rows; i++) {
        check_max = 0;
        check_min = 0;
        if (sizes[i][0] < sizes[i][1]) {
            check_max = sizes[i][1];
            check_min = sizes[i][0];
        } else {
            check_min = sizes[i][1];
            check_max = sizes[i][0];
        }
        if (maxx < check_max) {
            maxx = check_max;
        }
        if (minn < check_min) {
            minn = check_min;
        }
    }
    answer = maxx * minn;
    
    return answer;
}