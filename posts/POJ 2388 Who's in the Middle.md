<!--
.. title: POJ 2388 Who's in the Middle
.. slug: poj-2388
.. date: 2013-04-07T04:16:03+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2388](http://poj.org/problem?id=2388)

这个题目是基础排序的题目，主要利用数组的排序，我查阅相关资料，找到个数组排序的函数sort然而代码中的vector，维基里是这么解释的：
>Vector 是一个动态数组（dynamic array）。在数据结构里，它被称之为容器（container），除此之外，其他则包括 set、map、…等等。由于它的实做是一个类模板，亦即泛型框架，所以它可以放置一般的数据型态，也可以放置用户自定义的数据型态，例如：它可以是一个放置整数（int）型态的 vector、也可以是一个放置字符串（char 或 string）型态的 vector、甚至可以放置用户自定类（user-defined class）的 vector。<
c++中灵活利用函数能使程序本身简洁度降到最低，也许poj应该禁用某些函数，让算法得到更大的利用

代码很简单多亏了sort函数，代码如下：


	:::cpp
	/*Problem: 2388		User: awq123
	**Memory: 296K		Time: 47MS
	**Language: C++		Result: Accepted
	*/
	#include<iostream>
	#include<vector>
	#include<algorithm>
	using namespace std;
	int main()
	{
		int i, n;
		cin>>n;
		vector<int>num(n);
		for(i=0;i<n;i++)
			cin>>num[i];
		sort(num.begin(),num.end());
		cout<<num[n/2]<<endl; 
	return 0;
	}