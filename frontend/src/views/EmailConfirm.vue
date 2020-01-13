<template>
    <div class="email-confirm">
        <div v-if="error">
            <h3>{{ error }}</h3>
        </div>
        <div v-else="">
            <h3>You have successfully confirmed your email</h3>
            <p><router-link :to="{name:'login'}"><b>Log In</b></router-link></p>
        </div>
       
    </div>
</template>


<script>
import axios from 'axios';
export default {
    data() {
        return {
            error: '',
        }
    },

    async created() {
        const user_id = this.$route.query.code
        let res = await axios.post('http://127.0.0.1:8000/api-user/activation/',{user_id:user_id})
        if(res.data.res == 'no'){
            this.error = "Activation link is invalid!"
        }else{
            this.error = '';
        }
    }
}
</script>