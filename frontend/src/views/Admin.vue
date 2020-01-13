<template>
  <div class="row">
    <div class="col-md-10 offset-md-1 mt-5">

      <h1 class="display-5">Credit Products</h1>

      <table class="table table-striped table-hover">
        <thead class="font-weight-bold">
          <tr>
            <th>Bank name</th>
            <th>Credit rate</th>
            <th>Min credit time</th>
            <th>Max credit time</th>
            <th>Early repayment</th>
            <th>Min credit sum</th>
            <th>Max credit sum</th>
            <th>

              <button @click="showModal = true" class="btn btn-outline-success">
                  Add New
              </button>

              <div v-if="showModal" >
                <CreateProductForm @createProduct="createProduct" @close="showModal = false"/>
              </div>

            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.name }}</td>
            <td>{{ product.credit_rate }}%</td>
            <td>{{ product.min_credit_time }} months</td>
            <td>{{ product.max_credit_time }} months</td>
            <td>{{ product.early_repayment }}</td>
            <td>{{ product.min_credit_sum }} $</td>
            <td>{{ product.max_credit_sum }} $</td>

            <td>
              <button @click="deleteProduct(product)" class="btn btn-outline-danger">
                  Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      
    </div>
  </div>
</template>


<script>
import CreateProductForm from "@/components/CreateProductForm.vue";
import axios from 'axios';

export default {

  name: "admin",

  components: {
    CreateProductForm,
  },

  data() {
    return {
      showModal: false,
      products: [],
    };
  },

  created() {
    this.fetchProducts();
  },

  methods: {

    fetchProducts() {
      axios.get('http://127.0.0.1:8000/api/products/')
      .then((res) => {
        this.products = res.data;
      })
    },

    createProduct(current_product) {
      axios.post('http://127.0.0.1:8000/api/products/', current_product)
      .then(() => {
        this.fetchProducts();
        this.showModal = false;
      })
    },
    
    deleteProduct(product_id) {
      const { id } = product_id;

      axios.delete(`http://127.0.0.1:8000/api/products/${id}/`)
      .then(() => {
        this.fetchProducts();
      })
    }
  }
};
</script>

