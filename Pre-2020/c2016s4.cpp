#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define loop(h) for(int i = 0; i<h; i++)

using namespace std;


map <vector <int>, int> maxMem;
map <vector<int>, vector <pair<int, int> > > pMoveMem;



vector <pair <int, int> > findPossibleMoves(vector <int> rbArray){
	auto a = pMoveMem.find(rbArray);
	if (a != pMoveMem.end()){
		return pMoveMem[rbArray];
	}
	
	else{
		vector< pair<int, int> > mList;
		loop(int(rbArray.size()-1)){
			if (rbArray[i] == rbArray[i+1]){
				mList.push_back(pair<int, int>(i, i+1));
				}
			if (i <= int((rbArray.size()-3))){
				if (rbArray[i] == rbArray[i+2]){
					mList.push_back(pair<int, int>(i, i+2));
					}
				}
		pMoveMem[rbArray] = mList;
		}
	}
	return pMoveMem[rbArray];
}

vector <int> applyMove(vector <int> rbArray, pair<int, int> move){
	if ((move.second - move.first) == 1){
		rbArray[move.first] = rbArray[move.first] + rbArray[move.second];
	}
	
	else if ((move.second - move.first) == 2){
		rbArray[move.first] = rbArray[move.first] + rbArray[move.second] + rbArray[move.first+1];
	}
	
	return rbArray;
}

void findLargestRiceBall(vector <int> rbArray, int &maxN){
	auto a = maxMem.find(rbArray);
	
	if (a != maxMem.end()){
		maxN = maxMem[rbArray];
		return;
	}
	
	else if (findPossibleMoves(rbArray).size() == 0){
		maxMem[rbArray] = *max_element(rbArray.begin(), rbArray.end());
		if (maxMem[rbArray] > maxN){
			maxN = maxMem[rbArray];
		return;
		}
	}
	
	else{
		auto mList = findPossibleMoves(rbArray);
		for (const auto &move: mList){
			findLargestRiceBall(applyMove(rbArray, move), maxN);
		}
	}
	
}



void disp(vector<int> v){
	loop(int(v.size())){
		cout<<v[i]<<" ";
	}
	cout<<endl;
}

void disp( map <vector <int> , int> m){
	for (auto a = m.begin(); a != m.end(); a++){
		disp(a->first);
		cout<<" value: "<<a->second<<endl;
	}
}


int main(){
	int n;
	cin>>n;
	
	vector <int> riceBalls;
	int temp;
	loop(n){
		cin>>temp;
		riceBalls.push_back(temp);
	}
	
	int maxN = -1;
	findLargestRiceBall(riceBalls, maxN);
	
	disp(maxMem);
	
}
