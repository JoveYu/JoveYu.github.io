<!--
.. title: POJ 2586 Y2K Accounting Bug C++版
.. slug: poj-2586
.. date: 2013-04-07T04:54:11+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2586](http://poj.org/problem?id=2586)

这个题目要求我们分析公司盈亏，题目有点麻烦，盈利和亏损的钱是固定的，公司每5个月汇总一次，全年都是亏的，问一年最多盈利多少钱，s表示盈利，d表示亏损，5个月统计一次都亏空，那么有5种情况：

1、若SSSSD亏空，那么全年最优情况为SSSSDSSSSDSS
2、若SSSDD亏空，那么全年最优情况为SSSDDSSSDDSS
3、若SSDDD亏空，那么全年最优情况为SSDDDSSDDDSS
4、若SDDDD亏空，那么全年最优情况为SDDDDSDDDDSD
5、若DDDDD亏空，那么全年最优情况为DDDDDDDDDDDD

先令num为最坏测情况也就是第五种，然后一次分析，注意越前面的盈利越大，但是要满足在五个月内是亏损的，所以一次由上到下分析，简单if语句解决，如果有最大的盈利时替换num

代码如下：

	:::cpp
	/*Problem: 2586		User: awq123
	**Memory: 248K		Time: 32MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	using namespace std;
	#define max(a,b) (a>b)?a:b

	int main()
	{
		int s, d, num;
		while(cin>>s>>d)
		{
			num=-12*d;
			if(4*s<d)
				num=max(num,10*s-2*d);
			else if(3*s<2*d)
				num=max(num,8*s-4*d);
			else if(2*s<3*d)
				num=max(num,6*s-6*d);
			else if(1*s<4*d)
				num=max(num,3*s-9*d);
			if(num>0)
				cout<<num<<endl;
			else 
				cout<<"Deficit"<<endl;
		}
	}