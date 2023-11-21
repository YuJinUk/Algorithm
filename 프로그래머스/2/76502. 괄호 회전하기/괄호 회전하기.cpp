#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    int n = s.size();
    vector<char> check = {};
    int val = 0;
    if (n % 2 == 1){
        return 0;
    }
    for (int i=0; i<n; i++){
        val = 0;
        check = {};
        for (int j=i; j< i+n; j++){
            if (check.empty()){
                check.push_back(s[j%n]);
            } else {
                if (check[check.size()-1] == '{' && s[j%n] == '}'){
                    check.pop_back();
                    val++;
                } else if(check[check.size()-1] == '[' && s[j%n] == ']'){
                    check.pop_back();
                    val++;
                } else if(check[check.size()-1] == '(' && s[j%n] == ')'){
                    check.pop_back();
                    val++;
                } else {
                    check.push_back(s[j%n]);
                }
            }
        }
        if (val == n/2) {
            answer++;
        }
    }
    return answer;
}