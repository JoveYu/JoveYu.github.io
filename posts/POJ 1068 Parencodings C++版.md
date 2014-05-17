<!--
.. title: POJ 1068 Parencodings C++版
.. slug: poj-1068
.. date: 2013-04-07T04:50:32+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1068](http://poj.org/problem?id=1068)

解释下题意，对于一个括号组合，有两种括号代码，一种是P代码，一种是W代码，英语不好看了半天，还是要提升下，为CCNA准备，下面解释下两种代码：
P代码就是每一个反括号前面的正括号数
W代码就是每一个好括号与其对应的正括号之间的正括号数，算上他本身的那个

题目要求通过P代码，求W代码，典型的模拟题。

我的代码原理就是，先翻译每一个P代码前方的S字符串，用0表示（，用1表示），在通过这个前方的字符串，求该反括号的W代码

具体实现利用

	:::cpp
	temp=p[i]+i;


这句代码通过P代码找出每一个反括号，然后针对这个括号向前找他对应的正括号，其中用flag识别是否为其对应的，用num记录经过的正括号数，依次求出每一个P代码对应的W代码，并放入W数组。

具体代码如下：

	:::cpp
	/*Problem: 1068		User: awq123
	**Memory: 248K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstring>
	using namespace std;

	int main()
	{
		int s[41],p[21],w[21];
		int i,j,t,n,temp,num,flag;
		cin>>t;
		while(t--)
		{
			cin>>n;
			memset(s,0,sizeof(s));
			memset(w,0,sizeof(w));
			for(i=0;i<n;i++)
			{
				cin>>p[i];
				temp=p[i]+i;
				s[temp]=1;
				num=1,flag=0;
				for(j=temp-1;j>=0;j--)
				{	
					if(s[j]==0&&flag;==0)
					{
						w[i]=num;
						break;
					}
					else if(s[j]==1)
					{
						flag++;
						num++;
					}
					else if(s[j]==0)
						flag--;
				}
			}
			for(i=0;i<n;i++)
				cout<<w[i]<<" ";
			cout<<endl;
		}
	}
