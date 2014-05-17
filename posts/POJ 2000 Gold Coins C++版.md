<!--
.. title: POJ 2000 Gold Coins C++版
.. slug: poj-2000
.. date: 2013-04-07T07:54:08+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2000](http://poj.org/problem?id=2000)

先开始一天，每天1枚硬币，后两天每天两枚，后三天每天三枚，不难，处理好收尾的几天就是了


代码如下：

	:::cpp
	/***************************************
	Problem: 2000		User: awq123
	Memory: 248K		Time: 16MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,m,i,sum;
		while(cin>>n&&n;)
		{
			sum=0;
			m=0;
			for(i=1;sum<=n;i++)
			{
				m+=i*i;
				sum+=i;
			}
			m-=(sum-n)*(i-1);
			cout<<n<<" "<<m<<endl;
		}

	}