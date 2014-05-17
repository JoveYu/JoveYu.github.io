<!--
.. title: POJ 1656 Counting Black C++版
.. slug: poj-1656
.. date: 2013-04-07T09:07:09+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1656](http://poj.org/problem?id=1656)


每日一水，今天又是一水题，按照题目给的数据去填涂区域起始点为x，y，长度为l的正方形，最后问给出的区域有多少黑的？

纯模拟，不说了！

	:::cpp
	/*Problem: 1656		User: awq123
	**Memory: 288K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace	std;

	int main()
	{
		int i,j,x,y,l,n,map[105][105];
		char m[7];
		cin>>n;
		memset(map,0,sizeof(map));
		while(cin>>m>>x>>y>>l)
		{
			if(m[0]=='B')
			{
				for(i=x;i<x+l;i++)
					for(j=y;j<y+l;j++)
						map[i][j]=1;
			}
			else if(m[0]=='W')
			{
				for(i=x;i<x+l;i++)
					for(j=y;j<y+l;j++)
						map[i][j]=0;
			}
			else if(m[0]=='T')
			{
				int count=0;
				for(i=x;i<x+l;i++)
					for(j=y;j<y+l;j++)
						if(map[i][j]==1)
							count++;
				cout<<count<<endl;
			}
		}
	}