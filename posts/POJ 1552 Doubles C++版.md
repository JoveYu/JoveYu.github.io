<!--
.. title: POJ 1552 Doubles C++版
.. slug: poj-1552
.. date: 2013-04-07T07:36:57+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1552](http://poj.org/problem?id=1552)


水题，输出一组数中，又两杯关系的数对的个数。没什么好说的！


	:::cpp
	/***************************************
	Problem: 1552		User: awq123
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
		//freopen("input.txt", "r", stdin);
		int d[20],i,j,k,count;
		while(cin>>d[0]&&d;[0]!=-1)
		{
			count=0;
			for(i=1;1;i++)
			{
				cin>>d[i];
				if(d[i]==0)
					break;
			}
			sort(d,d+i);
			for(j=0;j<i;j++)
				for(k=j+1;k<i;k++)
					if(2*d[j]==d[k])
					{
						count++;
						break;
					}
			cout<<count<<endl;
		}
	}
