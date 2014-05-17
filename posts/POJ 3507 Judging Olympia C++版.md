<!--
.. title: POJ 3507 Judging Olympia C++版
.. slug: poj-3507
.. date: 2013-04-07T08:29:55+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3507](http://poj.org/problem?id=3507)


简单题，六个分数去掉一个最高分，去掉一个最低分，然后取平均值，然而这题的难点在于输出要求：

>(without unnecessary decimal points and/or zeros.)

也就是输出浮点数，但不输出多余的0，其实要是用printf输出，我觉得很麻烦，还要判断这那的，不过C++中cout对浮点的输出会自动优化这些，嘿嘿，又偷懒了！


代码如下：

	:::cpp
	/*Problem: 3507		User: awq123
	**Memory: 248K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int i,d[6];
		while(1)
		{
			float sum=0;
			for(i=0;i<6;i++)
			{
				cin>>d[i];
				sum+=d[i];
			}
			if(sum==0)
				break;
			sort(d,d+6);
			sum-=d[0];
			sum-=d[5];
			sum/=4;
			cout<<sum<<endl;
		}
	}