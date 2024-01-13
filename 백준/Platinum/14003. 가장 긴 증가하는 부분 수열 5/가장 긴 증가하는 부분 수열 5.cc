#include <iostream>
#include <vector>

using namespace std;
vector <int> table;
vector<pair<int, int>> dex;
int n;

int lb(int a) {
    int left = 1; int right = table.size()-1; int mid;
    //int bound = -1;
    while (left < right) {
        mid = (left + right) / 2;
        if (table[mid] >= a) { 
            //bound = mid;
            right= mid; }
        else { left = mid + 1; }
    }
    return right;
}
void out(int s) {
    vector <int> print_v;
    int dexnow = s-1;
    //cout << "with dexnow " << dexnow << endl;
    for (int i = n - 1; i >= 0; i--) {
        //cout << "  - checking " << dex.back().first << ", " << dex.back().second << endl;
        if (dex.back().first == dexnow) { 
            print_v.push_back(dex.back().second);
            dexnow --;
            //cout << "with dexnow " << dexnow << endl;
        }
        if (dexnow == 0) { break; }
        dex.pop_back();
    }
    for (int i = 0; i < s - 1; i++) {
        cout << print_v.back() << " ";
        print_v.pop_back();
    }


}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    
    int inp; int count = 1;
    cin >> n;
    table.push_back(-1000000001);
    for (int i = 0; i < n; i++) {
        cin >> inp;
        if (table.back() < inp) {
            dex.push_back(make_pair(count, inp));
            table.push_back(inp);
            count += 1;
        }
        else {
            int pt= lb(inp);
            //cout << "changing to " << i << ", " << inp << " at " << pt << "\n";
            dex.push_back(make_pair(pt,inp));
            table[pt]= inp;
        }
    }
    cout << count-1<<"\n";
    out(count);
    return 0;
}