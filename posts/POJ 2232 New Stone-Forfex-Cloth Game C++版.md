<!--
.. title: POJ 2232 New Stone-Forfex-Cloth Game C++版
.. slug: poj-2232
.. date: 2013-04-07T05:36:24+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2232](http://poj.org/problem?id=2232)


一个新的石头剪刀布游戏，大概的玩法是，大家选择一个，然后坐成一圈，任意选择一个人，逆时针比较，输的淘汰，平局算这个人赢，问可能由多少人可以赢！

算法不难，不是我子集想出来的，比如，由F C S那么这三个可以通过F可以让C先打败S在打败C，其他同理。

如果却少一种，比如只有F C那么C必输，每一个F都可能赢，其他同理，

如果缺少两种，都是一样的，那么谁都能赢！

由于三种可以交换，我在判断是时候就用了个小技巧，没有一一判断，不过先开始没有加break，导致输出了三遍！

题目不难，思路一说就简单的，

代码如下：

	:::cpp
	/*Problem: 2232		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	using namespace std;

	int main()
	{
		int n,i,f,c,s;
		char a[1001];
		while(cin>>n)
		{
			f=0;c=0;s=0;
			for(i=0;i<n;i++)
			{
				cin>>a[i];
				switch(a[i])
				{
					case 'F':f++;break;
					case 'C':c++;break;
					case 'S':s++;break;
				}
			}
			for(i=0;i<3;i++)
			{
				if(f&&c;&&s;)
				{
					cout<<n<<endl;
					break;
				}	
				else if(f&&c;==0&&s;==0)
					cout<<n<<endl;
				else if(f&&c;&&s;==0)
					cout<<f<<endl;
				int temp=f;
				f=c;c=s;s=temp;
			}
		}
	}