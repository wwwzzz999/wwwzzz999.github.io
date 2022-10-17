---
layout: $/layouts/post.astro
title: ssh连接不上本地虚拟机
date: 2022-10-17
description: ssh连接不上本地虚拟机
tags:
- 虚拟机
---
# ssh 连接不上本地虚拟机



### 检查

查看虚拟机网卡

```
ip a
```

出现ens33:＜NO-CARRIER,BROADCAST,MULTICAST,UP＞mtu 1508 gdisc pf ifo_fast state DOWN。



### 解决

打开windows服务,将中间两个服务设置为自动

![image-20221017231448306](/assets/ssh连接不上本地虚拟机/image-20221017231448306.png)

