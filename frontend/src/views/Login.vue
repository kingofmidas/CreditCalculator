<template>
  <div class="row">
    <div class="col-md-4 offset-md-4 mt-5">

      <h1>Log In</h1>
      <b-form @submit.prevent="submit">
        <b-form-group id="input-group-1" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.username"
            type="text"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.password"
            required
            type="password"
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>

        <div v-if="errors">
          <p  class="input_errors">Invalid Data</p>
        </div>

        <b-button type="submit" variant="primary">Submit</b-button>
        <p class="mt-2"><router-link :to="{name:'register'}">Don't have an account?</router-link></p>
      </b-form>

    </div>
  </div>
</template>


<script>
import { mapActions } from 'vuex';

export default {
  name: 'login',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      errors: '',
    }
  },
  methods: {

    ...mapActions ({
      obtainTokens: 'auth/obtainTokens'
    }),

    async submit() {
      this.obtainTokens(this.form)
        .then(() => {
          this.errors = '';
          this.$router.replace({ name: 'home' })
        })
        .catch((error) => {
          this.errors = error
        })
    },
  }
}
</script>



<style>
  .input_errors {
    color: crimson;
    margin: 10px;
  }
  
</style>