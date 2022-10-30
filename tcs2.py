Karan
Ryat
Project, [05 - 03 - 2022 12: 02]
# include <bits/stdc++.h>
using
namespace
std;

int
main()
{
    int
n, p;
cin >> n;
vector < int > v(n);
for (int i=1;i <= n;i++)
{
    cin >> v[i];
}
cin >> p;
vector < int > ans;
vector < pair < int, int > > arr(p);
for (int i=0;i < p;i++)
{
    int
x;
cin >> x;
int
y;
cin >> y;
arr[i].first = x;
arr[i].second = y;
}
sort(arr.begin(), arr.end());

int
i = 0, j = 1, sum = 0, maxin = INT_MIN;
for (i=0;i < p-1 & & j < p;i++)
{
    sum = 0;
maxin = INT_MIN;
j = i + 1;
set < int > s;
if (arr[i].first == arr[j].first)
{
    s.insert(arr[i].first);
s.insert(arr[i].second);
s.insert(arr[j].first);
s.insert(arr[j].second);
}
else if (arr[i].second == arr[j].first | | arr[i].second == arr[j].second)
{

s.insert(arr[i].first);
s.insert(arr[i].second);
s.insert(arr[j].first);
s.insert(arr[j].second);

}

set < int >::
    iterator
itr;
// adding
set
elements
for (itr = s.begin(); itr != s.end(); itr++)
{
sum += v[* itr];
s.erase(itr);
}
maxin=max(sum, maxin);
ans.push_back(maxin);

}
sort(ans.begin(), ans.end());
cout << ans[ans.size()-1];
return 0;
}

Karan
Ryat
Project, [05 - 03 - 2022 14: 12]
# include <bits/stdc++.h>
using
namespace
std;

int
main()
{
int
n;
cin >> n;
vector < pair < pair < int, int >, int >> v(n);
for (int i=0;i < n;i++)
    {
        int
    x, y, z;
    cin >> z >> x >> y;
    v[i].first.first = x;
    v[i].first.second = x + y;
    v[i].second = z;
    }
    int
    x;
    cin >> x;
    sort(v.begin(), v.end());
    int
    ptf = 1;
    deque < pair < pair < int, int >, int >> dq;
    dq.push_back({{ptf, v[0].first.second}, v[0].second});

    for (int i=1;i < n;i++)
        {
        // cout << v[i].second << " " << v[i].first.first << "--" << v[i].first.second << endl;
        if (v[i].first.first <= v[i - 1].first.second)
        {

        if (v[i-1].first.second >= v[i].first.second )
        {
        if (dq.front().first.second < v[i].first.second)
        {
        ptf=dq.front().first.first;
        dq.push_front({{ptf, v[i].first.second}, v[i].second});
        }
        else
        {
        ptf++;
        dq.push_back({{ptf, v[i].first.second}, v[i].second});
        }
        }
        else
        {
        dq.push_back({{ptf, v[i].first.second}, v[i].second});
        }
        }
        else
        {
        ptf=dq.back().first.first;
        dq.push_back({{ptf, v[i].first.second}, v[i].second});
        }
        }
    while (x != dq.front().second)
        {
            dq.pop_front();
        }
        cout << dq.front().first.first + 1;
        return 0;
        }
# import numpy as np
#
# N=int(input("Enter no. of Trains : "))
#
# list1=[]
#
# for i in range (0,N):
#     T=int(input("Train No. : "))
#     A=int(input("Arrival Time : "))
#     I=int(input("Stoppage Interval : "))
#     L=A+I
#     list=[T,A,L]
#     list1.append(list)
#
# # F=int(input("Enter Required Train : "))
#
# def MinValue():
#     min_value = np.min(list1)
#     return min_value
#
# print(MinValue())

