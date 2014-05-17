<!--
.. title: POJ 1953 World Cup Noise C++版
.. slug: poj-1953
.. date: 2013-04-07T08:05:44+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1953](http://poj.org/problem?id=1953)

一列数，每位只能是0和1，问使1不连续的序列有多少种？

最先开始的思路是递归，可是递归的败病就在这里，递归层数过多，处理长数据会超时，但是思路应该是没问题了！来看看代码把！

<!--more-->

代码如下：

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <iomanip>
	using namespace std;

	int ct,n,d[50];

	void dp(int k,int i)
	{
		if(k==n-1)
		{
			ct++;
			return;
		}
		d[k]=i;
		if(d[k]==0)
			dp(k+1,1);
		dp(k+1,0);
	}

	int main()
	{
		int t;
		cin>>t;
		for(int i=1;i<=t;i++)
		{
			ct=0;
			cin>>n;
			dp(0,0);
			dp(0,1);
			cout<<"Scenario #"<<i<<":"<<endl<<ct<<endl<<endl;
		}
	}


一看超时我就知道这个没得改，换思路，改用DP，用数组保存d[n][i]n个数当这个数为i的所有情况，我们可以看到，如果这个数为1前一位数一定是0，如果这一位是0，前面一位可能是1也可能是0

代码如下：

	:::cpp
	/*Problem: 1953		User: awq123
	**Memory: 248K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t,ct,n,d[50][2];
		cin>>t;
		for(int i=1;i<=t;i++)
		{
			cin>>n;
			d[1][1]=1;
			d[1][0]=1;
			for(int j=2;j<=n;j++)
			{
				d[j][1]=d[j-1][0];
				d[j][0]=d[j-1][1]+d[j-1][0];
			}
			ct=d[n][1]+d[n][0];
			cout<<"Scenario #"<<i<<":"<<endl<<ct<<endl<<endl;
		}
	}
