<template>
  <div id="app">

    <b-navbar id="navbar" >
      <b-navbar-brand>
        <router-link to="/home" class="text-white mr-3">
          Credit Calculator
        </router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-nav-item v-if="authenticated">
              <router-link to="/home" class="text-white mr-3">
                Calculator
              </router-link>
            </b-nav-item>
            <b-nav-item v-if="admin">
              <router-link to="/admin" class="text-white mr-3">
                Products
              </router-link>
            </b-nav-item>
          </b-navbar-nav>

          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <em class="text-white">User</em>
            </template>
            <b-dropdown-item>
              <span><router-link to="/login">Log In</router-link></span>
            </b-dropdown-item>
            <b-dropdown-item>
              <span><router-link to="/register">Register</router-link></span>
            </b-dropdown-item>
            <b-dropdown-item v-if="authenticated" @click.prevent="logOut">
              <span>Log Out</span>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view></router-view>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters({
      authenticated: 'auth/isAuthenticated',
      admin: 'auth/isAdmin',
    }),
  },

  methods: {
    ...mapActions({
      logOutAction: 'auth/logOut'
    }),

    logOut () {
      this.logOutAction()
      .then(() => {
        this.$router.push({ name: 'login' })
      })
    }
  },

}
</script>


<style>
#app {
  /* font-family: "Avenir", Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased; 
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2e649b;
  font-family:'Montserrat','sans-serif';
  background-color:rgb(255, 255, 255);
  
}

#navbar {
  background-color: #182022;
}
</style>
