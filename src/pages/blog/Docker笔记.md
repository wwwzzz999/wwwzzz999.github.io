---
layout: $/layouts/post.astro
title: docker
date: 2022-09-08
description: jj
tags:
- docker
---
# Docker 笔记



 

## 一. Docker 引擎



### 1. docker与传统虚拟机区别

虚拟机：

1. 硬件支持

2. 操作系统 os

3. VM 虚拟机软件

4. 虚拟机系统（centos）
5. 运行软件服务（mysql，redis，。。。）

![image-20220708134053364](\assets\Docker笔记\image-20220708134053364.png)

虚拟内存→虚拟物理内存→真正物理内存





docker：

1. 硬件支持
2. 操作系统
3. docker引擎
4. 运行服务软件 （mysql，redis，。。。。）

![image-20220708134103957](\assets\Docker笔记\image-20220708134103957.png)

虚拟内存 → 真正物理内存

![image-20220708203737387](\assets\Docker笔记\image-20220708203737387.png)

1. docker引擎对比 传统的虚拟机更加轻量，不需要guest os（centos，。。），本质上都是虚拟化技。

2. docker引擎可以安装在任何操作系统 （不推荐win）



## 二. docker 安装



一. 使用bash 脚本安装 （适用所有Linux 平台）：

1. 拉取sh脚本

```
curl  -fsSL get.docker.com -o get-docker.sh
```



2.  使用阿里云镜像加速执行脚本下载docker

```
sudo sh get-docker.sh --mirror Aliyun
```



二 .启动docker服务

+ 将docker 加入开机

```
systemctl enable docker
```

+ 启动docker 服务

```
systemctl start docker ##restart /status /stop
```



三. 准备工作（推荐）

在Linux中每个用户必须属于一个组，不能独立于组外。在Linux中每个文件有所有者，所在组，其他组的概念

1. 创建docker组

```
sudo groupadd docker
```

2. 将当前用户加入docker组

```
usermod -aG docker $USER 
```



 

## 四. docker 使用

  ### 1.docker 核心概念

1. 镜像 image

    定义： 一个镜像代表一个软件 （redis镜像，mysql镜像，。。。。），只读

2. 容器 Container

   定义：一个镜像运行一次就会生成一个容器，容器就是一个运行的软件服务，可读可写，镜像运行生成容器。

3. 远程仓库 Respostory

   定义：仓库用来存储所有软件的镜像位置 ———> 仓库的的web界面 docker hub（用来查找所需要的镜像）

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220710201251315.png" alt="image-20220710201251315" style="zoom: 80%;" />



4. 本地仓库：

   定义：用来存储在使用docker过程中的相关镜像



### 2.docker核心架构图



![image-20220710205456111](\assets\Docker笔记\image-20220710205456111.png)



 

1. 阿里云提供了远程镜像仓库

+ 配置阿里云镜像加速

```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://7vuxxs7e.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```



2.docker 执行流程：

+ 执行第一个docker程序

```
docker run hello-world
```

	![image-20220711133505733](\assets\Docker笔记\image-20220711133505733.png)



![image-20220711134148999](\assets\Docker笔记\image-20220711134148999.png)





### 3.docker 基本操作

docker 辅助命令：



1. 查看docker 客户端引擎和server端引擎版本信息

```
docker version
```

![image-20220712152235927](\assets\Docker笔记\image-20220712152235927.png)

2. 查看docker引擎详细信息

```
docker info 
```





#### image 的基本操作：

1. 查看当前本地仓库存在的镜像

```
docker image ls   或者  docker images
```

![image-20220712152808501](\assets\Docker笔记\image-20220712152808501.png)

``` 
REPOSITORY(镜像名称) TAG(版本) IMAGE ID(镜像id) CREATED(官方镜像创建时间)  SIZE
hello-world   		latest    	feb5d9fea6a5   9 months ago   		13.3kB

```

 可以使用镜像短命 image id 前几位 或使用 镜像名称



2. 镜像的下载

```
docker pull 镜像名称       ///默认最新版本
docker pull 镜像名称:版本
```

3. 搜索镜像 

```
docker search 镜像名称  ///不可显示版本
```

4. 删除镜像

```
docker image rm 镜像名字or镜像id     （要求镜像没有运行）
```

	强制删除

