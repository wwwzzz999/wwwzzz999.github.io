---
layout: $/layouts/post.astro
title: 设置.gitignore规则不生效
date: 2022-09-17
tags:
- 问题t
- git
description: git设置忽略不生效
---





# 关于git 设置.gitignore规则不生效可能的问题

.gitignore只能忽略那些原来没有被 track 的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。

解决方法： 删除缓存，更新到未跟踪状态，重新提交

```cmd
git rm -r --cached   
git add .
……
```

总结：当出现未知问题致使远程仓库同预期结果不一致时，本地可以将问题目录恢复到未被追踪状态，核查完问题之后再次提交最新结果

参考资料：

```cmd
usage: git rm [<options>] [--] <file>...

    -n, --dry-run         dry run
    -q, --quiet           do not list removed files
    --cached              only remove from the index
    -f, --force           override the up-to-date check
    -r                    allow recursive removal
    --ignore-unmatch      exit with a zero status even if nothing matched
```



 