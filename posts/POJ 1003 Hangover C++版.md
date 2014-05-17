<!--
.. title: POJ 1003 Hangover C++版
.. slug: poj-1003
.. date: 2013-04-07T04:20:18+08:00
.. tags:
.. link:
.. description:
.. type: text
-->


题目链接：[http://poj.org/problem?id=1003](http://poj.org/problem?id=1003)

说实话，这个题目我看了半天，（不得不承认自己的英语水了点），网上都说这个是个水题，其实代码也不复杂，但是有些细节还是要注意的，题目大意可以理解成求1/2+1/3....1/x>=n的最小x值，我用最原始的方法做的，显然耗时有点多，看到别人0msAC还是很羡慕的，方法上还要优化啊
第一次超时代码：

	:::cpp
	sum+=(1/i);

导致for循环成死循环
第二次WA

	:::cpp
	int i;
	double  n=1,sum;
	while(n!=0)
	{
		cin>>n;
		for(i=2,sum=0;sum<n;i++)
		{
			sum+=(1.0/i);
		}
		cout<<i-2<<" card(s)"<<endl;
	}

输入0的时候会多输出次card，这个是我没注意后来修改代码通过！！
完整代码如下：

	:::cpp
	/*Problem: 1003		User: awq123
	**Memory: 256K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	using namespace std;
	int main()
	{
		int i;
		double  n,sum;
		cin>>n;
		while(n!=0)
		{
			for(i=2,sum=0;sum<n;i++)
			{
				sum+=(1.0/i);
			}
			cout<<i-2<<" card(s)"<<endl;
			cin>>n;
		}
	return 0;	
	}