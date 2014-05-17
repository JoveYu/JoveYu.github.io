<!--
.. title: POJ 1026 Cipher C++版
.. slug: poj-1026
.. date: 2013-04-07T07:58:58+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1026](http://poj.org/problem?id=1026)


这个题给我们了字符串的对应关系，要求我们根据变换顺序转换n次输出字符串，如：  
3  
2 1 3  
1 abc  
那么就是abc经过一次转换，根据对应关系得bac。  

我们来分析下题目的例子  
1 2 3 4 5 6 7 8 9 10  
4 5 3 7 2 8 1 6 10 9  
那么原来第一位上的数经过一次变换就到了第四位上，其他同理，我们要是纯模拟，一定会超时。我们来观察下数列变化，其实变化时一个循环，只是每一位的循环长度不同，  
1--->4--->7--->1  
2--->5--->2  
那么我们用转换次数取余这个循环数，可以省去很多的时间。细节见注释！  

代码如下：

	:::cpp
	/***************************************
	Problem: 1026		User: awq123
	Memory: 244K		Time: 141MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <algorithm>
	using namespace std;

	int main()
	{
		int key[205],t[205];
		int n,m,i,j;
		char ch[500],ans[500];
		while(cin>>n&&n;)
		{
			for(i=1;i<=n;i++)//输入对应关系
				cin>>key[i];
			for(i=1;i<=n;i++)//测量该位循环长度
			{
				int temp=key[i];
				int count=1;
				while(temp!=i)//是否循环
				{
					temp=key[temp];
					count++;
				}
				t[i]=count;
			}
			while(cin>>m&&m;)
			{
				getchar();//这句一定不能掉，我调试的时候发现ch前多读入了一个空格。
				cin.getline(ch,n+1);
				int len=strlen(ch);
				for(i=len;i<n;i++)//补齐位数不够的空格
					ch[i]=' ';
				ch[n]='\00';//加上结束符
				for(i=1;i<=n;i++)//处理字符串
				{
					int temp=i;
					for(j=1;j<=m%t[i];j++)//寻找对应关系
						temp=key[temp];
					ans[temp-1]=ch[i-1];
				}
				ans[n]='\00';//加上结束符
				cout<<ans<<endl;
			}
			cout<<endl;//这句害我wa了半天
		}
	}
