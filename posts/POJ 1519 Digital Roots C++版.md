<!--
.. title: POJ 1519 Digital Roots C++版
.. slug: poj-1519
.. date: 2013-04-07T08:40:30+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1519](http://poj.org/problem?id=1519)


这个题，原本我想模拟做的，但是其实又更简单的办法，让我很惊讶，难道是小学奥术没学好？？

把一个数字的各位相加得到一个和，这个和又是一个新的数，把这个数的各位再次相加又得到一个和，如此一直重复做，直到最后的数字之和是一位数。这个数就是原数除以9的余数，我们把这个余数称之为原数的"数字根"。这道题肯定没有告诉你数字根和各位相加对9取余是一样的啦

代码如下：

	:::cpp
	/*Problem: 1519		User: awq123
	**Memory: 244K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		char str[2000];
		while(cin>>str&&str;[0]!='0')
		{
			int i,sum=0,len=strlen(str);
			for(i=0;i<len;i++)
				sum+=str[i]-'0';
			sum%=9;
			if(sum==0)
				cout<<9<<endl;
			else
				cout<<sum<<endl;
		}
	}