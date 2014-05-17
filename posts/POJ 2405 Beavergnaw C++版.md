<!--
.. title: POJ 2405 Beavergnaw C++版
.. slug: poj-2405
.. date: 2013-04-07T06:06:51+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2405](http://poj.org/problem?id=2405)


![2405](http://poj.org/images/2405_1.jpg)

纯数学问题，给出D和咬去的V求d，先开始一直再查圆台的体积公式，是这样的：
V＝πh(R2＋Rr＋r2)/3 
r－上底半径 
R－下底半径 
h－高

然而解方程真不方便，后来看到大神用定积分来解题，一下觉得自己高数没学好，真实损失大，直接d的三次方-6v除派再开三次方

代码如下：

	:::cpp
	/*Problem: 2405		User: awq123
	**Memory: 276K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	#include <cmath>
	#include <iomanip>
	using namespace std;

	int main()
	{
		//freopen("input.txt", "r", stdin);
		int d,v;
		while(cin>>d>>v&&d;&&v;)
			cout<<fixed<<setprecision(3)<<pow(d*d*d-6*v/3.1415926,1.0/3)<<endl;
	
	
	}