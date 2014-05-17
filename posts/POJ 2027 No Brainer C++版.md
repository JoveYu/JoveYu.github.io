<!--
.. title: POJ 2027 No Brainer C++版
.. slug: poj-2027
.. date: 2013-04-07T07:38:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2027](http://poj.org/problem?id=2027)


植物大战僵尸，这个题水的太离谱了！


	:::cpp
	/***************************************
	Problem: 2027		User: awq123
	Memory: 240K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t,m,n;
		cin>>t;
		while (t--)
		{
			cin>>m>>n;
			if(m>=n)
				cout<<"MMM BRAINS"<<endl;
			else
				cout<<"NO BRAINS"<<endl;
		}

	}
