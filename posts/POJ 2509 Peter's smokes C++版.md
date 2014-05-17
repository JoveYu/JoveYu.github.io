<!--
.. title: POJ 2509 Peter's smokes C++版
.. slug: poj-2509
.. date: 2013-04-07T09:08:18+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2509](http://poj.org/problem?id=2509)


继续每日一水，简单模拟题，还是贡献了2个WA，题目就是k个盖子可以再换瓶，问n瓶最多喝几瓶？

模拟每次的换和喝的流程。不过我写算法的时候漏了个=的情况，哎！

代码如下：

	:::cpp
	/*Problem: 2509		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	using namespace std;

	int main()
	{
		int n,k;
		while(cin>>n>>k)
		{
			int sum=n;
			while(n>=k)//错在这里了
			{
				sum+=n/k;
				n=n/k+n%k;
			}
			cout<<sum<<endl;
		}
	}