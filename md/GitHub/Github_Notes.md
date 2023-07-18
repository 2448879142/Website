# 笔记
-----------------

> [GitHub菜鸟教程](https://www.runoob.com/w3cnote/git-guide.html)


## 如何上传 GitHub

### 1.git 安装

- 下载并安装 Git
- [git 教程-菜鸟教程](https://www.runoob.com/git/git-tutorial.html)

### 2. git 使用

##### 设置用户签名

- 进入代码文件路径当中，右击选择“Git Bash here”，然后输入以下代码：

```git
# 让 git 知道是谁在操作
 git config --global user.name '用户名' # 在当前工作目录下执行操作
 git config --global user.email '邮箱' # 在当前工作目录下执行操作
```

##### 初始化

- 在代码文件夹下初始化一个.git

```git
git init # 初始化
```

##### 提交到暂存区

- 在代码文件夹下，将数据提交到暂存区中， `.`代表当前文件夹路径中所有文件

```git
git add . # 提交到暂存区中
```

##### 提交到本地仓库

- 将暂存区提交到本地仓库
- git commit -m '初始化项目版本:备注'

```git
git commit -m "first commit" # 第一次提交
```

##### 创建分支管理

- 创建一个新分支，名为`master`，并在代码文件夹下执行操作。

```git
git branch -M master # 创建分支master，然后切换到该分支
```

##### 远程添加

- 这个 origin 只是我们给后面一长串远程地址起的别名;
- 修改后，push 时， origin 的位置改成你起的别名.

```git
git remote add origin 仓库的SSH链接 	# 在你的机器上添加一个远程库origin
```

##### 提交到远程仓库

- 将本地仓库中的数据提交到远程仓库

```git

git push -u origin master

```

--------------

## 权限拒绝访问

### fatal: Could not read from remote repository

- 解决git@github.com: Permission denied (publickey). fatal: Could not read from remote repository.
- 输入以下代码重新生成 shh key 一路回车即可
- `"C:\Users\24488\.ssh\id_rsa.pub"`，复制文件里面的代码
- 登录 GitHub，进入 Settings,` SHH and GPG keys>New SSH key`,将复制的代码，新建一个 key
- [问题参考文档](https://blog.csdn.net/W_317/article/details/106518894)

```git
$ ssh-keygen -t rsa -C "邮箱"
```

-------------

## 更新远程仓库报错

### error: failed to push some refs to ‘xxx‘ 报错

> - error: failed to push some refs to ‘xxx‘
> - hint: Updates were rejected because the remote contains work that you do
> - hint: not have locally. This is usually caused by another repository pushing
> - hint: to the same ref. You may want to first integrate the remote changes
> - hint: (e.g., 'git pull ...') before pushing again.
> - hint: See the 'Note about fast-forwards' in 'git push --help' for details.

### 解决办法

- git pull 命令用于从远程获取代码并合并本地的版本;

> git pull 使用了强制 push 的方式提交代码，这样会带来版本覆盖的问题.

- git push 命令用于从将本地的分支版本上传到远程并合并.

> 本办法会合并分支，谨慎操作.

-------------

## gitClone

```
git clone 'url'
```
