---
layout: $/layouts/post.astro
title: java中关于try-return-finally问题
date: 
description: 关于代码中try-return-finally执行顺序问题
tags:
- 问题
---
# Java中关于try-return-finally问题

[JAVA中try、catch、finally带return的执行顺序总结 - PC君 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pcheng/p/10968841.html)

**一、try中带有return**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1     private int testReturn1() {
 2         int i = 1;
 3         try {
 4             i++;
 5             System.out.println("try:" + i);
 6             return i;
 7         } catch (Exception e) {
 8             i++;
 9             System.out.println("catch:" + i);
10         } finally {
11             i++;
12             System.out.println("finally:" + i);
13         }
14         return i;
15     }
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

输出：

try:2
finally:3
2

　　因为当try中带有return时，会先执行return前的代码，然后暂时保存需要return的信息，再执行finally中的代码，最后再通过return返回之前保存的信息。所以，这里方法返回的值是try中计算后的2，而非finally中计算后的3。但有一点需要注意，再看另外一个例子：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1     private List<Integer> testReturn2() {
 2         List<Integer> list = new ArrayList<>();
 3         try {
 4             list.add(1);
 5             System.out.println("try:" + list);
 6             return list;
 7         } catch (Exception e) {
 8             list.add(2);
 9             System.out.println("catch:" + list);
10         } finally {
11             list.add(3);
12             System.out.println("finally:" + list);
13         }
14         return list;
15     }
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

输出：

try:[1]
finally:[1, 3]
[1, 3]

　　看完这个例子，可能会发现问题，刚提到return时会临时保存需要返回的信息，不受finally中的影响，为什么这里会有变化？其实问题出在参数类型上，上一个例子用的是基本类型，这里用的引用类型。list里存的不是变量本身，而是变量的地址，所以当finally通过地址改变了变量，还是会影响方法返回值的。

 