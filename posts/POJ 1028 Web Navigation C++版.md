<!--
.. title: POJ 1028 Web Navigation C++版
.. slug: poj-1028
.. date: 2013-04-07T04:31:12+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1028](http://poj.org/problem?id=1028)

1028的确是个水题，算法已经给出，仅要求你根据题意模拟浏览器的访问，前进，后退。
我查阅相关解题报告，感觉最好的思路就是STL中的stack，天然的浏览记录，第一次用stack，有点小激动。

其中，几个重要的函数：

>ush()--将数据推入堆栈
>pop()--推出堆栈
>top()--查看堆栈最上方数据
>empty()--检测堆栈是否为空


代码如下：

	:::cpp 
	/*Problem: 1028		User: awq123
	**Memory: 244K		Time: 0MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <string>
	#include <algorithm>
	#include <stack>

	using namespace std;

	int main()
	{
		stack<string> forward;
		stack<string> backward;
		string now="http://www.acm.org/",cmd;
		while(1)
		{
			cin>>cmd;
			if(cmd=="VISIT")
			{
				backward.push(now);
				cin>>now;
				cout<<now<<endl;
				while(!forward.empty()) forward.pop();
			}
			if(cmd=="BACK")
			{
				if(backward.empty())
					cout<<"Ignored"<<endl;
				else
				{
					forward.push(now);
					now=backward.top();
					cout<<now<<endl;
					backward.pop();
				}
			}
			if(cmd=="FORWARD")
			{
				if(forward.empty())
					cout<<"Ignored"<<endl;
				else
				{
					backward.push(now);
					now=forward.top();
					cout<<forward.top()<<endl;
					forward.pop();
				}
			}
			if (cmd=="QUIT")
				break;
		}

	}