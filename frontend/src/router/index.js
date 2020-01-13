import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import Admin from "../views/Admin.vue";
import AboutProduct from "../views/AboutProduct.vue";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import EmailConfirm from "../views/EmailConfirm.vue"

import store from '@/store'


Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "home",
    component: Home,
  },
  {
    path: "/admin",
    name: "admin",
    component: Admin,
  },
  {
    path: '/about-product/:id',
    name: 'about_product',
    component: AboutProduct,
    props: true,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/email',
    name: 'email',
    component: EmailConfirm,
  }
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

router.beforeEach((to, from, next) => {
  const publicPages = ['login', 'register', 'email'];
  const authRequired = !publicPages.includes(to.name)

  if(authRequired && !store.getters['auth/isAuthenticated']){
    return next('/login')
  }
  if((to.name==='admin') && !store.getters['auth/isAdmin']){
    return next('/home')
  }
  next();
})


export default router;
