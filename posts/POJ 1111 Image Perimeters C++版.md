<!--
.. title: POJ 1111 Image Perimeters C++版
.. slug: poj-1111
.. date: 2013-04-07T04:58:50+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1111](http://poj.org/problem?id=1111)

题意是先输入4个数，前两个分别代表输入矩阵的行和列，后两个数是起始点的坐标，然后输入字符矩阵，来判断与坐标点八方向相连的点组成的图形的边长。

看到个说是用DFS但是我看了下算法，与DFS还是有区别的，我用map来记录字符数组，用mapnum数组来记录是否访问过，dir数组来实现8方向扫描，具体搜索算法，见注释把，应该看的懂，呵，尤其是何时增加计数的判断条件，有点麻烦。

代码如下

	:::cpp
	/*Problem: 1111		User: awq123
	**Memory: 256K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	using namespace std;

	char map[21][21];
	int mapnum[21][21];
	int dir[16]={1,1,1,0,1,-1,0,-1,-1,-1,-1,0,-1,1,0,1};
	int r,c,a,b,sum;
	void search(int a,int b)
	{
		int x,y;
		mapnum[a][b]=1;
		for(int i=0;i<16;i+=2)
		{
		x=a+dir[i];
		y=b+dir[i+1];
		if(x>=1&&x;<=r&&y;>=1&&y;<=c)//扫描点不越界
			{
				if(map[x][y]=='X'&&mapnum;[x][y]==0)//未被搜索
					search(x,y);
				else if(map[x][y]=='.'&&(x==a||y==b))//在上下左右方向 计数+1
					sum++;
			}
			else if(x==a||y==b)//在上下左右方向越界的话 计数+1
				sum++;
		}
	}
	int main()
	{
		int x,y;
		while(cin>>r>>c>>x>>y&&r;)
		{
			memset(mapnum,0,sizeof(mapnum));
			for(int i=1;i<=r;i++)
				for(int j=1;j<=c;j++)
					cin>>map[i][j];
			sum=0;
			search(x,y);
			cout<<sum<<endl;
		}
	}
