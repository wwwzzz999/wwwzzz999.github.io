---
layout: $/layouts/post.astro
title: Vue学习笔记
date: 2022-04-1
description: Vue 基础知识学习笔记
tags:
- Vue
---
## component

 使用组件可以实现代码的复用

component中的props 属性可以设置成对象。避免属性值过多，绑定繁琐

```js
Vue.component('blog-post', {
  props: ['post'],
  template: `
    <div class="blog-post">
      <h3>{{ post.title }}</h3>
      <button>
        Enlarge text
      </button>
      <div v-html="post.content"></div>
    </div>
  `
})
```





![image-20220329164708261](/assets/vue/image-20220329164708261.png)



```html
<div id="blog-posts-events-demo">
  <div :style="{ fontSize: postFontSize + 'em' }">
    <blog-post
      v-for="post in posts"
      v-bind:key="post.id"
      v-bind:post="post"
    ></blog-post>
  </div>
</div>
```



# vue router

vue router 放在vue.js 之后





![image-20220328185633775](/assets/vue/image-20220328185633775.png)



## 纯静态引入.vue文件之http-vue-loader.js

![image-20220328192205278](/assets/vue/image-20220328192205278.png)







## 普通web项目引入.vue组将

定义.vue

```js
<template>
  <h2>headercom{{mes}}</h2>
</template>

<script>

module.exports= {
  data(){
    return {
      mes: "9999"
    }
  }
}
</script>

<style>

</style>
```

关键“module.exports={}”

引入：

![image-20220329165542815](/assets/vue/image-20220329165542815.png)

 ## vue 监听地址栏

```js
watch: {
	$route(to, from){
		// todo
	}
}

```

