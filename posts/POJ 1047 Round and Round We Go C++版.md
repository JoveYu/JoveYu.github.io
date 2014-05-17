<!--
.. title: POJ 1047 Round and Round We Go C++版
.. slug: poj-1047
.. date: 2013-04-07T04:32:46+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1047](http://poj.org/problem?id=1047)

这题不算个简单的题，主要在于算法，但是还是多谢别人总结的：
对于数N，若N为循环的则有N*(length(N)+1)=99....99， (length(N)个9)，length(N)为N的位数，含前导0。
代码调用一个judge函数判断是否成功，水题。
代码如下：

	:::cpp
	/*Problem: 1047		User: awq123
	**Memory: 212K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include<iostream>
	#include<string>
	using namespace std;
	int judge(string str)
	{
		int n=str.length()+1;
		int i,up=0,temp=0;
		for(i=n-2;i>=0;i--)
		{
			temp=(int)(str[i]-'0');
			if((temp*n+up)%10!=9) return 0;
			up=(temp*n+up)/10;
		}
		return 1;
	}
	int main()
	{
		string str;
		while(cin>>str)
		{
			if(judge(str))
			{
				cout<<str<<" is cyclic"<<endl; 
			}
			else
			{
				cout<<str<<" is not cyclic"<<endl;
			}
		}
		return 0;
	}