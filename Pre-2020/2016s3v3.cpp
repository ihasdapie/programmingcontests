#include <iostream>
#include <vector>
#include <algorithm>
//~ #include <cmath>
//~ #include <queue>
//~ #include <set>
#include <map>



using namespace std;

#define loop(h) for(int i = 0; i<h; i++)
#define pb push_back
#define INF 2147483647;
#define LINF 9223372036854775807;
//#define rest pair<int, vector<int> >

struct rest{
	int restN;
	bool isPho;
	vector <int> connected;
};

//~ vector< vector<int>> paths;

void disp(rest r);
void createV_InducedSubGraph(map <int, rest> &Rs, int currR, vector<bool> &visited, vector <int> &toErase){
	if (visited[currR] == true){
		return;
	}
	else{
		if (Rs[currR].connected.size() == 1){
			if(Rs[currR].isPho == false){
				toErase.pb(currR);
			}
		}
	}

	visited[currR] = true;
	loop(int(Rs[currR].connected.size())){
		createV_InducedSubGraph(Rs, Rs[currR].connected[i], visited, toErase);
	}
	
}



void checkOnlyPhoLeaf(map <int, rest> &r, int currR, vector<bool> &visited, bool &onlyPho){
	if (visited[currR] == true){
		return;
	}
	else{
		if (r[currR].connected.size() == 1){
			if (r[currR].isPho == false){
				onlyPho = false;
				return;
			}
		}
	}
	visited[currR] = true;
	loop(int(r[currR].connected.size())){
		checkOnlyPhoLeaf(r, r[currR].connected[i], visited, onlyPho); 
	}
}


void disp(vector <int> v){
	for (unsigned int i = 0; i<v.size(); i++){
		cout<<v[i]<<", ";
	}
	cout<<endl;
}

void disp(rest r){
	cout<<"restN: "<<r.restN<<" isPho: "<<r.isPho<<" connected: ";
	disp(r.connected);
}

void disp(vector <rest> r){
	loop(int(r.size())){
		int current = i;
		disp(r[current]);
	}
}

bool isleaf(map <int, rest> &tree, int leaf){
	if (tree[leaf].connected.size() == 1){
		return true;
	}
	else{
		return false;
	}
}

void disp(map <int, rest> m){
	map <int, rest>::iterator i;
	for (i = m.begin(); i != m.end(); i++){
		cout<<"key: "<<i->first<<" ";
		disp(i->second);
		cout<<endl;
	}
}


void dfs(map <int, rest> &tree, int sLeaf, vector <bool> &check, int &max, int &fNode, int count);

//global var


int main(){

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, M, temp;
	cin>>N>>M;
	vector <rest> rvec(N);
	map <int, rest> restS;

	loop(M){
		cin>>temp;
		rvec[temp].isPho = true;
		rvec[temp].restN = temp;
	}
	
	//all rests are now created, now just need to connect them together
	//(a, b) -> a to b, b to a
	
	loop(N){rvec[i].restN=i;};
	
	loop(N-1){
		int ta, tb;
		cin>>ta>>tb;
		rvec[ta].connected.pb(tb);
		rvec[tb].connected.pb(ta);
	}
	
	//turn the vector into a map:
	loop(N){
		restS.insert(pair<int, rest>(rvec[i].restN, rvec[i]));
	}
	
	rvec.clear();
	
	vector <bool> check(N, false);
	vector <int> toErase;
	bool done = false;
	int t = N;


	while (done == false){
		
		check.assign(t, false);
		done = false;
		
		createV_InducedSubGraph(restS, restS.begin()->first, check, toErase);


		//remove from roads
		for (auto mi = restS.begin(); mi != restS.end(); mi++){
			int rn = mi->first;
			rest r = mi->second;
			loop(int(toErase.size())){
				int te = i;
				auto ind = r.connected.begin(), r.connected.end(), toErase[te]);
				if (ind == r.connected.end()){
					continue;
				}
				else{
					//~ disp(restS[rn].connected);
					restS[rn].connected.erase(remove(restS[rn].connected.begin(), restS[rn].connected.end(), toErase[te]), restS[rn].connected.end());
					//~ disp(restS[rn].connected);			
				}
			}
		}
		//remove from map
		loop(int(toErase.size())){restS.erase(toErase[i]);};
		//check if all leaves are pho. if not, go again

		check.assign(t, false);
		done = true;
		checkOnlyPhoLeaf(restS, restS.begin()->first, check, done);
		
		toErase.clear();
		
		//clear out the crap
	}
	

		
	check.assign((N-int(toErase.size())), false);
	
	

	
	int longestDistance = -1;
	int fn1 = -1;
	int fn2 = -1;
	int sLeaf = -1;
	//must start from a leaf node
	for (auto i = restS.begin(); i != restS.end(); i++){
		if (isleaf(restS,i->first) == true){
			sLeaf = i->first;
		}
	}
	
	// num_edges*2 - longestDistance -> ans!
	dfs(restS, sLeaf, check, longestDistance, fn1, -1);
	
	
	fn2 = fn1;
	check.assign(N, false);
	dfs(restS, fn1, check, longestDistance, fn2, -1);
	
	int ans = (restS.size()-1)*2 - longestDistance;	
	cout<<ans<<endl;
	//~ disp(restS);
	return 0;		
}




void dfs(map <int, rest> &tree, int sLeaf, vector <bool> &check, int &max, int &fNode, int count){
	check[sLeaf] = true;
	count++;
	if (count>max){
		max = count;
		fNode = sLeaf;
	}
	loop(int(tree[sLeaf].connected.size())){
		
		int ind = i;
		if (check[tree[sLeaf].connected[ind]] == false){
			dfs(tree, tree[sLeaf].connected[ind], check, max, fNode, count);
		}
	}
}


