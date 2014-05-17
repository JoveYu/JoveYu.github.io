<!--
.. title: POJ 3219 Binomial Coefficients C++版
.. slug: poj-3219
.. date: 2013-04-07T08:18:32+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3219](http://poj.org/problem?id=3219)


题意简单，求C(n，k)的奇偶性，

我的方法不简单，但分析简单，不过今天还看到个大神的分析，让我很是佩服

我门知道C(n，k)=n!/k!/(n-k)!那么就通过分析这三项的2的阶数来分析C(n，k)的2的阶数，也就是n!的阶数<=k!的阶数+(n-k)!阶数，则为奇数。

其中n!的2的阶数求解的方法为n/2+n/4+n/8....我就是用的这个方法，

	:::cpp
	int y(int d)
	{
		int s=0;
		for(int i=2;d/i;i*=2)
			s+=d/i;
		return s;
	}

还有一种位运算的，我试了下都可以，但是对位运算的方法不是很懂，但是运行时间还是有提升的

	:::cpp
	int y(int d)
	{
	    int s=0;
	    while((d=d>>1)!=0)
		s+=d;
	    return s;
	}


我的代码如下：

	::cpp
	/*Problem: 3219		User: awq123
	**Memory: 244K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int y(int d)
	{
		int s=0;
		for(int i=2;d/i;i*=2)
			s+=d/i;
		return s;
	}

	int main()
	{
		int n,k;
		while (cin>>n>>k)
		{
			if(k>n-k)
				k=n-k;
			if(y(n)<=y(n-k)+y(k))
				cout<<1<<endl;
			else
				cout<<0<<endl;
		}
	}


这个题还见到了一种大神的做法

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int n,k;
		while (cin>>n>>k)
		{
			if((k&n;)==k)
				cout<<1<<endl;
			else
				cout<<0<<endl;
		}
	}

这个方法利用位运算分析，也不知道他怎么总结出来的，我看了分析还是不懂，参考自[hi.baidu.com/doraemonshare/blog/item/9bee7cd00a38f7349b502749.html](http://hi.baidu.com/doraemonshare/blog/item/9bee7cd00a38f7349b502749.html)