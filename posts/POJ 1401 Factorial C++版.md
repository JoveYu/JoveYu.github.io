<!--
.. title: POJ 1401 Factorial C++版
.. slug: poj-1401
.. date: 2013-04-07T06:32:07+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1401](http://poj.org/problem?id=1401)


解释下题意，求n！后面有多少个0？比如10的阶乘是3628800那么就输出2！

有人说这个题是水题，其实只是题目简单，要在一个简单的题目里找到好的思路还是很有难度的！

分析下题目，有多少个0就是要求有多少含10的因式，也就是2*5的，但是其中含有的2绝对比5多，那么其实就是求，因式中有多少5

我现开始的思路就是将阶乘的每一个数都计算一次，每一个求因式5的数量，但是这样的方法在1000000000的数字下TLE了

贴下超时代码：

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t,n,i,j,m=0;
		scanf("%d",&t;);
		while (t--)
		{
			m=0;
			scanf("%d",&n;);
			for(i=5;i<=n;i++)
			{
				j=i;
				while(j%5==0)
				{
					m++;
					j/=5;
				}
			}
			printf("%dn",m);
		}
	}



后来转换想法。我们来看看比如60含有因式5的有：  
5 10 15 20 25 30 35 40 45 50 55 60  
他们一次除去本身的因式5得到  
1 2 3 4 5 6 7 8 9 10 11 12  
其中含有因式5的有：  
5 10  
除去5得：  
1 2  
结束  


这样得一个思路可以避免每个数都去求，每个阶段因式5的数量就是最大的数除以5（ps：12/5=2哦）

修改后代码如下：

	:::cpp
	/***************************************
	Problem: 1401		User: awq123
	Memory: 136K		Time: 125MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int t,n,m=0;
		scanf("%d",&t;);
		while (t--)
		{
			m=0;
			scanf("%d",&n;);
			while(n>=5)
			{
				n/=5;
				m+=n;
			}
			printf("%dn",m);
		}
	}