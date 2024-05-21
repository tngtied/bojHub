#include <iostream>
using namespace std;

int main()
{
    int hour, minute;
    cin >> hour >> minute;
    int time;
    cin >> time;
    hour += ((time + minute) - (time + minute) % 60) / 60;
    hour %= 24;
    minute = (time + minute) % 60;
    cout << hour << " " << minute;

    return 0;
}
