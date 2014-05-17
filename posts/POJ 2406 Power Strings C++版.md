<!--
.. title: POJ 2406 Power Strings C++版
.. slug: poj-2406
.. date: 2013-04-07T06:07:57+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2406](http://poj.org/problem?id=2406)


解释下题意，就是问一个字符串可以看成一个子串循环最多多少次组成，比如
abcd就是abcd循环1次
aaaa就是a循环4次
ababab就是ab循环3次

由1开始扫描每种可能的节长，一一对比，直到到串尾还满足！

花了900多ms好像也有简单的方法，改天研究下！

代码如下：

	:::cpp
	/*Problem: 2406		User: awq123
	**Memory: 1216K		Time: 969MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		char c[1000001];
		int i,j,len,flag;
		start:
		scanf("%s",c);
		len=strlen(c);
		if(c[0]=='.')
			return 0;
		for(i=1;i<=len;i++)
		{
			flag=1;
			if(len%i==0)
				for(j=0;j<len;j++)
				{
				
					if(c[j%i]!=c[j])
					{
						flag=0;
						break;
					}
					if(j==len-1&&flag;)
					{
						cout<<len/i<<endl;
						goto start;
					}
				}
		}
	
	}