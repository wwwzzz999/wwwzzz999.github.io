---
layout: $/layouts/post.astro
title: Springboot整合mybatis
date: 2022-01-11
description: 
tags:
- Springboot
- mybatis
---
# springboot + mybatis



## 1. 数据库依赖

pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.6.4</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.wu</groupId>
    <artifactId>springbootMybatis</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springbootMybatis</name>
    <description>springbootMybatis</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.0.1</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.9</version>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```



1.mybatis 依赖

``` xml
<dependency>
	<groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.3.1</version>
</denpendency>

<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.2.0</version>
</dependency>
```

2.数据库驱动

```xml
<dependency>
	<groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

3.数据库连接池

```xml
<dependency>
	<groupId>com.alibaba</groupId>
    <artifactId>druid</artifactId>
    <version>1.2.4</version>
</dependency>
```



 ## 2.结构目录

![image-20220308172111500](/assets/springBoot+mybatis/image-20220308172111500.png)

controller层，serice层，dao层

## 技巧

使用lombok可以简化操作

``` xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>
```

### @Data

@Data注解在类上，会为类的所有属性自动生成setter/getter、equals、canEqual、hashCode、toString方法，如为final属性，则不会为该属性生成setter方法。

### @Getter/@Setter

@Getter/@Setter注解，此注解在属性上，可以为相应的属性自动生成Getter/Setter方法@Getter/@Setter注解，此注解在属性上，可以为相应的属性自动生成Getter/Setter方法

### @NonNull

该注解用在属性或构造器上，Lombok会生成一个非空的声明，可用于校验参数，能帮助避免空指针。

### @ToString

.....

### @NoArgsConstructor, @RequiredArgsConstructor and @AllArgsConstructor

无参构造器、部分参数构造器、全参构造器。

``` java
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.NonNull;

@RequiredArgsConstructor(staticName = "of")
@AllArgsConstructor(access = AccessLevel.PROTECTED)
public class ConstructorExample<T> {
  private int x, y;
  @NonNull private T description;
  
  @NoArgsConstructor
  public static class NoArgsExample {
    @NonNull private String field;
  }
}
```



## 3.mybatis 配置文件（application.yml）

![image-20220307203528260](/assets/springBoot+mybatis/image-20220307203528260.png)

### application.yml基本信息配置

``` yaml
server:
  port: 8080

# 数据库数据源
spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    username: root
    password: 123456
    url: jdbc:mysql://localhost:3306/webapp?useUnicode=true&characterEncoding=utf-8&serverTimezone=GMT
    driver-class-name: com.mysql.cj.jdbc.Driver

mybatis:
  mapper-locations: classpath:/mapper/*.xml   #   xml文件

logging:
  file:
    name: log/log.log
  level:
    root: info
    wuhobin: debug

```



- MySQL5.x的版本使用的驱动类是com.mysql.jdbc.Driver
- MySQL8.x的版本使用的驱动类是com.mysql.**cj**.jdbc.Driver

两者区别：[mysql驱动 com.mysql.cj.jdbc.Driver报红 - 春霞紫梦 - 博客园 (cnblogs.com)](https://www.cnblogs.com/stone075/p/15346837.html)

![image-20220307203127380](/assets/springBoot+mybatis/image-20220307203127380.png)

## 4.dao, mapper.xml

```java
package com.wu.dao;

import com.wu.pojo.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;
@Mapper
@Repository
public interface UserDao {
    List<User> findAll();
}
```



```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.wu.dao.UserDao">
  <select id="findAll" resultType="com.wu.pojo.User">
    select * from user;
  </select>
</mapper>
```

## 5.service

```java
package com.wu.service;

import com.wu.pojo.User;

import java.util.List;

public interface UserService {
    List<User> findAll();
}
```





```java
package com.wu.service;

import com.wu.pojo.User;
import com.wu.dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class UserServiceImpl implements UserService{
    @Autowired
    UserDao dao;
    @Override
    public List<User> findAll() {
        return dao.findAll();
    }
}
```

## 6 controller

```java
package com.wu.controller;

import com.wu.pojo.User;
import com.wu.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class UserConroller {

    @Autowired
    UserService userService;
    @RequestMapping("/findall")
    @ResponseBody
    public List<User> findall(){
        return userService.findAll();
    }
}
```

## 7，项目地址

D:\Demo\spring_boot\springbootMybatis

## 8.测试类

在测试类上添加

```java
@RunWith(SpringRunner.class)
@SpringBootTest
```

![image-20220311172748918](/assets/springBoot+mybatis/image-20220311172748918.png)



![image-20220311172804199](/assets/springBoot+mybatis/image-20220311172804199.png)
