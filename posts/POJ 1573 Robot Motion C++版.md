<!--
.. title: POJ 1573 Robot Motion C++版
.. slug: poj-1573
.. date: 2013-04-07T04:55:34+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1573](http://poj.org/problem?id=1573)

题目的意思很容易从图中看出，题目要求机器人根据每个字母的方向行走，直到走出矩阵，或者进入循环，我的思路是利用map数组记录矩阵字母，用getv函数和step数组配合找出此时该怎么走，利用mapnum数组给经过的路标号，因为我初始化时所有的数都是0再遇到不是0的数则说明循环，而且利用这个路标号可以很方便的求出循环长度。

做题完成了后完美显示给出的两个例子，但是一直WA我就郁闷了，当时的代码其实只有一点区别，就是

	:::cpp
	t=0;

and

	:::cpp
	cout<<t<<" step(s) to exit"<<endl;

and

	:::cpp
	cout<<mapnum[y][x]<<" step(s) before a loop of "<<t-mapnum[y][x]<<" step(s)"<<endl;

这样的其实没什么太大的问题只是我后来查看mapnum数组的时候，起步点的值会是0，这样的话如果再次经过起始点就会判断错误，修改t的初始值为1然后修改后面的t的输出值AC，看来其中的测试数据应该有经过起始点的吧！

代码如下：

	:::cpp
	/*Problem: 1573		User: awq123
	**Memory: 260K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstring>
	using namespace std;

	int getv(char ch)
	{
		switch(ch)
		{
		case 'N': return 0;
		case 'E': return 2;
		case 'S': return 4;
		case 'W': return 6;
		}
	}

	int main()
	{
		int step[8]={0,-1,1,0,0,1,-1,0};
		char map[50][50];
		int mapnum[50][50];
		int x,y,n,i,j,r,c,t,temp;
		while(cin>>r>>c>>n&&r;!=0&&c;!=0&&n;!=0)
		{
			x=n;
			y=1;
			t=1;
			memset(map,0,sizeof(map));
			memset(mapnum,0,sizeof(mapnum));
			for(j=1;j<=r;j++)
				for(i=1;i<=c;i++)
					cin>>map[j][i];
			while(1)
			{
				if(x==0||x==c+1||y==0||y==r+1)
				{
					cout<<t-1<<" step(s) to exit"<<endl;
					break;
				}
				else if(mapnum[y][x]!=0)
				{
					cout<<mapnum[y][x]-1<<" step(s) before a loop of "<<t-mapnum[y][x]<<" step(s)"<<endl;
					break;
				}
				mapnum[y][x]=t++;
				temp=getv(map[y][x]);
				x+=step[temp];
				y+=step[temp+1];
			
			}

		}

	}