<template>
    <div class="row">
        <div class="col-md-8 offset-md-2 mt-4 container">

            <table class="table table-striped table-dark table-hover">
                <thead class="font-weight-bold">
                    <tr>
                        <th>Месяц</th>
                        <th>Сумма</th>
                        <th>Платеж</th>
                        <th>Ставка</th>
                        <th>Срок</th>
                        <th>Проценты</th>
                        <th>Тело</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th></th>
                        <th>{{ sum[0] }}</th>
                        <th>{{ payment }}</th>
                        <th>{{ rate }}</th>
                        <th>{{ time }}</th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                    <tr v-for="(value,index) in sum" :key="index">
                        <td v-if="index < (sum.length - 1)">{{ index + 1 }}</td>
                        <td v-if="index < (sum.length - 1)">{{ sum[index + 1] }}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>{{ percents[index] }}</td>
                        <td>{{ body[index] }}</td>
                        <td>{{ percents_plus_body[index] }}</td>
                    </tr>
                </tbody>
            </table>
          
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {

  name: "about-product",

  props: ['id'],

  data() {
    return {
        product: {},
        sum: [],
        percents: [],
        body: [],
        percents_plus_body: [],
        payment: '',
        rate: '',
        time: '',
    };
  },

  created() {
    axios.get(`http://127.0.0.1:8000/api/product/${this.id}`)
    .then((response) => {
        this.product = response.data;
        this.calculation();
    })
  },

  methods: {
      calculation() {

        this.rate = this.product.credit_rate/100;
        this.sum = [+(localStorage.credit_sum)];
        this.time = +(localStorage.credit_time);

        var payment_numerator = (this.rate/12)*(Math.pow(1+(this.rate/12), this.time));
        var payment_denominator = Math.pow(1+(this.rate/12), this.time) - 1;
        this.payment = +((this.sum[0]*(payment_numerator/payment_denominator)).toFixed(2));

        this.percents = [];
        this.body = [];
        this.percents_plus_body = [];

        for(let i = 0; i < this.time; i++){

            this.percents.push(+(Math.round(100*this.sum[i]*this.rate/12)/100).toFixed(2));
            this.body.push(+(Math.round(100*(this.payment - this.percents[i]))/100).toFixed(2));
            this.percents_plus_body.push(+(Math.round(100*(this.percents[i] + this.body[i]))/100).toFixed(2));
            
            if(i == (this.time - 1)){
                this.body[i] = this.sum[i]
                this.percents_plus_body[i] = (+(Math.round(100*(this.percents[i] + this.body[i]))/100).toFixed(2))
                this.sum.push(+Math.round(this.sum[i] - this.body[i]));
            }
            else{
                this.sum.push(+(Math.round(100*(this.sum[i] - this.body[i]))/100).toFixed(2));
            }
        }
      }
  }
};
</script>


<style>
.container {
    display: flex;
}
.container div{
    padding: 10px;

    border: 1px solid silver;
}
</style>