````
docker image rm -f
````

	**批量删除镜像**

```
docker image rm -f $(docker images 镜像名称 -q)
 ///$()里面的语句先执行,结果传递给主语句
```



#### 容器的基本操作:

操作容器的命令格式 : docker 命令  [选项]

1. 查看正在运行的容器

```
docker ps
```

+ **查看所有容器(包括停止和运行的容器)**

```
docker ps -a
```



2. 简单运行tomcat 容器

```
docker run tomcat
```

![image-20220713154213490](\assets\Docker笔记\image-20220713154213490.png)



容器已经运行,不可结束.

![image-20220713154255263](\assets\Docker笔记\image-20220713154255263.png)

复制新的会话窗口进行操作



3. 容器是在系统层面上进行隔离，此时容器相当与独立的系统。所以通过访问centos系统的8080端口无法访问tomcat，容器无法访问，需要与宿主机端口映射。
4. 容器端口的映射

```\
docker run -p 8080(宿主机):8080 tomcat:8.0
///映射多个端口
-p xxxx:xxx -p xxxx:xxx
///后台启动 -d
docker -p8080:8080 -d tomcat:8.0
```

+ **开放端口映射,后台启动服务,指定容器名称 ---name 容器名称    ////通过容器的名称进行容器的操作**

```
docker run -d -p 8080:8080 --name tomcat01(唯一) tomcat:8.0 ///参数无先后顺序
```

![image-20220713211758652](\assets\Docker笔记\image-20220713211758652.png)

ps:网络防火墙不可以关闭

![image-20220713205514533](\assets\Docker笔记\image-20220713205514533.png)



5. 停止 重启 暂停 恢复容器

```
docker stop 容器名称 | 容器id
docker restart 容器名称 | 容器id
docker start .......
docker pause(暂停) ...
docker unpause(恢复) ....
```



+ 杀死容器

```
docker kill id | name
```

+ 删除容器

```
docker rm id|name  ///删除已经停止的容器
docker rm -f id|name //强制删除
```



6. 查看容器日志

 ```
docker logs id|name

参数:
-t 时间戳
-f 实时日志

 ```

7. 进入容器内部

```
docker exec -it(交互模式) id|name bash   ///进入容器的bash窗口进行交互

```

![image-20220714151053240](\assets\Docker笔记\image-20220714151053240.png)

默认进入tomcat 安装目录

![image-20220714151435793](\assets\Docker笔记\image-20220714151435793.png)

8. 退出容器

```
exit
```

9. 容器与宿主机之间进行容器的拷贝

+ 容器到宿主机

```
docker cp 容器id|name:容器中的文件或目录 主机的目录
```

+ 宿主机到容器

```
docker cp 主机文件或目录 容器id|name:容器中的目录
```

 

10. 查看容器内的进程

```
docker top id|name
```

11. 查看容器内的细节指令

```
docker inspect name|id
```



12. **容器数据卷机制**

数据卷  Data volume

作用: 用来实现容器中数据和宿主机中数据进行映射的(同步,数据绑定)

ps: 使用数据卷不需要频繁去拷贝更新数据,



 

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20220714204914176.png" alt="image-20220714204914176" style="zoom:80%;" />

注意事项:  数据卷使用必须在容器启动前设置 (首次使用时设置)

```
docker run -v 宿主机目录:容器内目录 .......
```

+ 使用绝对路径设置数据卷

```
pwd ///查看路径
```



```
docker run -v 宿主机绝对路劲:容器内路径 .......
docker run -v 宿主机路径:容器内路径:ro
	ro: read only 如果在设置数据卷时指定ro,代表容器内的路径是只读的
注意: 这种方式会将容器路径的原始内容全部清空,始终以宿主机路径为主
```

![image-20220714211049428](\assets\Docker笔记\image-20220714211049428.png)

