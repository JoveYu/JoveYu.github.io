<!--
.. title: POJ 1363 Rails C++版
.. slug: poj-1363
.. date: 2013-04-07T08:38:37+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1363](http://poj.org/problem?id=1363)


题目先开始没有读清楚，结果思路一直是错的，解释下题意，一列顺序为1，2，3。。的列车通过一个中转站后是否能变为给出的序列，其中这个站，类似于那个栈，利用他暂时保留车辆，以调整顺序，比如
3辆车想变为1，3，2，那么2号进站，等三号出来后在从站里出来跟在3后面

天然的栈运用，我们用stack模拟中转站中存的车辆

依次比较出来的序列是否和进站的一样或者于栈顶的一样，否则将这车推入栈，等待后面的判断，最后要是可以的话，栈里的元素应该全部推出！我用i计数进站的车，用k计数出站的出车，模拟这样的中转。

代码如下：

	:::cpp
	/*Problem: 1363		User: awq123
	**Memory: 264K		Time: 266MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <stack>
	using namespace std;

	int main()
	{
		int d[1005],n,i;
		stack <int> s;
		while(cin>>n&&n;)
		{
			while(cin>>d[1]&&d;[1])
			{
				for(i=2;i<=n;i++)
				{
					cin>>d[i];
				}
				int i=1,k=1;
				while(i<=n+1&&k;<=n)
				{
					if (d[k]==i)
					{
						i++;k++;
					}
					else if (s.empty()==0&&d;[k]==s.top())
					{
						s.pop();
						k++;
					}
					else
					{
						s.push(i);
						i++;
					}
				}
				if(s.empty())
					cout<<"Yes"<<endl;
				else
					cout<<"No"<<endl;
				while(s.empty()==0)
					s.pop();
			}
			cout<<endl;
		}
	}