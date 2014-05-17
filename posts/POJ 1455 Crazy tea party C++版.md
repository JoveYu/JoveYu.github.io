<!--
.. title: POJ 1455 Crazy tea party C++版
.. slug: poj-1455
.. date: 2013-04-07T08:50:17+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1455](http://poj.org/problem?id=1455)


解释下题意，n个人围着一个桌子坐，可以交换两个人的位置，问至少交换多少次，可以使座次左右相反！比如原来使12345，要变成54321，但是注意桌子使圆的也可以变为43215同样满足条件！

说起交换，不由想起了冒泡排序，我们这样看讲12345用冒泡排序降序排列，交换次数为n*(n-1)/2,但是我们可以讲这些数分为两块，分别交换，计算推论我们可以知道，两堆越接近越少,那么12345变为32154或21543交换次数最少.

代码简单，纯数学问题，重在思考！

	:::cpp
	/*Problem: 1455		User: awq123
	**Memory: 260K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t;
		cin>>t;
		while(t--)
		{
			int n;
			cin>>n;
			cout<<(n/2)*(n/2-1)/2+(n-n/2)*(n-n/2-1)/2<<endl;
		}
	}
