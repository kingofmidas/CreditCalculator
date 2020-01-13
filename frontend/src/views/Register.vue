<template>
  <div class="row">
    <div class="col-md-4 offset-md-4 mt-5">
      <h1>Sing Up</h1>
      <b-form @submit.prevent="onSubmit">
        <b-form-group id="input-group-1" label-for="input-1">
          <b-form-input id="input-1" v-model="form.username" required placeholder="Enter name">
          </b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label-for="input-2">
          <b-form-input id="input-2" v-model="form.email" required placeholder="Enter email">
          </b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label-for="input-3">
          <b-form-input id="input-3" v-model="form.password" required placeholder="Enter password">
          </b-form-input>
        </b-form-group>

        <div v-if="error" style="color:crimson">
          <b><p>{{error}}</p></b>
        </div>
        <div v-if="valid" style="color:limegreen">
          <b><p>{{valid}}</p></b>
        </div>

        <b-button type="submit" variant="success">Submit</b-button>
        <p class="mt-2"><router-link :to="{name:'login'}">Do you have an account?</router-link></p>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

  export default {
    data() {
      return {
        form: {
          username: '',
          email: '',
          password: '',
        },
        error: '',
        valid: '',
      }
    },
    methods: {
      async onSubmit() {
        let res = await axios.post('http://127.0.0.1:8000/api-user/register/', this.form)
        if(res.data.valid == 'yes'){
          this.valid = "An account activation link has been sent to your mail";
          this.error = '';
        }else {
          this.error = await res.data.username[0];
          this.valid = '';
        }
        this.onReset();
      },

      onReset() {
        this.form.username = this.form.email = this.form.password = '';
      }
    }
  }
</script>



