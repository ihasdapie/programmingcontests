#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

#define loop(h) for(int i = 0; i < h; i++)


void disp(vector <pair< int, int> > v);

int main(){
    string screen;
    getline(cin, screen);

    string cs = screen.substr(0, screen.find(" "));
    string rs = screen.substr(screen.find(" "), screen.size());

    int c = stoi(cs, nullptr, 10);
    int r = stoi(rs, nullptr, 10);


    vector < pair< int, int> > moves;
    while (true){
        string input;
        getline(cin, input);
        if (input.empty() == false){
            pair <int, int> temp;
            temp.first = stoi(input.substr(0, input.find(" ")));
            temp.second = stoi(input.substr(input.find(" "), input.size()));
            moves.push_back(temp);
        }
        else{
            break;
        }
    }
    int mx = 0;
    int my = 0;

    loop(int(moves.size())){
        if ((moves[i].first == 0) && (moves[i].second == 0)){
            break;
        }
        else{
            if (((mx + moves[i].first) <= c) && ((mx + moves[i].first) >= 0)) {
                mx += moves[i].first;
            }

            else if ((mx + moves[i].first) < 0){
                mx = 0;
            }

            else if ((mx + moves[i].first) > c){
                mx = c;
            }

            if (((my + moves[i].second) <= r) && (((my + moves[i].second) >= 0))){
                my += moves[i].second;
            }

            else if ((my + moves[i].second) < 0){
                my = 0;
            }

            else if ((my + moves[i].second) > r){
                my = c;
            }
        printf("%d %d\n", mx, my);
        }
    }
}
void disp(vector< pair< int, int> > v){
    loop(int(v.size())){
        printf("%d %d\n", v[i].first, v[i].second);
    }

}
