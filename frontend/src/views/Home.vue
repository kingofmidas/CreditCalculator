<template>
    <div class="row">

      <div class="col-md-4 offset-md-4 mt-5">
        
        <h1 class="display-4 align-items-center">Calculator</h1>
        <hr class="my-4">

        <b-form>
          <b-form-group>
              <b-form-input placeholder="Credit sum" v-model.number="credit_sum" required>
              </b-form-input>
          </b-form-group>
          <b-form-group>
              <b-form-input placeholder="Credit time" v-model.number="credit_time" required>
              </b-form-input>
          </b-form-group>
          <b-form-group>
            <b-form-radio-group id="checkboxes-4">
                <p> Early repayment:
                  <b-form-radio value="True" v-model="repayment">Yes</b-form-radio>
                  <b-form-radio value="False" v-model="repayment">No</b-form-radio>
                </p>
            </b-form-radio-group>
          </b-form-group>

          <div v-if="errors">
            <p  class="input_errors">Invalid Data</p>
          </div>

          <b-button @click.prevent="filterProducts" type="submit" variant="primary">Submit</b-button>
        </b-form>
      </div>

      <div class="col-lg-6 offset-lg-3 mt-4" id="product-card">
        <FilterProducts :filter-products="filter_products" :credit-sum="credit_sum" :credit-time="credit_time"/>
      </div>

    </div>
</template>


<script>
import FilterProducts from "@/components/FilterProducts.vue";
import axios from 'axios';

export default {

  components: {
    FilterProducts
  },

  name: "home",

  data() {
    return {
      credit_sum: '',
      credit_time: '',
      repayment: '',
      filter_products: [],
      errors: '',
    };
  },

  methods: {

    filterProducts() {
      axios.get(`http://127.0.0.1:8000/api/filter/?credit_sum=${this.credit_sum}&credit_time=${this.credit_time}&early_repayment=${this.repayment}`)
      .then((response) => {
        this.filter_products = response.data;
        localStorage.setItem('credit_sum', this.credit_sum);
        localStorage.setItem('credit_time', this.credit_time);
        this.credit_sum = this.credit_time = this.repayment = '';
        this.errors = '';
      })
      .catch((error) => {
        this.errors = error;
      })
    },
  }
};
</script>

