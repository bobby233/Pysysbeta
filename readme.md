# 欢迎来到Pysys项目
Pysys是一个基于Python的突破性微型命令行系统，该系统仅为初期阶段，还有一些bug和很多不足。

# 目录
- [了解Pysys项目](https://github.com/bobby233/Pysys#了解Pysys项目)
    - [Pysys的命名](https://github.com/bobby233/Pysys#Pysys的命名)
    - [Pysys的目的](https://github.com/bobby233/Pysys#Pysys的目的)
- [使用者须知](https://github.com/bobby233/Pysys#使用者须知)
    - [如何使用](https://github.com/bobby233/Pysys#如何使用)
    - [常用功能](https://github.com/bobby233/Pysys#常用功能)
        - [`app list`——查看所有应用](https://github.com/bobby233/Pysys#app-list查看所有应用)
        - [`q`——退出](https://github.com/bobby233/Pysys#q退出)
        - [`settings`——系统设置](https://github.com/bobby233/Pysys#settings系统设置)
        - [`info`——查看信息](https://github.com/bobby233/Pysys#info查看信息)
- [开发者须知](https://github.com/bobby233/Pysys#开发者须知)
    - [如何成为开发者](https://github.com/bobby233/Pysys#如何成为开发者)
- [关于版本](https://github.com/bobby233/Pysys#关于版本)
    - [版本的命名](https://github.com/bobby233/Pysys#版本的命名)
    - [更新日志](https://github.com/bobby233/Pysys#更新日志)
        - [v0.0.1beta](https://github.com/bobby233/Pysys#v0.0.1beta)
        - [v0.0.1](https://github.com/bobby233/Pysys#v0.0.1)
        - [cmd_testv0](https://github.com/bobby233/Pysys#cmd_testv0)
        - [v0.1.0beta](https://github.com/bobby233/Pysys#v0.1.0beta)
        - [v0.1.0](https://github.com/bobby233/Pysys#v0.1.0)
        - [v0.2.0beta](https://github.com/bobby233/Pysys#v0.2.0beta)
        - [v0.2.0](https://github.com/bobby233/Pysys#v0.2.0)
        - [v0.2.1](https://github.com/bobby233/Pysys#v0.2.1)
    - [TODO](https://github.com/bobby233/Pysys#TODO)
- [交流](https://github.com/bobby233/Pysys#交流)
- [预告](https://github.com/bobby233/Pysys#预告)

# 了解Pysys项目
想要完整地使用这款微型系统，你可能需要了解一些关于它的信息，如果你并不想了解关于这方面的信息，你可以选择跳过，这对你的使用没有很大的影响。
## Pysys的命名
当你第一眼看到这个系统的名字时，你肯定已经反应过来了，这是Python和system的合并名称。确实，我们的命名方式就是这样的，我们实际上还有更深层的意义，你没有想过，以Py做开头不就是Python中的唯一一个吗？实际上，这是一个有未来的项目，我们在以后学习了更多Python知识和系统编程知识后会真正地把这个微型系统变成一个庞大的实用系统。
## Pysys的目的
在看到"sys"时，你也会明白我们的目的的，这就是一个系统，一个系统不一定要复杂，但是一定要实用，Python语言就完美地解决了这个问题，它可以使用更少的代码来做更多的事，在以后，Pysys一定会成为一个实用的系统，帮助你完成更多繁杂的琐事。

# 使用者须知
如果你想要使用这款微型系统，你一定要好好读这个须知，你会了解如何使用这款系统的。
## 如何使用
如果你不了解git，但又想要使用这个系统，你可以在终端输入以下的代码：
````
git clone git@github.com:bobby233/Pysys.git
cd Pysys
python3 Pysys.py
````
在正常情况下，Linux系统会正常地开始运行，但是Windows和macOS就会遇到一些问题，如果你遇到了问题，那么极大可能是你没有[安装git](https://git-scm.com/downloads)。
如果你是Windows，那么最后一行可能是`python Pysys.py`
## 常用功能
想要更好使用这款系统，一定不能错过系统里的功能和内置应用，这里可以查看一些常用功能。
### `app list`——查看所有应用
这是一个非常常用的功能，如果你想用一个应用，但是你又忘记了这个应用的名称，你就需要使用这个命令了，这个命令可以列出所有的app名称来帮助你使用到你想要的app。就像这样：
````
<=> app list
These are built in apps:
settings
info
dev
Pyox
Pyrandcard
Pyrandom
These are third party apps:
<=>
````
### `q`——退出
这是一个常用得不能在常用的功能，这也是一个非常重要的功能。当然，这个功能应该不需要介绍了，应该都明白。如果你在一个应用中不知道如何退出，那么很大可能可以使用这个命令。
### `settings`——系统设置
上面介绍的都是“命令”，现在开始就都是“app”，也就是“应用程序”了。分辨他们的最好方法就是看有没有进入和退出提示，比如“settings”的提示就是这样的：
````
Welcome to settings-----------------------------------------
Exit settings-----------------------------------------------
````
这也是一个很好的防伪标记，如果这一行提示的字符加起来是60个，那么你用的就是正版。  

下面开始介绍“settings”的操作：
在这个版本中，“settings”只有一个操作，就是“cpsw”，这是一个缩写，全称是“change password”更改密码，只需进入“settings”，然后输入“cpsw”就可以更改了，这是一个例子：
````
<=> settings
Welcome to settings-----------------------------------------
Type "cpsw" to change your password.
Type "info" to see the info.
What do you want to do(type "q" to quit)? cpsw
Please type your password: 0
Type your new password: 00
Change succefully
Type "cpsw" to change your password.
Type "info" to see the info.
What do you want to do(type "q" to quit)? q
Exit settings-----------------------------------------------
<=> 
````
在上面这个例子中，我们把原来的密码0更改为00，操作十分简单和容易理解。
### `info`——查看信息
这看起来是一个命令，但实际上它是**应用程序(app)**，它可以在任何app或者系统本身中查看信息，就像这样查看系统信息：
````
<=> info
Welcome to info---------------------------------------------
These are the info of Pysys:
Name: Pysys
Author: bobby233
Version: 0.0.1
Info: A breakthrough system based on Python
Exit info---------------------------------------------------
<=> 
````
它是app的最好证据就是它有**进入和退出提示**，这个app也很好理解，如果你不明白，可以自己选择几个app进行测试。
### 想要了解更多？
请期待我们的官方文档——[PysysDocument](https://github.com/bobby233/Pysys/blob/master/PysysDocument.md)

# 开发者须知
我们欢迎你成为一名Pysys开发者，如果你想要成为开发者，你一定要看看以下的须知，你会成为更优秀的开发者的。
## 如何成为开发者
想要成为开发者，你一定要会一些Python技术，你可以通过以下的方式来成为一名开发者：  
1. 制作一个Python程序，不管程序的大或小，只要证明你具有Python技术。
2. 发送你的程序至邮箱mczsjzsjz@outlook.com。
3. 等待开发者让你通过开发者测试。
4. 欢迎成为开发者！

# 关于版本
如果你想要知道版本的信息，你可能需要看这些。
## 版本的命名
这款系统的版本命名方式应该很容易理解，这是一个典型的命名：v0.0.1beta。在这个命名中v后面的第一位数字代表长期版本，这个数字只会在很大的更新才会变动；第二位数字是中期版本，这个数字基本上会在每次正常更新时变动；第三位数字是短期版本，这个数字会在每次小改版和bug修复时改动；最后的单词是各种版本的分类，有alpha/beta，分别是内部版/内测版，普通版没有后缀。
## 更新日志
### v0.0.1beta
发布时间：4/1  
更新内容：第一个版本
### cmd_testv0
发布时间：4/19  
更新内容：这是一个补丁，需要配合其他文件使用，你可以直接运行它来查看最新的cmd标准库版Pysys。**注：它不用登录或注册**
### v0.1.0beta
发布时间：5/1
更新内容：
- 修改各种bug和格式问题；
- 添加密码和用户名的加密；
- 添加文件系统（虚拟，仅在Pysys中拥有，并不是主系统的）。
### v0.2.0beta
发布时间：5/1
更新内容：
- 添加网络连接，可以与外界联系；
- 基于基本的网络连接，可以有系统更新提示、阅读文档和获取网页源码等功能。
## TODO
短期（到4/26）：
- [x] readme整合系统常用功能

长期（到5/3）：
- [x] 实现文件路径
- [x] 优化命令行体验

超长期（到5/17）：
- [x] 存储在GitHub上的app可以通过Pysys联网下载安装

完成反馈：
1. 整合了`app list`和`q`两个简单的基础功能，以后会添加更多，大部分完成任务。
2. 命令行体验确实更好了，提示符更改了，但是以后会更好，会使用标准库`cmd`。
3. 已经使用了标准库`cmd`。
4. 在v0.1.0beta中，添加了基本的文件系统，但是不够成熟，需要不断更新才能达到想要的效果。
5. 联网已经基本实现。

# 交流
加QQ2370706289或者发邮件给mczsjzsjz@outlook.com。