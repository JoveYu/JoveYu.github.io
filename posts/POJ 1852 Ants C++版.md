<!--
.. title: POJ 1852 Ants C++版
.. slug: poj-1852
.. date: 2013-04-07T09:49:19+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1852](http://poj.org/problem?id=1852)

这个题有点弯转，解释下题意，在一个长度为len的木条上分布着num个蚂蚁，他们可以以相同的速度向任意两个方向走，每碰到一个蚂蚁，反向移动，问蚂蚁全部走完，所需要的最短时间和最长时间，之前被转向迷惑了，其实速度相同，蚂蚁也相同，两个同时转向相当与穿过去了，那么我们只要考虑每个蚂蚁，离开木条的时间就可以了，这里我将近路径和min比较，远路径和max比较，然后输出！

思路比较简单，但是这题启发我们，分析题目的时候应该主要要排除一些干扰条件，脑筋要会转弯！

代码如下：

	:::cpp
	/*Problem: 1852		User: awq123
	**Memory: 220K		Time: 625MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>

	using namespace std;

	int main()
	{
	    int n,len,num,min,max,tmp;
	    cin>>n;
	    while(n--)
	    {
		cin>>len>>num;
		max=0,min=0;
		while(num--)
		{
		    cin>>tmp;
		    if(tmp>len-tmp)
		        tmp=len-tmp;
		    if(tmp>min)
		        min=tmp;
		    if(len-tmp>max)
		        max=len-tmp;
		}
		cout<<min<<" "<<max<<endl;
	    }
	}
