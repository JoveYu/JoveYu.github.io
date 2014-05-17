<!--
.. title: POJ 1979 Red and Black C++版
.. slug: poj-1979
.. date: 2013-04-07T08:07:11+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1979](http://poj.org/problem?id=1979)


简单解释下题意，包括@在内，与其连通的.有多少个！

简单DFS，每次标记一个点已经使用，再四方向深搜，每发现一个，计数t++，这样最后t+1，就是答案，因为@算一个所以要加1.

其中注意判断点的条件，不仅要没使用过，还要在矩阵内！



代码如下：

	:::cpp
	/***************************************
	Problem: 1979		User: awq123
	Memory: 256K		Time: 47MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	char d[25][25];
	int h,w,t,used[25][25],dir[8]={0,1,1,0,0,-1,-1,0};

	bool check(int m,int n)
	{
		if(m>=0&&m;<h&&n;>=0&&n;<w)
			return true;
		return false;
	}

	void dfs(int y,int x)
	{
		for(int i=0;i<8;i+=2)
		{
			int m=y+dir[i];
			int n=x+dir[i+1];
			if(used[m][n]==0&&check;(m,n))
			{
				t++;
				used[m][n]=1;
				dfs(m,n);
			}
		}
		return;
	}
	int main()
	{
		int startx,starty;
		while(cin>>w>>h&&w;+h)
		{
			t=0;
			memset(used,0,sizeof(used));
			for(int i=0;i<h;i++)
				for(int j=0;j<w;j++)
				{
					cin>>d[i][j];
					if(d[i][j]=='@')
					{
						startx=j;
						starty=i;
					}
					if(d[i][j]=='#')
						used[i][j]=1;
				}
				used[starty][startx]=1;
			dfs(starty,startx);
			cout<<t+1<<endl;
		}
	}
