#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int solution(vector<int> elements) {
    set<int> Set;

    int n = elements.size();

    for (int i = 0 ; i < n ; ++i) {
        int sum = 0;
        for (int j = i ; j < i + n ; ++j) {
            sum += elements[j % n];
            // cout << elements[j % n] << endl;
            Set.insert(sum);
        }
        // cout << "----------" << endl;
    }

    return Set.size();
}