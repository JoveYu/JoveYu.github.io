<!--
.. title: POJ 1226 Substrings C++版
.. slug: poj-1226
.. date: 2013-04-07T07:35:16+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1226](http://poj.org/problem?id=1226)


又一个LCS的题，不过这个题范围扩大到了这个字符串，和他的逆向字符串。

讲下思路，先输入字符串找出最短的一个，依次枚举每一种长度，以及这种长度下，每一种子串是否符合所有字符串，若有则输出，没有则最后输出0，其中逆向字符串花了我好多时间，不知道怎么表示，最后用另一个字符串拷贝过来的，

这个题我又学会了一个函数

	:::cpp
	const char * strstr ( const char * str1, const char * str2 );
	      char * strstr (       char * str1, const char * str2 );

在str1里搜索str2，如果找到返回指针，找不到返回NULL



题目不难，要细心，还有什么i,j,k的关系一定要搞清楚，我先开始就是数据弄混了

代码如下：

	:::cpp
	/***************************************
	Problem: 1226		User: awq123
	Memory: 260K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		char d[105][105]，min[105],str1[105],str2[105];
		int t,n,i,j,k,len,flag;
		cin>>t;
		while(t--)
		{
			len=200;
			flag=0;
			cin>>n;
			for(i=0;i<n;i++)
			{
				cin>>d[i];
				if((int)strlen(d[i])<len)
				{
					len=strlen(d[i]);
					strcpy(min,d[i]);
				}
			}
			for(i=len;i>=1&&flag;==0;i--)
			{
				for(j=0;j<=len-i&&flag;==0;j++)
				{
					for(k=0;k<i;k++)
					{
						str1[k]=min[j+k];
						str2[i-k-1]=min[j+k];
					}
					str1[i]='\00';
					str2[i]='\00';
					for(k=0;k<n;k++)
						if(strstr(d[k],str1)==NULL&&strstr;(d[k],str2)==NULL)
							break;
					if(k==n)
					{
						cout<<i<<endl;
						flag=1;
					}
				}
			}
			if(flag==0)
				cout<<0<<endl;
		}
	}