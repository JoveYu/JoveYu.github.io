<!--
.. title: POJ 2109 Power of Cryptography C++版
.. slug: poj-2109
.. date: 2013-04-07T04:51:38+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2109](http://poj.org/problem?id=2109)

本题要求，求出所给k和p的幂次n，虽然题目给出的范围很大，但是查阅了下double的精度

然而精度已经够高了，关于求幂次的函数pow在cmath里有具体用法查阅MSDN是这样说的
>Calculates x raised to the power of y.
也就是说求x^y，这里利用的1/n实现求幂次，学习了

代码如下：

	:::cpp
	/*Problem: 2109		User: awq123
	**Memory: 272K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include<iostream>
	#include <iomanip>
	#include <cmath>
	using namespace std;

	int main()
	{
		double n,p;
		while(cin>>n>>p)
		{
			double k=pow(p,1/n);
			cout<<setprecision(0)<<k<<endl;
		}
	}


我试了下其实不指定输出的小数点限制，他也会默认不显示，但是运行时间会长些。