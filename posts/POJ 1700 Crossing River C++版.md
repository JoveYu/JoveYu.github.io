<!--
.. title: POJ 1700 Crossing River C++版
.. slug: poj-1700
.. date: 2013-04-07T05:23:00+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1700](http://poj.org/problem?id=1700)


题意就是我们以前听过的过桥的故事。但是这里时过河，一条船每次只能过两个人，问过去的最小路程

查阅相关资料，利用贪心算法解题，具体思路时这样的：

设i=人数；
i<3时，直接过去；
i=3时，设速度为ABC升序，那么A护送C过去，再回来，再送B过去最短，也就是t[0]+t[1]+t[2]
i>=4时，设最快的A，次快的B，次慢的C，最慢的D，
（1）如果用最小的来送:d+a+c+a+b=d+c+b+2a
（2）如果先让最小的两个过河,再让其中一个回来,
让最大的两个过河,再让前一步过去留下的那个回来,
再让最小的2个过河
也就是说小的两个过去2次,再单独回来一次.
2b+b+a+d=d+3b+a 
比较两种方法，选小的；

我们分析每次的情况人数从N开始倒数回去，每次选取最优解，则得到的时最小值！

代码如下

	:::cpp
	/*Problem: 1700		User: awq123
	**Memory: 256K		Time: 16MS
	**Language: C++		Result: Accepted
	*/
	#include <cstdio>
	#include <iostream>
	#include <cstring>
	#include <algorithm>
	using namespace std;
	int main()
	{
		int m,n,i,max,t[1001];
		cin>>m;
		while(m--)
		{
			cin>>n;
			for(i=0;i<n;i++)
				cin>>t[i];
			max=0;
			sort(t,t+n);
			for(i=n-1;i>2;i-=2)
				if(t[0]+2*t[1]+t[i]>2*t[0]+t[i]+t[i-1])
					max+=2*t[0]+t[i]+t[i-1];
				else
					max+=t[0]+2*t[1]+t[i];
			if(i==2)
				max+=t[0]+t[1]+t[2];
			else if(i==1)
				max+=t[1];
			else
				max+=t[0];
			cout<<max<<endl;
		}
	}
