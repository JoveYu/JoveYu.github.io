<!--
.. title: POJ 1579 Function Run Fun C语言版
.. slug: poj-1579
.. date: 2013-04-07T08:22:03+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1579](http://poj.org/problem?id=1579)


题目没什么好说的，给出了递归算法，但是单纯模拟题意，你会发现递归过多，严重超时。这里我们利用DP里的记忆搜索，开一个数组记录已经求出的值，减少递归的计算次数，单纯优化运行速度，对于这样的题OJ系统的数据是不可想象的，就算你的能运行，在OJ系统里的数据也过不了！

代码如下：

	:::cpp
	/*Problem: 1579		User: awq123
	**Memory: 228K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <cstring>
	#include <iostream>
	#include <algorithm>
	using namespace std;

	int map[25][25][25];

	int w(int a,int b,int c)
	{
		if(a<=0||b<=0||c<=0)
			return map[0][0][0]=1;
		else if(a>20||b>20||c>20)
			return map[20][20][20]=w(20,20,20);
		else if(map[a][b][cpp])
			return map[a][b][cpp];
		else if(a<b&&b;<c)
			return map[a][b][cpp]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c);
		else
			return map[a][b][cpp]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1);
	}

	int main()
	{
		memset(map,0,sizeof(map));
		int a,b,c;
		while(scanf("%d %d %d",&a;,&b;,&c;)==3&&!(a==-1&&b;==-1&&c;==-1))
			printf("w(%d, %d, %d) = %dn",a,b,c,w(a,b,c));
	}