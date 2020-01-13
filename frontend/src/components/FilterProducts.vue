<template>
    <div class="filter-products">

        <div class="card mb-4 mt-4 border-primary" v-for="product in filterProducts" :key="product.id">
            <table class="table table-borderless">
                <thead class="border-bottom font-weight-bold">
                    <tr>
                        <th>Bank name</th>
                        <th>Credit rate</th>
                        <th>Min credit time</th>
                        <th>Max credit time</th>
                        <th>Min credit sum</th>
                        <th>Max credit sum</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ product.name }}</td>
                        <td>{{ product.credit_rate }}</td>
                        <td>{{ product.min_credit_time }}</td>
                        <td>{{ product.max_credit_time }}</td>
                        <td>{{ product.min_credit_sum }}</td>
                        <td>{{ product.max_credit_sum }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="card-footer text-muted">
                <router-link :to="{name:'about_product', params:{id:product.id}}" class="btn btn-primary float-right">About</router-link>
            </div>
        </div>

    </div>
</template>


<script>
export default {
    name: 'FilterProducts',

    props: ['filterProducts', 'creditSum', 'creditTime'],
}
</script>
