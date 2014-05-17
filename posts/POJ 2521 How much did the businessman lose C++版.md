<!--
.. title: POJ 2521 How much did the businessman lose C++版
.. slug: poj-2521
.. date: 2013-04-07T09:02:10+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2521](http://poj.org/problem?id=2521)

水题，计算一系列交易后，因假币损失的钱，理清思路后不难，本来应该赚的是m-n，然后亏的钱就是那个假币，

	:::cpp
	/*Problem: 2521		User: awq123
	**Memory: 224K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <IOSTREAM>
	using namespace std;

	int main()
	{
		int n,m,p,c;
		while(cin>>n>>m>>p>>c&&n;+m+p+c)
		{
			cout<<p-(m-n)<<endl;
		}
	
	}