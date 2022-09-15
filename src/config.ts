import type{ NavItems } from './types'

export const NAV_ITEMS: NavItems = {
    home: {
        path: '/',
        title: '主页'
    },
    blog: {
        path: '/blog',
        title: '博客'
    },
    tags: {
        path: '/tags',
        title: '标签'
    },
    // media: {
    //     path: '/media',
    //     title: 'media'
    // },
    // about: {
    //     path: '/about',
    //     title: 'about'
    // }
}

export const SITE = {
    // Your site's detail?
    name: 'wwwzzz999博客',
    title: 'wwwzzz999的博客',
    // description: 'Crisp, minimal, personal blog theme for Astro',
    // url: 'https://astro-ink.vercel.app',
    githubUrl: 'https://github.com/wwwzzz999',
    listDrafts: true
    // description ?
}

export const PAGE_SIZE = 8
