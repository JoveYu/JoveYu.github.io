<!--
.. title: POJ 1218 THE DRUNK JAILER C++版
.. slug: poj-1218
.. date: 2013-04-07T06:29:14+08:00
.. tags:
.. link:
.. description:
.. type: text
-->


题目链接：[http://poj.org/problem?id=1218](http://poj.org/problem?id=1218)


做了才知道为什么说这题式用来调节心情的，呵呵，话不多说，直接开方就是了。

不过第一次提交CE没办法，现在都用g++，还是有点区别的，c++里sqrt直接开int会编译错误，后来改成double，AC！

代码如下：

	:::cpp
	/***************************************
	Problem: 1218		User: awq123
	Memory: 224K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	using namespace std;

	int main()
	{
		int t;
		double n;
		cin>>t;
		while(t--)
		{
			cin>>n;
			cout<<(int)sqrt(n)<<endl;
		}
	}