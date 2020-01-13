<template>
    <transition name="modal">

        <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container">

                    <b-form @submit.prevent="$emit('createProduct', currentProduct)">
                        <b-form-group>
                            <b-form-input 
                            type="text"
                            placeholder="Bank name" 
                            v-model="currentProduct.name" 
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-input 
                            type="number" 
                            placeholder="Credit rate" 
                            v-model="currentProduct.credit_rate"
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-input 
                            type="number" 
                            placeholder="Min credit time" 
                            v-model="currentProduct.min_credit_time"
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-input 
                            type="number" 
                            placeholder="Max credit time" 
                            v-model="currentProduct.max_credit_time"
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-input 
                            type="number" 
                            placeholder="Min credit sum" 
                            v-model="currentProduct.min_credit_sum"
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-input 
                            type="number" 
                            placeholder="Max credit sum" 
                            v-model="currentProduct.max_credit_sum"
                            required>
                            </b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-form-radio-group required>
                                <p>Early repayment:
                                  <b-form-radio value="True" v-model="currentProduct.repayment">Yes</b-form-radio>
                                  <b-form-radio value="False" v-model="currentProduct.repayment">No</b-form-radio>
                                </p>
                            </b-form-radio-group>
                        </b-form-group>

                        <b-button type="submit" variant="success" class="mr-2">Submit</b-button>
                        <b-button @click="$emit('close')" type="button" variant="danger">Cancel</b-button>
                    </b-form>

                </div>
            </div>
        </div>

    </transition>
</template>


<script>
export default {
    name: 'CreateProductForm',
    data() {
        return {
            currentProduct: {},
        }
    },
}
</script>


<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 400px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>