<!--
.. title: POJ 3302 Subsequence C++版
.. slug: poj-3302
.. date: 2013-04-07T08:20:17+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3302](http://poj.org/problem?id=3302)


解释下题目，问是否能在一个字符串正顺序，或者逆顺序中，删除一些字母组成另一个字符串。

注意：正序是以'\0'逆序则要以第一个字母的前面一位结束


代码如下：

	:::cpp
	/*Problem: 3302		User: awq123
	**Memory: 236K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char s[105],t[105];
		int n;
		cin>>n;
		while(n--)
		{
			cin>>t>>s;
			int ok=0;
			char *ps=s,*pt=t;
			while(1)
			{
				if(*ps=='\00')
				{
					ok=1;
					break;
				}
				if(*pt=='\00')
					break;
				if(*ps==*pt)
					ps++;
				pt++;
			}
			ps=s;
			while(1)
			{
				if(ok)
					break;
				if(*ps=='\00')
				{
					ok=1;
					break;
				}
				if(pt==t-1)
					break;
				if(*ps==*pt)
					ps++;
				pt--;
			}
			if(ok)
				cout<<"YES"<<endl;
			else
				cout<<"NO"<<endl;
		}
	}