<!--
.. title: POJ 1016 Numbers That Count C++版
.. slug: poj-1016
.. date: 2013-04-07T06:22:13+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1016](http://poj.org/problem?id=1016)

解释下题意，对一列数进行转换依次升序输出数字输出的次数和这个数字，比如
31123314中，1有3个，2有一个，3有3个，4有1个，那么转换为31123314，

题目要求写出数子的特性，有如下几种

* 自我循环，既转换一次后就与原来相同；
* j步转换后有与前一次相同的数字，之后开始循环；
* j步转换后与与前面，但不是前一次的相同那么永远不能循环：
* 15次转换后都没有结果！

这题利用了string，这个字符串比普通char强大太多，对于数组的添加写入分离，以及计算都方便太多了，有普通整形数组应该也能做，不过麻烦点！

解释下思路，编写work完成一次转换，其中利用w保存每个数的次数，其中应该注意，次数如果大于9就要输出两格了，然后循环15次一次转换字符串，每次转换后与前面的情况比较，看是否有相同的，如果相同则跳出，根据循环次数，以及对比的次数，分析各种情况；

* 循环1次
* 循环i次后，对比了j次；
* 循环i次后，对比了不到j次；
* 循环了15次！

其中有个小问题让我郁闷了半天C++提交老是编译错误，我G++编译就没问题，后来搞了半天才知道C++里不叫cstring叫string！郁闷！

代码如下：

	:::cpp
	/**************************************
	Problem: 1016		User: awq123
	Memory: 244K		Time: 16MS
	Language: C++		Result: Accepted
	**************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <string>
	#include <algorithm>
	using namespace std;

	string str[16];
	void work(int t)
	{
		int i,w[10]={0};
		for(i=0;i<(int)str[t].size();i++)
			w[str[t][i]-'0']++;
		string s="";
		for(i=0;i<10;i++)
			if(w[i]>0&&w;[i]<10)
			{
				s+=w[i]+'0';
				s+=i+'0';
			}
			else if(w[i]>=10)
			{
				s+=w[i]/10+'0';
				s+=w[i]%10+'0';
				s+=i+'0';
			}
		str[t+1]=s;
	}

	int main()
	{
		int i,j,flag;
		while(cin>>str[0]&&str;[0][0]!='-')
		{
			for(i=0;i<15;i++)
			{
				flag=0;
				work(i);
				for(j=0;j<=i;j++)
					if(str[i+1]==str[j])
					{
						flag=1;
						break;
					}
				if(flag==1)
					break;
			}
			if(flag)
			{
				if(i==0)
					cout<<str[0]<<" is self-inventorying"<<endl;
				else if(j==i)
					cout<<str[0]<<" is self-inventorying after "<<i<<" steps"<<endl;
				else
					cout<<str[0]<<" enters an inventory loop of length "<<i-j+1<<endl;
			}
			else
				cout<<str[0]<<" can not be classified after 15 iterations"<<endl;
		}
	}