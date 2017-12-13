<template>
    <div class="map" :class="{ 'map-active': show }">
        <div class="map_wrapper">
            <div class="map__text">
                <span class="map__close" @click="clickFalse">сменить метод доставки</span>
                <h1>Выберите точку приёма выдачи заказа.</h1>
                <gmap-map
                        :center="center"
                        :zoom="12"
                        style="width: 550px; height: 484px"

                >
                    <gmap-marker
                            :key="index"
                            v-for="(m, index) in markers"
                            :position="m.position"
                            :clickable="true"
                            @click="[center=m.position, toggleInfoWindow(m,index)]"
                    ></gmap-marker>
                    <gmap-info-window
                            :options="infoOptions"
                            :position="infoWindowPos"
                            :opened="infoWinOpen"
                            @closeclick="infoWinOpen=false">
                        Здесь!
                    </gmap-info-window>
                </gmap-map>
            </div>
            <div class="map_list">
                <div class="map_list-item"
                     :class="{ 'map_list-item-active': infoIndex === index }"
                     v-for="(item, index) in markers" @click="toggleInfoWindow(item, index)">
                    {{ item.position.address }}
                </div>
            </div>
            <div class="map_popup"
                 v-if="infoWinOpen"
            >
                <!--<div class="map_popup-address">{{ infoContent.address }}</div>-->
                <!--<div class="map_popup-desc">{{ infoContent.description }}</div>-->
                <!--<div class="methods__map_popup-phone">{{ infoContent.phone }}</div>-->
                <!--<div class="methods__map_popup-schedule">{{ infoContent.work }}</div>-->
            </div>
            <button class="map-button" @click="backMethods(3)">Перейти к методу оплаты</button>
        </div>

    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data(){
      return{
        show: false,
        result: [],
        next: 1,
        currentMidx: null,
        infoWinOpen: false,
        infoIndex: 0,
        infoWindowPos: {
          lat: 0,
          lng: 0
        },
        infoOptions: {
          pixelOffset: {
            width: 0,
            height: -40
          }
        },
        infoContent: [

        ],
        center: {
          lat: 10.0,
          lng: 10.0
        },

        markers: []
      }
    },
    watch:{
      shiptor(now){
        if(now.method.id === 18 || now.method.id === 25 || now.method.id === 11 || now.method.id === 14 ||
          now.method.id === 67 || now.method.id === 53 || now.method.id === 35) {
          this.ListPoints(this.city.kladr_id, now.method.id, now.method.courier )
          this.$store.commit('results', { type: 'deliveryPoint', items: []})
        } else{
          this.$store.commit('results', { type: 'deliveryPoint', items: []})
        }
      },
      infoContent(now){
        this.$store.commit('results', { type: 'deliveryPoint', items: now})
      },
      result(now) {
        this.infoIndex = 0
        this.markers = [];
        const self = this;

        let gps1 = Number(now[0].gps_location.latitude);
        let gps2 = Number(now[0].gps_location.longitude);
        this.center = {
          lat: gps1,
          lng: gps2
        },
          now.forEach(function (item, i, arr) {

            let gps1 = Number(item.gps_location.latitude);
            let gps2 = Number(item.gps_location.longitude);
            let arrResult =
              {
                position: {
                  lat: gps1, lng: gps2,
                  address: item.address,
                  description: item.trip_description,
                  id: item.id,
                  phone: item.phones[0],
                  work: item.work_schedule,
                  cityName: item.prepare_address,
                }
              }
            ;
//          self.placemarks.push(arrResult)

            self.$set(self.markers, i, arrResult )
          });

        this.toggleInfoWindow(this.markers[0] ,0)
        this.$gmapDefaultResizeBus.$emit('resize');
      }

    },
    computed: {
      city() {
        return this.$store.state.basket.city
      },
      shiptor() {
        return this.$store.state.basket.shiptor
      },
    },
    methods:{
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      ListPoints(idCity, idShiptor, courier) {
        const self = this;
        self.show = true
        axios.post('/shiptorg/', {
          json: {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "getDeliveryPoints",
            "params": {
              "kladr_id": idCity,
              "courier": courier,
              "shipping_method": idShiptor,
            }
          }
        }).then(
          function (response) {
            ;
            self.result = response.data.result

          }
        )
      },
      clickFalse(){
        this.show = false

      },
      toggleInfoWindow: function(marker, idx) {
        this.infoWindowPos = marker.position;
        this.infoContent = marker.position;
        this.infoIndex = idx;
        this.center = {
          lat: marker.position.lat,
          lng: marker.position.lng,
        }

        //check if its the same marker that was selected if yes toggle
        if (this.currentMidx === idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }
        //if different marker set infowindow to open and reset current marker index
        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
        this.$gmapDefaultResizeBus.$emit('resize');
      }

    }
  }
</script>