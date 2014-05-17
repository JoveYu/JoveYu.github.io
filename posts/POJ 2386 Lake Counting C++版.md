<!--
.. title: POJ 2386 Lake Counting C++版
.. slug: poj-2386
.. date: 2013-04-07T08:12:21+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2386](http://poj.org/problem?id=2386)


题目问，一共有几块池塘，8方向相连就算一块！

简单DFS，我用used数组记录每一块，若发现新的一块就编号，然后从这个点开始8方向深搜，有相连还没编号的一起编上号，看左后一共编了几个号！



代码如下：

	:::cpp
	/*Problem: 2386		User: awq123
	**Memory: 568K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int n,m,used[105][105],dir[16]={1,0,1,1,0,1,-1,1,-1,0,-1,-1,0,-1,1,-1};
	char map[105][105];

	void dfs(int i,int j)
	{
		for(int k=0;k<16;k+=2)
		{
			int p=i+dir[k];
			int q=j+dir[k+1];
			if(0<=p&&p;<n&&0<=q&&q;<m)//不出界
			{
				if(map[p][q]=='W'&&used;[p][q]==0)//若没编号
				{
					used[p][q]=used[i][j];
					dfs(p,q);//由新的点开始继续深搜
				}
			}
		}
	}

	int main()
	{
		int i,j,t;
		t=1;
		memset(used,0,sizeof(used));
		memset(map,'.',sizeof(map));
		cin>>n>>m;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				cin>>map[i][j];
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				if(map[i][j]=='W'&&used;[i][j]==0)
				{
					used[i][j]=t++;//若发现没编号的
					dfs(i,j);
				}
			}
		cout<<t-1<<endl;
	}