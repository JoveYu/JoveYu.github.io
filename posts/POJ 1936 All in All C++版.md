<!--
.. title: POJ 1936 All in All C++版
.. slug: poj-1936
.. date: 2013-04-07T08:05:31+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1936](http://poj.org/problem?id=1936)


题目问是否能在字符串t中去掉一些字母组成字符串s，一个简单的题目，用指针轻松解决，可是WA了3次才发现我输出的yesno是小写，郁闷了半天


代码如下：

	:::cpp
	/*Problem: 1936		User: awq123
	**Memory: 400K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char s[100005],t[100005];
		while(cin>>s>>t)
		{
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
			if(ok)
				cout<<"Yes"<<endl;
			else
				cout<<"No"<<endl;
		}
	}