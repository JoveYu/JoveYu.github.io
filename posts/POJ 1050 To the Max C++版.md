<!--
.. title: POJ 1050 To the Max C++版
.. slug: poj-1050
.. date: 2013-04-07T06:02:21+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1050](http://poj.org/problem?id=1050)


题目要求我们求出和最大的子矩阵。

我输入数据的时候，做了个小处理，就是用这个坐标表示到原点的矩阵和，这样后面只要计算对角线点的值就行了，不过这题for语句真的好多，这样的矩阵题还是比较熟的。

不多解释，不难！

代码如下：

	:::cpp
	/*Problem: 1050		User: awq123
	**Memory: 288K		Time: 94MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	int main()
	{
		//freopen("input.txt", "r", stdin);
		int d[101][101];
		memset(d,0,sizeof(d));
		int i,j,x,y,n,temp,max=0;
		cin>>n;
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
			{
				cin>>temp;
				d[i][j]=temp+d[i-1][j]+d[i][j-1]-d[i-1][j-1];
			}
		for(i=0;i<=n;i++)
			for(j=0;j<=n;j++)
				for(x=i;x<=n;x++)
					for(y=j;y<=n;y++)
					{
						temp=d[x][y]-d[x][j]-d[i][y]+d[i][j];
						if(temp>max)
							max=temp;
					}
		cout<<max<<endl;	

		
	
	}