+ **使用别名方式设置数据卷(核心)**

  ***1.容器的删除不影响数据卷.***

  2.任何需要数据 存储的容器都需要设置数据卷

  ```
  docker run -v aaaa(别名):/user/local/tomcat/webapps ......
  	aaaa: 
  		1.aaaa代表docker数据卷别名 注意: 这个别名如果存在docker直接使用,如果不纯在就创建
  		2.使用别名方式保存容器路径原始内容,前提别名对应路径不能存在内容
  		3.别名创建的目录保存在 /var/lib/docker/volumes/
  ```

  13. 容器打包成一个新的镜像

      a.为什么需要将容器打包成一个新的镜像

      原因：容器时可读可写的，基于这个特性我们就可以对容器进行自己深度定制，将修改的容器打包成一个新的镜像，日后基于这个镜像运行成新的容器存在原始定制特性

      b. 如何将容器打包成一个新的镜像

      ```
      docker commit -m "描述信息" -a "作者" 容器id|name 镜像名:版本 
      ```

### 镜像操作进阶

1.镜像备份和恢复

+ 镜像的备份

```
docker save 镜像名:Tag -o 镜像名-tag(推荐的命名格式).tar
例子: 
	docker save tomcat:8.0 -o tomcat-8.0.tar
```

+ 镜像的恢复

````
docker load -i tomcat-8.0.tar(镜像名)
````

![image-20220915193855607](\assets\Docker笔记\image-20220915193855607.png)







## 四. image 镜像原理

1. image 镜像为什么这么大 

   tomcat : 10M

   image: 365M

   解释: 容器独立的操作系统（精简linux 操作系统+软件服务）==>镜像运行 ==>镜像(操作系统库+软件文件)

2. 镜像的原理

镜像是什么 :镜像是一种轻量级的,可执行的独立软件包,用来打包软件运行环境和基于运行环境开发的软件,他包含运行某个软件所需要的所有软件内容,包括代码,运行时所需要的库,环境变量和配置文件.

	**UnionFS: 联合文件 系统 叠加文件系统**
	
	原理：就是一次同时加载多个文件系统，但从外看起来，只有一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有底层的文件和目录





## 五. mysql服务使用 

1. 搜索mysql 镜像 

   a.访问docker hub 搜索 mysql

   b.确定版本 

2. 下载

   docker pull mysql:5.6

3. 运行mysql

   a.开放端口映射3306

   b.指定用户名和密码  (-e 配置环境)

   c.--restart=always(总是运行,伴随docker)

   d.添加数据卷持久化保存数据

   问题：指定路径需要了解容器内的路径。

   答：所有需要数据存储的数据都需要查看 docker hub 说明文档

   -v xxxx：/var/lib/mysql(查看docker hub 软件说明文档）

   

   docker run --name xxxx -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d --restart=always  -v xxxx：/var/lib/mysql mysql:5.6

   

4. docker 运行mysql 容器数据备份

   问题:  在使用mysql 容器时,数据卷将数据库底层文件系统进行备份 不利于数据迁移和备份 推荐使用sql 文件行式备份数据		

   

   解决: 使用mysql导出sql 文件来备份

   1)备份所有数据

   ps:进入exec 执行shell脚本

   

   ![image-20220722181016103](\assets\Docker笔记\image-20220722181016103.png)

   2) 备份指定库

   ```
   docekr  exec sh -c 'sexc mysqldump --databases 库名 -uroot -p "$MYSQL_ROOT_PASSWORD"' > /root/xxx-databases.sql
   ```

   

   3) 备份指定库的数据接口不要数据

   加入指定参数 : --no-data

   ![image-20220722182740921](\assets\Docker笔记\image-20220722182740921.png)

   4）使用mysql远程连接软件（navicat） 备份数据



## 六 docker 容器间的通讯之网络使用

1. 容器间通讯

容器间的通讯是必须的

![image-20220723112238362](\assets\Docker笔记\image-20220723112238362.png)



2. 使用高级网络配置

在docker 启动后, 会自动创建了一个docker0 的虚拟网桥,

在创建容器后,同时会创建一对veth pair 接口

![image-20220915193808981](\assets\Docker笔记\image-20220915193808981.png)

3.docker 默认创建的所有容器都连接在docker0 网桥上,默认在docker0上的容器都可以通过ip进行通讯, 也可以通过容器名进行通讯 (需要自定义网桥不能使用默认的docker0)

 

<font color=red>4. 自定义网桥 ---建议一个项目自定义一个网桥</font>

1) docker 中网络类型

bridge, host, null



2) 创建自定义桥

docker 