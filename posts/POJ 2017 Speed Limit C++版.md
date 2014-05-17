<!--
.. title: POJ 2017 Speed Limit C++版
.. slug: poj-2017
.. date: 2013-04-07T07:54:08+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2017](http://poj.org/problem?id=2017)


给出每段时间的速度，求出长度，分段计算就是了

	:::cpp
	/***************************************
	Problem: 2017		User: awq123
	Memory: 248K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,i,d[11][2],sum;
		while(cin>>n&&n;!=-1)
		{
			d[0][1]=0;
			sum=0;
			for(i=1;i<=n;i++)
			{
				cin>>d[i][0]>>d[i][1];
				sum+=d[i][0]*(d[i][1]-d[i-1][1]);
			}
			cout<<sum<<" miles"<<endl;

		}

	}
