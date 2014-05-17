<!--
.. title: POJ 1844 Sum C++版
.. slug: poj-1844
.. date: 2013-04-07T08:31:42+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1884](http://poj.org/problem?id=1884)


题意是，给出一个数，求出最小的n，使得1,2,3...n中间加上+或-得到这个数

我们一直由1开始加，知道sum>=这个数，如果等于就直接输出，如果大于，再判断sum-这个数是否为奇数，若为奇数，则变化任何一个+为-变化量为偶数，无论怎么样都无法实现，直接n++，若为偶数，变化其中一个，变化量为偶数，可以实现。


代码如下：

	:::cpp
	/*Problem: 1844		User: awq123
	**Memory: 252K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int n=1,t;
		cin>>t;
		while(1)
		{
			int sum=(n+1)*n/2;
			if(sum==t)
				break;
			if(sum>t&&(sum-t)%2==0)
				break;
			n++;
		}
			cout<<n<<endl;
	}