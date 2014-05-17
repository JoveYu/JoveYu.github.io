<!--
.. title: Debug和Release之区别
.. slug: debug-and-release
.. date: 2013-04-07T04:06:17+08:00
.. tags:
.. link:
.. description:
.. type: text
-->

关于Debug和Release之本质区别的讨论本文主要包含如下内容：

1. Debug 和 Release 编译方式的本质区别

2. 哪些情况下 Release 版会出错

2. 怎样“调试” Release 版的程序

一、Debug 和 Release 编译方式的本质区别

Debug 通常称为调试版本，它包含调试信息，并且不作任何优化，便于程序员调试程序。Release 称为发布版本，它往往是进行了各种优化，使得程序在代码大小和运行速度上都是最优的，以便用户很好地使用。

Debug 和 Release 的真正秘密，在于一组编译选项。下面列出了分别针对二者的选项（当然除此之外还有其他一些，如/Fd /Fo，但区别并不重要，通常他们也不会引起 Release 版错误，在此不讨论）

Debug 版本：

/MDd /MLd 或 /MTd 使用 Debug runtime library(调试版本的运行时刻函数库)

/Od 关闭优化开关

/D "_DEBUG" 相当于 #define _DEBUG,打开编译调试代码开关(主要针对assert函数)

/ZI 创建 Edit and continue(编辑继续)数据库，这样在调试过程中如果修改了源代码不需重新编译

/GZ 可以帮助捕获内存错误

/Gm 打开最小化重链接开关，减少链接时间

Release 版本：

/MD /ML 或 /MT 使用发布版本的运行时刻函数库

/O1 或 /O2 优化开关，使程序最小或最快

/D "NDEBUG" 关闭条件编译调试代码开关(即不编译assert函数)

/GF 合并重复的字符串，并将字符串常量放到只读内存，防止被修改

实际上，Debug 和 Release 并没有本质的界限，他们只是一组编译选项的集合，编译器只是按照预定的选项行动。事实上，我们甚至可以修改这些选项，从而得到优化过的调试版本或是带跟踪语句的发布版本。

二、哪些情况下 Release 版会出错

有了上面的介绍，我们再来逐个对照这些选项看看 Release 版错误是怎样产生的

1. Runtime Library：

2. 优化：这类错误主要有以下几种：

(1) 帧指针(Frame Pointer)省略（简称 FPO ）：在函数调用过程中，所有调用信息（返回地址、参数）以及自动变量都是放在栈中的。若函数的声明与实现不同（参数、返回值、调用方式），就会产生错误————但 Debug 方式下，栈的访问通过 EBP 寄存器保存的地址实现，如果没有发生数组越界之类的错误（或是越界“不多”），函数通常能正常执行；Release 方式下，优化会省略 EBP 栈基址指针，这样通过一个全局指针访问栈就会造成返回地址错误是程序崩溃。C++ 的强类型特性能检查出大多数这样的错误，但如果用了强制类型转换，就不行了。你可以在 Release 版本中强制加入 /Oy- 编译选项来关掉帧指针省略，以确定是否此类错误。

(2) volatile 型变量：volatile 告诉编译器该变量可能被程序之外的未知方式修改（如系统、其他进程和线程）。

(3) 变量优化：优化程序会根据变量的使用情况优化变量。例如，函数中有一个未被使用的变量，在 Debug 版中它有可能掩盖一个数组越界，而在 Release 版中，这个变量很可能被优化调，此时数组越界会破坏栈中有用的数据。当然，实际的情况会比这复杂得多。与此有关的错误有：

3. _DEBUG 与 NDEBUG ：当定义了 _DEBUG 时，assert() 函数会被编译，而 NDEBUG 时不被编译。除此之外，VC++中还有一系列断言宏。这包括：

ANSI C 断言 void assert(int expression );

C Runtime Lib 断言 _ASSERT( booleanExpression );

_ASSERTE( booleanExpression );

MFC 断言 ASSERT( booleanExpression );

VERIFY( booleanExpression );

ASSERT_VALID( pObject );

ASSERT_KINDOF( classname, pobject );

ATL 断言 ATLASSERT( booleanExpression );

此外，TRACE() 宏的编译也受 _DEBUG 控制。

4. /GZ 选项：这个选项会做以下这些事

(1) 初始化内存和变量。

(2) 通过函数指针调用函数时，会通过检查栈指针验证函数调用的匹配性。（防止原形不匹配）

(3) 函数返回前检查栈指针，确认未被修改.

三、怎样“调试” Release 版的程序

1. 前面已经提过，Debug 和 Release 只是一组编译选项的差别，实际上并没有什么定义能区分二者。我们可以修改 Release 版的编译选项来小错误范围。如上所述，可以把 Release 的选项逐个改为与之相对的 Debug 选项，如 /MD 改为 /MDd、/O1 改为 /Od，或运行时间优化改为程序大小优化。注意，一次只改一个选项，看改哪个选项时错误消失，再对应该选项相关的错误，针对性地查找。这些选项在 ProjectSettings... 中都可以直接通过列表选取，通常不要手动修改。由于以上的分析已相当全面，这个方法是最有效的。

2.你也可以像 Debug 一样调试你的 Release 版，只要加入调试符号。在 Project/Settings... 中，选中 Settings for "Win32 Release"，选中 C/C++ 标签，Category 选General，Debug Info 选 Program Database。再在 Link 标签 Project options 最后加上 "/OPT:REF" (引号不要输)。
