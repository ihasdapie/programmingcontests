#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cstring>
#include <bits/stdc++.h> 

#define loop(h) for(int i = 0; i < h; i++)

using namespace std;
bool sameAdjacent(string s){
	set <char> t;
	int n = s.size();
	t.insert(s[0]);
	for (int i = 1; i<n; i++){
		if (s[i] == s[i-1]){
			continue;
		}
		if (t.find(s[i]) != t.end()){
			return false;
		}
		
		t.insert(s[i]);
	}
	return true;
}



int minL(string s, int a, int b, int cnt, int minm) 
{ 
   // Base case  
   if (a == b) { 
        if (sameAdjacent(s)) 
            return cnt; 
        else
            return INT_MAX; 
    } 
     
    for (int i = a + 1; i <= b; i++) { 
        swap(s[i], s[a]); 
        cnt++; 
  
        // considering swapping of i and l chars  
        int x = minL(s, a + 1, b, cnt, minm);  
  
        // Backtrack 
        swap(s[i], s[a]); 
        cnt--; 
  
        // not considering swapping of i and l chars 
        int y = minL(s, a + 1, b, cnt, minm); 
  
        // taking min of above two  
        minm = min(minm, min(x, y));  
    } 
  
    return minm; 
} 






int main(){
	string s;
	cin>>s;

    int n = s.length(), count = 0, minm = INT_MAX; 
	cout<<minL(s, 0, n-1, count, minm)<<endl;
	return 0;
}	
