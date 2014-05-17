<!--
.. title: POJ 1057 FILE MAPPING C++版
.. slug: poj-1057
.. date: 2013-04-07T07:58:38+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

题目链接：[http://poj.org/problem?id=1057](http://poj.org/problem?id=1057)


解释下题意，输入文件系统，dir*就是定义一个文件夹，]就是结束这个文件夹的定义，其中我们观察第2个例子可以看出，每个文件夹里的文件要排序输出，这点要注意

查阅了几篇文章，看到个用vector做的，其中利用了string，不禁感叹，用string表示字符串数组真实太方便了，其中排序，量长度，大小都有函数，总的来说思路算是DFS但是不是搜索，利用递归输入文件，每一次输入新的文件夹，递归输入一次，正好符合题目的输入格式，输出的时候也是，只不过多了个n表示数据层次，方便输出分隔符，也就是|。具体思路看注释把！

至于为什么有两个string头文件，因为我用g++编译的但是用的c++提交，其中这个是没有c的！

代码如下：

	:::cpp
	/***************************************
	Problem: 1057		User: awq123
	Memory: 212K		Time: 0MS
	Language: C++		Result: Accepted
	***************************************/
	#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <string>
	#include <algorithm>
	#include <vector>
	using namespace std;

	struct node//文件夹结构体
	{
		vector<string> file;//包含的文件
		vector<node> dir;//包含的文件夹
		string name;//文件夹的名字
	};

	node root;//这句可以不要但是好像会多花点时间

	bool end=0;//标记是否结束

	void fileinput(node& now)//输入文件系统
	{
		string temp;
		while (1)
		{
			cin>>temp;
			if (temp[0]=='#')
			{
				end=1;
				break;
			}
			else if(temp[0]=='f')//如果是文件推入文件序列
				now.file.push_back(temp);
			else if(temp[0]=='d')//如果是文件夹
			{
				node d;//定义一个新的结构体
				d.name=temp;//新文件夹名称
				fileinput(d);//输入新文件夹内容
				now.dir.push_back(d);//将新文件夹推入文件夹序列
			}
			else
				break;
		}
		sort(now.file.begin(),now.file.end());//对文件夹里的文件名称进行升序排列
	}

	void fileprint(node& now,int n)
	{
		int i,j;
		for(i=0;i<n;i++)//输入包含的文件夹名
			cout<<"|     ";
		cout<<now.name<<endl;
		for(i=0;i<(int)now.dir.size();i++)//搜索输出子目录
			fileprint(now.dir[i],n+1);
		for(i=0;i<(int)now.file.size();i++)//输出包含文件名
		{
			for(j=0;j<n;j++)
				cout<<"|     ";
			cout<<now.file[i]<<endl;
		}
	}

	int main()
	{
		//freopen("Input.txt", "r", stdin);
		int i;
		for(i=1;;i++)
		{
			node root;//这句一定不能掉，算是root的初始化
			root.name="ROOT";
			fileinput(root);
			if(end)
				break;
			cout<<"DATA SET "<<i<<":"<<endl;
			fileprint(root,0);
			cout<<endl;
		}
	}
