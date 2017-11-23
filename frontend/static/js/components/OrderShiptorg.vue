<template>
    <div class="order__shiptorg">
        {{ phone }}
        <button @click="postShiptorg()">shiptorg</button>
        {{ result }}
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        result: []
      }
    },
    computed: {
      phone() {
        return this.$store.state.basket.phone
      },
      city() {
        return this.$store.state.basket.city
      },
      email() {
        return this.$store.state.basket.email
      },
      FirstName() {
        return this.$store.state.basket.FirstName
      },
      phone() {
        return this.$store.state.basket.phone
      },
      phone() {
        return this.$store.state.basket.phone
      },
      phone() {
        return this.$store.state.basket.phone
      },
    },
    methods: {
      postShiptorg() {
        const self = this;
        axios.post('/shiptorg/', {
            json: {
                "id": "JsonRpcClient.js",
                "jsonrpc": "2.0",
                "method": "calculateShipping",
                "params": {
                    "length": 10,
                    "width": 10,
                    "height": 10,
                    "weight": 10,
                    "cod": 10,
                    "declared_cost": 10,
                    "kladr_id": "01000001000",
                    "courier": "dpd"
                }
            }
      }).then(
          function (response) {
            console.log(response)
            self.result = response.date
          }
        )

      }
    }
  }
</script>
