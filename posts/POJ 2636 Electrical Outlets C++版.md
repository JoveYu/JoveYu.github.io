<!--
.. title: POJ 2636 Electrical Outlets C++版
.. slug: poj-2636
.. date: 2013-04-07T09:49:16+08:00
.. tags:
.. link:
.. description:
.. type: text
-->


题目链接：[http://poj.org/problem?id=2636](http://poj.org/problem?id=2636)


水题，问一堆插座相互相接后有多少个插孔可以用

代码如下：

	:::cpp
	/*Problem: 2636		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	/*
	#include <iostream>
	#include <cstdio>

	using namespace std;

	int main()
	{
	    int n;
		cin>>n;
		while(n--)
		{
			int m;
			cin>>m;
			int sum=1-m;
			while(m--)
			{
				int t;
				cin>>t;
				sum+=t;
			}
			cout<<sum<<endl;
		}
	}