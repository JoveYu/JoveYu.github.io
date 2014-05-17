<!--
.. title: POJ 1922 Ride to School C++版
.. slug: poj-1922-ride-school-c
.. date: 2013-04-07T05:26:50+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1922](http://poj.org/problem?id=1922)


题意简单讲下，有个男的比较怪，喜欢跟着快的走，然后给出，几个人的速度和出发时间，求出这个男的到的时间；

其实题意很容易想到算法，那么这个男的必然和第一个到达的同时到达，当然要去掉时间为负数，提前出发的人。

这个题不难，主要是纠结了两个问题，

一个是，当是时间为不为整数的时候应该，统一取大于大的那个整数，但是自动转换会取小的，我利用了一个简单的算法，想了半天

	:::cpp
		int temp=min;
		if(temp==min)
			cout<<temp<<endl;
		else 
			cout<<temp+1<<endl;


其实有个函数可以解决这个问题的，就是<cmath>中的ceil函数直接就可以转换，只是当时我不知道，可以改为：

	:::cpp
	cout<<ceil(min)<<endl;

第二点是我百思不得其解的，就是，关于计算机做乘除时的误差问题，为什么这么讲呢，比如我原来的语句是

	:::cpp
	ts=4500/(v/3.6)+t;

这样的一个算法，除法的精确情况没有乘法好，就因为这WA了半天，后来总结出以后尽量用乘法；

综合来说题目不难，代码如下：

	:::cpp
	/*Problem: 1922		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int n,i,t,v;
		double ts,min;
		while(cin>>n&&n;)
		{
			min=4500*3.6;
			for(i=0;i<n;i++)
			{
				scanf("%d%d",&v;,&t;);
				if(t>=0)
				{
					ts=4500*3.6/v+t;
					if(ts<min)
						min=ts;
				}
			}
			int temp=min;
			if(temp==min)
				cout<<temp<<endl;
			else 
				cout<<temp+1<<endl;
		}
	}