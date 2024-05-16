import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import BookDetail from "../views/BookDetail.vue"; // 引入 BookDetail 组件

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/comments",
    name: "Comments",
    // 加入新的路由
    component: () =>
      import("../views/Comments.vue")
  },
  {
    path: "/reader",
    name: "Reader",
    component: () =>
      import("../views/Reader.vue")
  },
  {
    path: "/book/:bookId",
    name: "BookDetail",
    component: BookDetail,
    props: true
  },
  {
    path: "/Center",
    name: "Center",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
       import(/* webpackChunkName: "center" */ "../views/centre.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
