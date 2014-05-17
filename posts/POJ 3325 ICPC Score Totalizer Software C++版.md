<!--
.. title: POJ 3325 ICPC Score Totalizer Software C++版
.. slug: poj-3325
.. date: 2013-04-07T08:26:53+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3325](http://poj.org/problem?id=3325)


题目很简单，去掉一个最高分，去掉一个最低分，求平均分，小日本的题目还是很简单的！

	:::cpp
	/*Problem: 3325		User: awq123
	**Memory: 248K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,d[105];
		while(cin>>n&&n;)
		{
			int sum=0;
			for(int i=0;i<n;i++)
			{
				cin>>d[i];
				sum+=d[i];
			}
			sort(d,d+n);
			sum-=d[0];
			sum-=d[n-1];
			sum/=n-2;
			cout<<sum<<endl;
		}
	}