#include <iostream>
#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(int n) {
    for (int i=1; i<n; i++){
        if (n % i == 1) {
            return i;
        }
    }
}