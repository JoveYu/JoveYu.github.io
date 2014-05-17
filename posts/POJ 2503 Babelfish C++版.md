<!--
.. title: POJ 2503 Babelfish C++版
.. slug: poj-2503
.. date: 2013-04-07T08:55:56+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=2503](http://poj.org/problem?id=2503)


题目给出大量的字典数据，然后在一空行后开始查询，要是用c语言就麻烦点，我偷了点懒，用STL的map做的，对于这样的一一对应的关系map还是很好用的，只是听说，在时间上会长点

思路就不解释了，上代码

	:::cpp
	/*Problem: 2503		User: awq123
	**Memory: 10516K		Time: 1125MS
	**Language: C++		Result: Accepted
	*/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <string>
	#include <map>
	using namespace std;


	int main()
	{
		map <string,string>mymap;
		string line;
		while (getline(cin,line))
		{
			if(line.length()==0)
				break;
			string a="",b="";
			bool flag=0;
			for(unsigned int i=0;i<line.length();i++)
			{
				if(line[i]==' ')
					flag=1;
				else
				{
					if(flag)
						b+=line[i];
					else
						a+=line[i];
				}
			}
			mymap[b]=a;
		}
		while(cin>>line)
		{
			if(mymap[line].length())
				cout<<mymap[line]<<endl;
			else
				cout<<"eh"<<endl;
		}

	}