<!--
.. title: POJ 1318 Word Amalgamation C++版
.. slug: poj-1318
.. date: 2013-04-07T05:04:26+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

一个半成品，

花了我一下午，但是还是有点小问题，累了，睡觉去的，改天继续。

问题就是搜索顺序不对，我是按顺序搜索的，他是排完序搜索的，结果无问题，在G++下编译，

懒得解释题目了，郁闷  

代码如下：

	:::cpp
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm> 
	using namespace std;

	typedef struct node
	{
		char c[7];
		char y[7];
		int n;
	}NODE;

	/*int cmp(const void *a,const void *b)
	{
	    return strcmp( (*(node *)a)->str , (*(node *)b)->str );
	}*/

	int main()
	{
		//freopen("input.txt", "r", stdin);
		NODE node[101];
		string str;
		int t=0,i,j,temp,flag;
		while(cin>>str&&str;!="XXXXXX")
		{
			node[t].n= str.length();
			for(i=0;i<node[t].n;i++)
			{
				node[t].y[i]=str[i];
				node[t].c[i]=str[i];
			}
			sort(&node;[t].c[0],&node;[t].c[str.length()]);
			t++;
		}
		//qsort(node,t,sizeof(node[0]),cmp);
		while(cin>>str&&str;!="XXXXXX")
		{
			flag=0;
			sort(&str;[0],&str;[str.length()]);
			for(i=0;i<t;i++)
			{
				if(int(str.length())==node[i].n)
				{
					temp=1;
					for(j=0;j<node[i].n;j++)
					{
						if(node[i].c[j]!=str[j])
						{
							temp=0;
							break;
						}
					}	
					if(temp==1)
					{
						cout<<node[i].y<<endl;
						flag=1;
					}
				}
			}
			if(flag==0)
				cout<<"NOT A VALID WORD"<<endl;
			cout<<"******"<<endl;
		
		}
	}