---
layout: $/layouts/post.astro
title: 使用Dockerfile与docker network部署springboot项目
date: 2022-10-21
description: 初学docker的测试
tags:
- Dockerfile
---
# 使用Dockerfile 与docker network 部署spring boot应用

## 1.上传springboot.jar到主机

注:修改application.yml配置中的mysql 的连接

useSSL=false,取消ssl安全检测,使用主机名作为mysql地址

```
spring:
  application:
    name: Dockertest
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    username: root
    password: root
    url: jdbc:mysql://mysql:3306/docker_test?useUnicode=true&characterEncoding=utf-8&serverTimezone=GMT&useSSL=false
    driver-class-name: com.mysql.cj.jdbc.Driver
```

### 1) 打包程序

### 2) 上传jar包

技巧:

在idea上浏览远程主机进行文件的操作

![image-20221020144523181](/assets/使用Dockerfile与docker network部署springboot应用/image-20221020144523181.png)







### 3)新建文件夹新创建Dockerfile

![image-20221021151342635](/assets/使用Dockerfile与docker network部署springboot应用/image-20221021151342635.png)

## 2.下载所需镜像





### 1) 下载jre镜像

[docker利用jre制作成基础镜像,再根据这个基础镜像制作可运行jar包的镜像_左边有只汪的博客-CSDN博客](https://blog.csdn.net/weixin_43744059/article/details/108059971)

在docker hub 中搜索openjdk，下载镜像



![image-20221020190746907](/assets/使用Dockerfile与docker network部署springboot应用/image-20221020190746907.png)



### 2) 下载mysql:5.7 镜像



## 3.编写dokerflie构建镜像

### 1) 基于jre 构建镜像

Dockerfile

```
FROM openjdk:8-jre
ENV PATH_TEST=/spring_test
WORKDIR $PATH_TEST
ADD springboot_docker-1.0-SNAPSHOT.jar $PATH_TEST/app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar"]
CMD ["app.jar"]
```

### 2) 运行Dockerfile 构建镜像

```
docker build -t app:1.0
```



## 4.运行镜像构建网络



### 1) 运行mysql镜像

```
docker run -p3306:3306 -d -e MYSQL_ROOT_PASSWORD=root -v mysqldata:/var/lib/mysql mysql:5.7 
```

### 2) 运行app镜像

```
docker run -p 8080:8080 -d app:1.0
```



### 3)创建网络

```
docker network create app
```

### 4) 添加mysql 与 app 容器到一个网络下

```
docker network connect app mysql
docker network connect app app的id
```



### 5) 查看网络

```
docker inspect app
```



<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20221021152217875.png" alt="image-20221021152217875" style="zoom:80%;" />





## 5. 使用mysql连接软件连接数据库导入数据



## 6. 结果

![image-20221021153649222](/assets/使用Dockerfile与docker network部署springboot应用/image-20221021153649222.png)



注:springboot 项目打包时需要引入插件，否则XXX--1.0-SNAPSHOT.jar中没有主清单属性

```
<!-- 这个插件，可以将应用打包成一个可执行的jar包  -->
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```





