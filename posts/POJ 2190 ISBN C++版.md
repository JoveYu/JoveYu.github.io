<!--
.. title: POJ 2190 ISBN C++版
.. slug: poj-2190
.. date: 2013-04-07T09:48:31+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2190](http://poj.org/problem?id=2190)


水题但是有些小细节还是要注意，解释下题意，根据给出的规则依次给每个位数加权求和，这里有一个特殊情况，也就是第十位上为X的情况，也就是这位上为10的情况，这里我没有注意，后来才发现的。


我用的方法就是枚举？可以取到的值，来求解！不多解释看注释

代码如下：

	:::cpp
	/*Problem: 2190		User: awq123
	**Memory: 232K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>

	using namespace std;

	int main()
	{
	    char str[12];
	    cin>>str;
	    int sum=0,flag=0,ok=0;
	    //判断？在哪一位并算出除了那位的总和
	    for(int i=0;i<10;i++)
	    {
		if(str[i]=='?')
		    flag=i;
		else if(str[i]=='X')
		    sum+=10*(10-i);
		else
		    sum+=(10-i)*(str[i]-'0');
	    }
	    //依次枚举0-9
	    for(int i=0;i<10;i++)
		if((sum+(10-flag)*i)%11==0)
		{
		    cout<<i;
		    ok=1;
		}
	    //最后一位为10也就是x的情况
	    if(ok==0&&flag;==9)
		if((sum+10)%11==0)
		{
		    cout<<"X";
		    ok=1;
		}
	    //如果都不是
	    if(ok==0)
		cout<<"-1";
	}