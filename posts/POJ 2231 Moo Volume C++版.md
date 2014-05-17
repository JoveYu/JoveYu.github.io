<!--
.. title: POJ 2231 Moo Volume C++版
.. slug: poj-2231
.. date: 2013-04-07T05:07:59+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2231](http://poj.org/problem?id=2231)

看似简单的题目，把我WA到哭啊，强烈推介这个题目，我自己做的是后总超时。

其中如何优化自己的算法是最重要的，这也是为什么OJ系统都有时间限制的原因，

我的算法是这样的：

比如题目中的1   2   3   4   5

我们可以看见每两个之间的距离，也就是就是这个数与其他数的差，所以就想到了相加的算法，现开始因为数据类型错误还WA了几次就不说了。

最原始的代码是：

	:::cpp
	for(i=0;i<m;i++)
		for(j=0;j<m;j++)
			if(i!=j)
				s+=(num[i]>=num[j])?(num[i]-num[j]):(num[j]-num[i]);
	cout<<s<<endl;
}

超时没商量，我了个去哦，后来想到对于一个序列的排序，都会有重复状况，优化算法排除其中相互成对的情况，优化代码如下：

	:::cpp
	for(i=0;i<m;i++)
		for(j=i+1;j<m;j++)
			s+=(num[i]>=num[j])?(num[i]-num[j]):(num[j]-num[i]);
	cout<<2*s<<endl;

可是还是超时，我就没办法了，后来只能去看解体报告，结果居然是abs函数，我了个去额，库函数就是好些啊，我这个简易abs也不算太差啊
最后代码如下：

	:::cpp
	/*Problem: 2231		User: awq123
	**Memory: 296K		Time: 563MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cmath>
	using namespace std;

	int main()
	{
		int m,i,j,num[10002];
		long long int s=0;
		cin>>m;
		for(i=0;i<m;i++)
			scanf("%d",&num;[i]);
		for(i=0;i<m;i++)
			for(j=i+1;j<m;j++)
				s+=abs(num[i]-num[j]);
		cout<<2*s<<endl;
	}


这个题给我很多启发，多学习使用库函数去优化代码，听说boost更加好，改天学习下，以上是我的思路，解题报告中还看到个不错的算法，也贴出来学习下

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <vector>
	using namespace std;

	int main()
	{
		long long int m,i,s=0,num[10002];
		cin>>m;
		for(i=0;i<m;i++)
			cin>>num[i];
		sort(num,num+m);
		for(i=0;i<m-1;i++)
			s += (m-1-i) * (num[m-1-i] - num[i]);
		cout<<s*2<<endl;
	}