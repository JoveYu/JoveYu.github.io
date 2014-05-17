<!--
.. title: POJ 1828 Monkeys' Pride C++版
.. slug: poj-1828
.. date: 2013-04-07T05:03:45+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1828](http://poj.org/problem?id=1828)

题意给出许多点，每个点代表一个猴子，猴王就是没有横坐标和纵坐标都大于他的猴子，问有几个猴王？

这个题目的算法已经给我们了，就是在一个点位原点的坐标系内，第一象限没有点，不包括坐标轴。

思路是这样的，利用结构体构造点阵，先对结构题中的x排序，对于每个相同的x，取最大的y，这样排除了靠里面不可能的点，然后由x最大的那个点开始，往前扫描,如果出现某个猴子的y大于当前最大y时，代表其满足条件，那么计数更新，再由这个点开始，向前找，依次求出，因为永远会有最大值，所以至少有一个，计数的初值为1，在本机上错过一次因为没注意结尾的0，多输出了个1。

代码不算复杂，但是完成这个题第一次AC用了922ms，主要是因为这个题需要大量的输入，那么c++的类输入会造成很大的浪费，修改为c语言普通输入输出，结果219ms，还算不错

代码如下：

	:::cpp
	/*Problem: 1828		User: awq123
	**Memory: 556K		Time: 219MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <cstdlib>
	using namespace std;
	struct point
	{
	int x,y;
	}p[50001];

	int cmp(const void *a,const void *b)
	{
		if(((point *)a)->x==((point *)b)->x)
			return ((point *)a)->y>((point*)b)->y ?1:-1;
		else
			return ((point *)a)->x>((point *)b)->x ?1:-1;
	}

	int main()
	{
		int t,i,max,temp;
		while(scanf("%d",&t;)&&t;)
		{
			for(i=0;i<t;i++)
				scanf("%d%d",&p;[i].x,&p;[i].y);
			qsort(p, t, sizeof(p[0]), cmp);
			max=1;
			temp=p[t-1].y;
		for(i=t-2;i>=0;i--)
		{
		    if(temp<p[i].y)
		    {
		        temp=p[i].y;
		        max++;
		    }
		}
		printf("%dn",max);

		}
	}