<!--
.. title: POJ 1258 Agri-Net C++版
.. slug: poj-1258
.. date: 2013-04-07T08:50:34+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1258](http://poj.org/problem?id=1258)


标准prim题，无变化，利用简单prim算法解决，先开始WA了一次，后来发现这题，是多数据输入的，修改了个while循环过了！


代码如下：

	:::cpp
	/*Problem: 1258		User: awq123
	**Memory: 300K		Time: 63MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;
	#define MAX 105
	#define INF 0xFFFFF

	int prim(int graph[][MAX], int n)
	{
		int lowcost[MAX],mst[MAX];
		int i, j, min, minid, sum = 0;
		for (i = 2; i <= n; i++)
		{
			lowcost[i] = graph[1][i];
			mst[i] = 1;
		}
		mst[1] = 0;
	 	for (i = 2; i <= n; i++)
		{
			min = INF;
			minid = 0;
	 		for (j = 2; j <= n; j++)
			{
				if (lowcost[j] < min && lowcost[j] != 0)
				{
					min = lowcost[j];
					minid = j;
				}
			}
	 		sum += min;
	 		lowcost[minid] = 0;
			for (j = 2; j <= n; j++)
			{
				if (graph[minid][j] < lowcost[j])
				{
					lowcost[j] = graph[minid][j];
	 				mst[j] = minid;
				}
			}
		}
		return sum;
	}

	int main()
	{
		int i,j,n,map[MAX][MAX];
		while(cin>>n)
		{
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
					cin>>map[i][j];
			cout<<prim(map,n)<<endl;
		}
	}