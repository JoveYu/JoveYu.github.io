<!--
.. title: C语言打字练习程序（半成品）
.. slug: c-input-test
.. date: 2013-04-07T03:57:43+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

今天看到个文本输入程序  很有启发 加以修改成了一个打字游戏 可是我运行的时候总是无法正确识别键盘输入今天不早了改天有时间再修改先晒下代码

	:::cpp
	/*C语言打字游戏
	**键盘读入不正确
	**2011-6-8
	*/
	#include<stdio.h>
	#include<conio.h>
	#include<windows.h>
	#include<stdlib.h>
	#include <time.h>
	#include <process.h> 
	#include<string.h>

	int pos;
	int level=1000;
	int count;
	int num;
	int score;
	int Down;
	int intst;
	int isRun;
	int isOver;
	int isRight;
	int isFull;
	int map[11][11];

	int Build_char()
	{
		int res;
		res=rand()%2?(65+rand()%26):(97+rand()%26);
		return res;
	}

	int Build_Pos()
	{
		int res;
		res=rand()%10;
		return res;
	}

	void Listener(PVOID pvoid)    //监视输入的线程函数
	{
		char temp;
		while(1)
		{   
			while(!_kbhit())
			temp=getchar();
			if(temp==num)
			{
				score+=10;
				isRight=1;
				if(score==100)
				{
					isFull=1;
					temp='0';
				}
			}
			if(temp=='1')
				isRun=1-isRun;
			if(temp=='0')
			{
				isOver=1;
				return;
			}
		}
	}

	void Repaint(PVOID pvoid)//重画
	{
		int i,j;
		while(1)
		{
			if(isOver)break;
				while(!isRun);
					system("cls");
			printf(" 时间：%d  得分：%d  1---暂停，0---退出n--------------------------------------------------------n",time(0)-intst,score);
			for(i=0;i<=10;i++)
			{
				for(j=0;j<=10;j++)
					if(map[i][j])
						printf("%c",map[i][j]);
					else
						printf(" ");
				printf("n");
			}
			printf("--------------------------------------------------------n");
		}

	}

	void Calculate()
	{
		memset(map,0,sizeof(map));//全屏清零
		map[count][pos]=num;
	}

	void Run()
	{
		int flag=1;
		int cnt;
		while(flag)//出现数字
		{ 
			cnt=Down;
			count=1;
			pos=Build_Pos();
			num=Build_char();
			while(cnt&&!isRight)//数字下掉
			{   
				if(isOver)return;
					while(!isRun);
						Calculate();
				count++;
				cnt--;
				Sleep(level);
			}
		isRight=0;
	    }
	}

	void init()
	{
		score=0;
		isOver=0;
		Down=10;
		isFull=0;
		isRun=1;
		isRight=0;
	    intst=time(0);
	    memset(map,0,sizeof(map));
	}

	int  main()
	{
		init();
		_beginthread(Listener,0,NULL); //开线程
		_beginthread(Repaint,0,NULL); //开线程
		Run();
		if(isFull)
			printf("祝贺你，你赢了n");
		//system("cls");
		return 0;
	 }