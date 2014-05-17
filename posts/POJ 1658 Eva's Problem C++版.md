<!--
.. title: POJ 1658 Eva's Problem C++版
.. slug: poj-1658
.. date: 2013-04-07T07:53:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1658](http://poj.org/problem?id=1658)


最近光做水题！


	:::cpp
	/***************************************
	Problem: 1658		User: awq123
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
		int d[5],i,t;
		cin>>t;
		while(t--)
		{
			for(i=0;i<4;i++)
				cin>>d[i];
			if(d[1]-d[0]==d[2]-d[1]&&d;[2]-d[1]==d[3]-d[2])
				d[4]=d[3]+d[3]-d[2];
			if(d[1]/d[0]==d[2]/d[1]&&d;[2]/d[1]==d[3]/d[2])
				d[4]=d[3]*d[3]/d[2];
			for(i=0;i<5;i++)
				cout<<d[i]<<" ";
			cout<<endl;
		}

	}