<!--
.. title: POJ 1132 Border C++版
.. slug: poj-1132
.. date: 2013-04-07T05:18:58+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1132](http://poj.org/problem?id=1132)


一个简单的模拟题，这个题目题意很容易理解，依据给出的坐标，按照给出的线路行走，然后输出围绕这个线路的方块。

我们可以拿笔纸画一画。
E就是这个点的右下方的那个方块，N就是这个点右上方的那个方块，W就是左上方的那个方块，S就是左下方的那个方块。

这样看来我们可以清楚的发现，根据字符串的每一个字母都能确认一个方块那么依次扫描就是了，其中遇到重复的也不要紧。

先开始一直PE我就是不懂，还数了半天点点，也对啊。后来才看到题目中这样一句话



>Output a blank line after each bitmap.

这才AC，尴尬啊！！！

代码如下：

	:::cpp
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	using namespace std;
	int main()
	{
		char map[33][33];
		char ch[1000];
		int n,x,y,len,i,t,j;
		cin>>n;
		for(t=1;t<=n;t++)
		{
			memset(map,'.',sizeof(map));
			cin>>x>>y;
			cin>>ch;
			len=strlen(ch);
			for(i=0;i<len;i++)
			{
				switch(ch[i])
				{
					case 'E':map[++x][y]='X';break;
					case 'N':map[x+1][++y]='X';break;
					case 'W':map[x--][y+1]='X';break;
					case 'S':map[x][y--]='X';break;
					default:break;	
				}
			}
			cout<<"Bitmap #"<<t<<endl;
			for(i=32;i>0;i--)
			{
				for(j=1;j<33;j++)
					cout<<map[j][i];
				cout<<endl;
				
			}
			cout<<endl;
		}
	}
