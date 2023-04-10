#include <string>
#include <vector>

using namespace std;
int maxPlus = 0;
int maxCost = 0;

void funct(vector<int> sale, vector<vector<int>> users, vector<int> emoticons);
void sales(vector<int> sale, vector<vector<int>> users, vector<int> emoticons);
vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> sale;
    sales(sale, users, emoticons);
    
    vector<int> answer;
    answer.push_back(maxPlus);
    answer.push_back(maxCost);
    
    return answer;
}

void funct(vector<int> sale, vector<vector<int>> users, vector<int> emoticons){
    int emotPlus = 0;
    int total = 0;
    
    for(int i=0; i<users.size(); i++){
        int s = 0;
        for(int j=0; j<sale.size(); j++){
            if(users[i][0] > sale[j]){
                continue;
            }
            s += (emoticons[j] / 100) * (100 - sale[j]);
        }
        if(s >= users[i][1]){
            emotPlus++;
        }
        else{
            total += s;
        }
    }
    if(maxPlus > emotPlus){
        return;
    }
    else if(maxPlus == emotPlus && maxCost > total){
        return;
    }
    
    maxCost = total;
    maxPlus = emotPlus;
}
void sales(vector<int> sale, vector<vector<int>> users, vector<int> emoticons){
    if (sale.size() == emoticons.size()){
        funct(sale, users, emoticons);
        return;
    }
    
    for (int i=10; i<=40; i+=10){
        sale.push_back(i);
        sales(sale, users, emoticons);
        sale.pop_back();
    }
}