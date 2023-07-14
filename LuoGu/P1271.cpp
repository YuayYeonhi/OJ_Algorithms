#include<iostream>
using namespace std;
int main()
{
    int n;cin>>n;
    int m;cin >> m;

    int* a = new int[m];
    for (int i = 0; i < m; i++)
    {
        cin >> a[i];
    }

    for (int j = 0; j < m - 1; j++)
    {
        for (int i = 0; i < m - 1; i++)
            {
                if (a[i] > a[i + 1])
                {
                    int tmp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = tmp;
                }
            }
    }
    for (int i = 0; i < m; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}