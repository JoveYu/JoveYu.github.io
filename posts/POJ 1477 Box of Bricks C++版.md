<!--
.. title: POJ 1477 Box of Bricks C++版
.. slug: poj-1477
.. date: 2013-04-07T08:39:15+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1477](http://poj.org/problem?id=1477)


题目给出一些高度的木箱，问至少移动多少步，可以移动到同以高度！水题，没什么好说的！


代码如下：

	:::cpp
	/*Problem: 1477		User: awq123
	**Memory: 260K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		int t,i,j=1,d[105];
		while(cin>>t&&t;)
		{
			int sum=0,ans=0;
			for(i=0;i<t;i++)
			{
				cin>>d[i];
				sum+=d[i];
			}
			sum/=t;
			for(i=0;i<t;i++)
			{
				int temp=sum-d[i];
				ans+=(temp>0?temp:-temp);
			}
			cout<<"Set #"<<j<<endl;
			cout<<"The minimum number of moves is "<<ans/2<<"."<<endl;
			cout<<endl;
			j++;
		}
	}