<!--
.. title: POJ 2242 The Circumference of the Circle C++版
.. slug: poj-2242
.. date: 2013-04-07T05:39:42+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2242](http://poj.org/problem?id=2242)


题目给出三个点坐标，求经过三个点的圆的周长。

纯数学问题，没什么好说的

其中fixed是用来输出纯浮点，也就是不使用科学计数法，若要使用科学计数法应该使用scientific

代码如下：

	:::cpp
	/*Problem: 2242		User: awq123
	**Memory: 252K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cmath>
	#include <iomanip>
	using namespace std;

	double square(double x)
	{
		return x*x;
	}
	int main()
	{
		double X1, X2, X3, Y1, Y2, Y3;
		double PI = 3.141592653589793;
		while(cin>>X1>>Y1>>X2>>Y2>>X3>>Y3)
		{
			double a = sqrt(square(X1 - X2) + square(Y1 - Y2));
			double b = sqrt(square(X1 - X3) + square(Y1 - Y3));
			double c = sqrt(square(X2 - X3) + square(Y2 - Y3));
			double p = (a + b + c) / 2;
			double s = sqrt(p * (p - a) * (p - b) * (p - c));
			double r = a * b * c / (s * 4);
			cout<<fixed<<setprecision(2)<<2 * PI * r<<endl;
		}
	}
