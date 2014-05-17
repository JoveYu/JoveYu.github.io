<!--
.. title: POJ 2105 IP Address C++版
.. slug: poj-2105
.. date: 2013-04-07T07:55:28+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2105](http://poj.org/problem?id=2105)

将2进制的ip地址转换为10进制，每8位取一次，正常转换就是了！

	:::cpp
	/***************************************
	Problem: 2105		User: awq123
	Memory: 248K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int d[8],i,j,t,n;
		char temp;
		cin>>t;
		while(t--)
		{
			for(i=0;i<4;i++)
			{
				n=0;
				for(j=7;j>=0;j--)
				{
					cin>>temp;
					d[i]=temp-'0';
					n+=pow(2.0,j)*d[i];
				}
				if(i==0)
					cout<<n;
				else
					cout<<"."<<n;
			}
			cout<<endl;
		}
	}