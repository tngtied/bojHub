#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    list<int> nums;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        nums.push_back(temp);
    }
    cout << *min_element(nums.begin(), nums.end()) << " " << *max_element(nums.begin(), nums.end());

    return 0;
}
