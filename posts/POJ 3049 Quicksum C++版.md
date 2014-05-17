<!--
.. title: POJ 3049 Quicksum C++版
.. slug: poj-3049
.. date: 2013-04-07T08:41:09+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=3049](http://poj.org/problem?id=3049)


上学了，时间不多，先水一把！
题目给出了算法，其中A代表1，依此类推，注意含空格的字符串的输入，我们一般用gets，其实注释掉的那句也可以的！


代码如下：

	:::cpp
	/*Problem: 3094		User: awq123
	**Memory: 244K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		char str[300];
		while (1)
		{
			//scanf("%[^n]n",str);
			gets(str);
			if(str[0]=='#')
				break;
			int i,sum=0,len=strlen(str);
			for(i=0;i<len;i++)
			{
				if(str[i]!=' ')
					sum+=(str[i]-'A'+1)*(i+1);
			}
			cout<<sum<<endl;
		}

	}