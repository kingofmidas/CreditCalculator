// import "@babel/polyfill";
// import "mutationobserver-shim";
import "./plugins/bootstrap-vue";
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from 'axios';

// require('@/store/subscriber');

Vue.config.productionTip = false;


axios.interceptors.request.use(
  config => {
      const access_token = localStorage.getItem('access_token');
      if (access_token) {
          config.headers['Authorization'] = 'JWT ' + access_token;
      }
      return config;
  },
  error => {
      Promise.reject(error)
  });


axios.interceptors.response.use((response) => {
  return response
}, (error) => {

  const originalRequest = error.config;

  if (error.response.status === 401 && originalRequest.url ==='http://127.0.0.1:8000/api/token/refresh/') {
    router.replace({ name: 'login' });
    return Promise.reject(error);
  }

  if (error.response.status === 401 && !originalRequest._retry) {

    originalRequest._retry = true;
    const refresh_token = localStorage.getItem('refresh_token');

    return axios.post('http://127.0.0.1:8000/api/token/refresh/', {"refresh": refresh_token})
      .then((res) => {
        if (res.status === 200) {
          localStorage.setItem('access_token', res.data.access)
          localStorage.setItem('refresh_token', res.data.refresh)
          return axios(originalRequest);
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return Promise.reject(error);
})


store.dispatch('auth/attempt', {
  access: localStorage.getItem('access_token'),
  refresh: localStorage.getItem('refresh_token'),})
  .then(() => {   
    new Vue({
      router,
      store,
      render: h => h(App)
    }).$mount("#app");
  })

