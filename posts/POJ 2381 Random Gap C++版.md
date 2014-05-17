<!--
.. title: POJ 2381 Random Gap C++版
.. slug: poj-2381
.. date: 2013-04-07T06:05:22+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2381](http://poj.org/problem?id=2381)


解释下题意，依次用（a×c+r）%m取随机数，直到循环，然后求在这些随机数里哪个区间最大，是多少！

这个题我很是郁闷了一晚上，做到完全想不出有什么问题了，还是WA，后来百度直到问的别人，我原来的代码是

	:::cpp
	temp=0;flag=0;max=0;

and

	:::cpp
	if(d[i]==0&&flag;==1)

adn

	:::cpp
	if(d[i]==1&&flag;==1)

思路上我的想法没错，通过d数组记录取过的数，标记为1，然后在从头开始扫描每个1之间的距离。

代码如下：

	:::cpp
	/*Problem: 2381		User: awq123
	**Memory: 62928K		Time: 1891MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>

	using namespace std;
	int d[16000002];
	int main()
	{
		long long int a,c,m,r,i,flag,temp,max;
		cin>>a>>c>>m>>r;
		memset(d,0,sizeof(d));
		d[r]=1;
		while(!d[(a*r+c)%m])
		{
			r=(a*r+c)%m;
			d[r]=1;
		}
		temp=0;flag=0;max=-1;
		for(i=0;i<m;i++)
		{
			if(d[i]==1&&flag;==0)
				flag=1;
			else if(d[i]==0&&flag;==1)
				temp++;
			else if(d[i]==1&&flag;==1)
			{
				if(temp>max)
					max=temp;
				temp=0;
			}
		}
		cout<<max+1<<endl;
	
	}