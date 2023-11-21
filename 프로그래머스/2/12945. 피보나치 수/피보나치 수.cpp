#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    vector<int> fib = {0, 1};
    for (int i=0; i<n-1; i++){
        int l = fib.size();
        fib.push_back((fib[l-1] + fib[l-2])%1234567);
    }
    return fib[fib.size()-1]%1234567;
}