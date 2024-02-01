#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

bool visit[1001][1001][2]; //x, y 벽 뚫음 여부
int inp[1001][1001]; //inp값저장
int table[1001][1001][2]; //x, y, 벽 뚫었는지 여부
vector<pair <int, int>> a[1001][1001]; //연결 노드를 저장
queue<tuple<int, int, int>> q;

//x, y, 현재까지 벽 뚫음 여부

void bfs() {
    while (!q.empty()) { // queue에 원소가 존재할 경우

        tuple <int, int, int>x = q.front();
        q.pop();
        //printf("bfsing from (%d %d %d) = %d\n", get<0>(x), get<1>(x), get<2>(x), table[get<0>(x)][get<1>(x)][get<2>(x)]);

        for (int i = 0; i < a[get<0>(x)][get<1>(x)].size(); i++) {
            //연결된 노드의 갯수만큼 이 포문이 돈다!
            pair <int, int>y = a[get<0>(x)][get<1>(x)][i];
            //아래는 미방문한 자식 노드의 좌표를 추가하는 코드.

            if ((!visit[y.first][y.second][1]&& visit[get<0>(x)][get<1>(x)][0]) && (inp[y.first][y.second] == 1 && get<2>(x)==0)) {
                table[y.first][y.second][1] = table[get<0>(x)][get<1>(x)][0] + 1;
                q.push(tuple<int, int, int>(y.first, y.second, 1));
                visit[y.first][y.second][1] = true;
            }
            else if (inp[y.first][y.second] == 0){
                if (!visit[y.first][y.second][0] && visit[get<0>(x)][get<1>(x)][0]) {
                    table[y.first][y.second][0] = table[get<0>(x)][get<1>(x)][0] + 1;
                    q.push(tuple<int, int, int>(y.first, y.second,0));
                    visit[y.first][y.second][0] = true;
                }
                if (!visit[y.first][y.second][1] && visit[get<0>(x)][get<1>(x)][1]) {
                    table[y.first][y.second][1] = table[get<0>(x)][get<1>(x)][1] + 1;
                    q.push(tuple<int, int, int>(y.first, y.second, 1));
                    visit[y.first][y.second][1] = true;
                }
            }

        }
    }
}

int main() {
    int n, m; int ret = 0; int zro = 0;
    char temp;
    scanf("%d %d\n", &n, &m);//가로, 세로

    for (int i = 0; i < n; i++) {//가로
        for (int j = 0; j < m; j++) {//세로
            scanf("%c", &temp);
            inp[i][j] = temp - '0';
            table[i][j][0] = 9999999;
            table[i][j][1] = 9999999;
            //만약 -1이 아니라면 ones 큐에 넣기
            if (i > 0) {
                a[i][j].push_back(pair<int, int>(i - 1, j));
                a[i - 1][j].push_back(pair<int, int>(i, j));
            }
            if (j > 0) {
                a[i][j].push_back(pair<int, int>(i, j - 1));
                a[i][j - 1].push_back(pair<int, int>(i, j));
            }
        }
        if (i != n - 1) { scanf("%c", &temp); }
    }

    q.push(tuple<int, int, int>(zro, zro, zro));
    table[0][0][0] = 1;
    visit[0][0][0]=true;
    bfs();

    if (table[n-1][m-1][0] == 9999999 && table[n-1][m-1][1]== 9999999) {
        printf("-1");
    }
    else{
        ret = min(table[n-1][m-1][0], table[n-1][m-1][1]);
        printf("%d", ret);
    }
    return 0;
}