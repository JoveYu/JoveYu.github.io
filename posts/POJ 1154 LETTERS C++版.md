<!--
.. title: POJ 1154 LETTERS C++版
.. slug: poj-1154
.. date: 2013-04-07T04:46:13+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1154](http://poj.org/problem?id=1154)

这个题目就是要求你从左上角开始在不经过同样字母的前提下能走的最大路程。
查阅了别人的解题报告，可以穷举四条线路，但是我发现了一个不错的思路，代码是这样的：

	:::cpp
	int step[8] = {1,0,-1,0,0,1,0,-1}; 

	for( int k=0; k<8; k+=2)

这样就解决的四个方向的穷举，这个启发还是很大的，我本来想也许用4个for语句的，但是不好下手，他们管这种搜索方法叫DFS，改天研究下，这样一个代码也算是递归了吧
先开始错了一只不知道什么问题，当时num数组定义的num[26]后来发现其实A对应的是num[1]不是num[0]导致Z无法识别，后来改了通过
代码如下：

	:::cpp 
	/*Problem: 1154		User: awq123
	**Memory: 268K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	using namespace std;

	int x,y,temp,tempmax,str[100][100],num[27];
	int step[8] = {1,0,-1,0,0,1,0,-1}; 

	void DFS(int i, int j)
	{
		for( int k=0; k<8; k+=2)
		{
			int a = i+step[k];  
			int b = j+step[k+1];  
			if(a>=1&&a;<=y&&b;>=1&&b;<=x&&!num[str[a][b]] )  
			{  
				num[str[a][b]] = 1;  
				temp++;  
				DFS(a,b);  
				if( temp > tempmax )  
					tempmax = temp;  
				temp--;  
				num[str[a][b]] = 0;  
			}  
		}
	}
	int main()
	{
		char s[100];
	
		while( cin >> y >> x )
		{
			temp=1,tempmax=1;
			memset(num,0,sizeof(num)); 
			getchar(); 
			/*这条getchar我还是不理解但是不加就会造成数据少输入一行， */
			for(int i=1; i<=y; i++)
			{
				gets(s);
				for(int k=1; k<=x; k++)
					str[i][k] = s[k-1] -'A' + 1;
			}
			num[str[1][1]] = 1;
			DFS(1,1);
			cout<<tempmax<<endl;
		}

	}