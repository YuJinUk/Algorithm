#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

int solution(int k, vector<int> tan) {
    int answer = 0;
    set<int> checkset;
    priority_queue<int, vector<int>, less<int>> pq;
    for (int i=0; i<tan.size(); i++){
        checkset.insert(tan[i]);
    }
    for (auto iter = checkset.begin(); iter !=checkset.end(); ++iter){
        pq.push(count(tan.begin(), tan.end(), *iter));
    }
    while (!pq.empty()){
        k -= pq.top();
        if (k>0){
            answer++;
        }else{
            answer++;
            return answer;
        }
        pq.pop();
    }
    return answer;
}