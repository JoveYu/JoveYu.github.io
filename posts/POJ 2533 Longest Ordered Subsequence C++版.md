<!--
.. title: POJ 2533 Longest Ordered Subsequence C++版
.. slug: poj-2533
.. date: 2013-04-07T08:54:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1079](http://poj.org/problem?id=1079)


最长上升子串，利用动态规划解题。

对于给定数列E，元素个数为n,最长上升子序列Q满足对任意1<=i<j<=n，有Q[i]<Q[j]，且E[i]<E[j]。
容易得出O(n^2)的DP递推公式：  
D[i]=max{D[j]}+1;(1<=j<i且E[j]<E[i])  
D[i]为以元素i结尾的最长子序列个数。  
这样经过两重循环一次遍历可以得到最长上升子序列。  


代码如下：

	:::cpp
	/*Problem: 2533		User: awq123
	**Memory: 268K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,j,t,d[1005],dp[1005];
		cin>>t;
		int max=-1;
		for(i=1;i<=t;i++)
		{
			cin>>d[i];
			dp[i]=1;
			for(j=1;j<i;j++)
			{
				if(d[j]<d[i]&&dp;[i]<dp[j]+1)
					dp[i]=dp[j]+1;
			}
			if(max<dp[i])
				max=dp[i];
		}
		cout<<max<<endl;
	}