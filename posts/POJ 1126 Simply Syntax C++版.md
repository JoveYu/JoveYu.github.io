<!--
.. title: POJ 1126 Simply Syntax C++版
.. slug: poj-1126
.. date: 2013-04-07T05:16:25+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1126](http://poj.org/problem?id=1126)


这个题给出几条语法要求，让我们判断词汇是否符合语法要求，大概可以描述成：
1.单个从p到z的字符满足条件；
2.如果字符串s（注意是字符串，我现开始以为是字母s）满足条件，Ns也满足条件。
3.如果字符串s和字符串t满足条件，Cst,Dst,Est,Ist也满足条件。

思路是这样的，给每一个字母一个值，由后往前，类似递归的查看方式，倒推出这一个字符串是否符合，若结果为-1，则正好满足题目要求的嵌套方式，输出yes。

代码如下：

	:::cpp
	/*Problem: 1126		User: awq123
	**Memory: 208K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	using namespace std;
	int main()
	{
	    char data[260];
	    int i,top,list[260];
	    bool flag;
	    while(cin>>data)
	    {
		top=strlen(data)-1;
		flag=1;
		for(i=0;i<=top;i++)
		{
		    if(data[i]=='N')
		        list[i]=1;
		    else if(data[i]=='C'||data[i]=='D'||data[i]=='E'||data[i]=='I')
		        list[i]=2;
		    else if(data[i]>='p'&&data;[i]<='z')
		        list[i]=-1;
		    else 
		    {    
		        flag=0;
		        break;
		    }
		}
		if(flag==0)
		    cout<<"NO"<<endl;
		else
		{
		    int sum=0;
		    while(top>=0)
		    {
		        sum+=list[top];
		        if(sum>0)
		            break;
		        if(list[top]>0)
		            sum--;
		        top--;
		    }
		    if(sum==-1)
		        cout<<"YES"<<endl;
		    else 
		        cout<<"NO"<<endl;
		}
	    }
	}