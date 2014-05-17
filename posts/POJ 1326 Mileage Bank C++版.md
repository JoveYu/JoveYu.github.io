<!--
.. title: POJ 1326 Mileage Bank C++版
.. slug: poj-1326
.. date: 2013-04-07T06:35:15+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1326](http://poj.org/problem?id=1326)

题意就是要求我们计算飞机的总费用，地名只是眼子，不用管，头等舱两倍于路程的价格，商务舱1.5倍于路程的价格，经济舱，若路程小于500按500算，1倍于路程的价格！0结束一次飞行，#结束程序！

简单模拟题，不过有一点，我觉得学会了一些东西，就是：



>Hint   
>  
>When calculate bonus ,be sure you rounded x.5 up to x+1  

当我们用int()强制转换时电脑会默认去掉小数，如何利用电脑去4舍5入，也算是这个题的一个考点了，我们巧妙的加上0.5就可能让电脑将尾数在5后的数识别到下一个整数里。

详细可以参见代码：

	:::cpp
	/***************************************
	Problem: 1326		User: awq123
	Memory: 252K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char temp[20],c;
		float n;
		int sum=0;
		while(cin>>temp)
		{
			if(temp[0]=='#')
				break;
			else if(temp[0]=='0')
			{
				cout<<sum<<endl;
				sum=0;
				continue;
			}
			cin>>temp;
			cin>>n>>c;
			if(c=='F')
				sum+=int(2*n+0.5);
			else if (c=='B')
				sum+=int(1.5*n+0.5);
			else if (c=='Y')
			{
				if(n<500)
					sum+=500;
				else
					sum+=int(n+0.5);
			}
		}
	}