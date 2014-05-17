<!--
.. title: POJ 1247 Magnificent Meatballs C++版
.. slug: poj-1247
.. date: 2013-04-07T08:09:08+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1247](http://poj.org/problem?id=1247)


解释下题意，S顺时针走E逆时针走，每走过一个点，加上这个数，问在哪相遇可以使两个和相同，输出两个的位置，否则输出不行！

简单模拟题，根据题意，模拟每个点相遇的情况比较每次的和！

	:::cpp
	/*Problem: 1247		User: awq123
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
		int i,j,n,d[35],sume,sums;
		while(cin>>n&&n;)
		{
			for (i=0;i<n;i++)
				cin>>d[i];
			for (i=0;i<n;i++)
			{
				sume=0;
				sums=0;
				for(j=0;j<i;j++)
					sums+=d[j];
				for(j=i;j<n;j++)
					sume+=d[j];
				if(sume==sums)
					break;
			}
			if(sume==sums)
				cout<<"Sam stops at position "<<i<<" and Ella stops at position "<<i+1<<"."<<endl;
			else
				cout<<"No equal partitioning."<<endl;
		}
	}