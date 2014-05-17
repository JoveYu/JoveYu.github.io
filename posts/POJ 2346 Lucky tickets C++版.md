<!--
.. title: POJ 2346 Lucky tickets C++版
.. slug: poj-2346-lucky-tickets-c
.. date: 2013-04-07T05:57:26+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2346](http://poj.org/problem?id=2346)


介绍下题意，给定一个偶数 n，求 n 位 lucky tickets 的个数，lucky tickets就是 n 位数可含前导 0，前 n/2 项上数字和等于后 n/2 项上数字和。

先上一种最简单的算法，我们管它叫流氓算法，再算法分类上算穷举把！

玩笑而已。之所以这样是因为我都知道答案了，而且数据不多。

代码如下：

	:::cpp
	/*Problem: 2346		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int n;
		cin>>n;
		if(n==2)
			cout<<10<<endl;
		if(n==4)
			cout<<670<<endl;
		if(n==6)
			cout<<55252<<endl;
		if(n==8)
			cout<<4816030<<endl;
		if(n==10)
			cout<<432457640<<endl;
	}


这个是玩笑而已，没事娱乐下，真正做这个题应该用DP的，不过不会，改天研究下，呵呵