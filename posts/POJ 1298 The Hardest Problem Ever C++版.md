<!--
.. title: POJ 1298 The Hardest Problem Ever C++版
.. slug: poj-1298
.. date: 2013-04-07T07:51:23+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1298](http://poj.org/problem?id=1298)


简单模拟加密算法，不过我试了下用scanf("%[^n]",ch)不行，一定要用gets(ch)，这点我有点不理解，以后研究下



代码如下

	:::cpp
	/***************************************
	Problem: 1298		User: awq123
	Memory: 196K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char ch[500];
		int len,i;
		while(gets(ch))
		{
			if(strcmp(ch,"START")==0||strcmp(ch,"END")==0)
				continue;
			if(strcmp(ch,"ENDOFINPUT")==0)
				break;
			len=strlen(ch);
			for(i=0;i<len;i++)
				if(ch[i]>='A'&&ch;[i]<='Z')
					ch[i]=(ch[i]-65+26-5)%26+65;
			cout<<ch<<endl;
		}
	}