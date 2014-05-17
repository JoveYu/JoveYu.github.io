<!--
.. title: POJ 2602 Superlong sums C++版
.. slug: poj-2602
.. date: 2013-04-07T08:44:31+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2602](http://poj.org/problem?id=2602)

题意要求我们模拟高精度加法运算，我们把数字横过来看就是正常加法了。不多说模拟进位运算，现开始用整型数组保存数据，结果一直超时，于是用字符数组试了下，事实证明，输出字符串，比没一个字母输出快！

PS：其中输入时，后面加上了n也可以在输入语句后加上getchar()代替！

代码如下：

	:::cpp
	/*Problem: 2602		User: awq123
	**Memory: 3112K		Time: 1500MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;
	char a[1000005],b[1000005],sum[1000005];
	int main()
	{
		int n,i,jw;
		scanf("%dn",&n;);
		for(i=0;i<n;i++)
			scanf("%c %cn",&a;[i],&b;[i]);
		jw=0;
		for(i=n-1;i>=0;i--)
		{
			int temp=a[i]-'0'+b[i]-'0'+jw;
			sum[i]=temp%10+'0';
			jw=temp/10;
		}
		sum[n]='\00';
		if(jw!=0)
			printf("%d",jw);
		printf("%s",sum);
	}
