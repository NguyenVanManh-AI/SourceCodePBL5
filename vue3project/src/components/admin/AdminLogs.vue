<template>
    <div id="adminlogs">
        <div id="detail_adminlogs" class="col-12" style="background-color: white;">
            <div>
                <div style="margin-top: 30px;margin-bottom: 20px;color:gray;text-align: center;font-size: 23px;"><i class="fa-solid fa-clock-rotate-left" style="margin-right: 10px;"></i> LOGS</div>
            </div>
            <table class="table table-bordered">
                <thead class="thead-dark">
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Id User</th>
                    <th scope="col">Full Name</th>
                    <th scope="col">Date Time</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(log,index) in logs" :key="index">
                        <th scope="row">{{log.id}}</th>
                        <td>{{log.id_user}}</td>
                        <td v-if="log.id_user==999999">UNKNOWN</td>
                        <td v-if="log.id_user!=999999">{{ fullnames[index] }}</td>
                        <td>{{ log.date }}</td>
                    </tr>
                </tbody>
            </table>
            </div>
        </div>
</template>
<script>

import BaseRequest from '../../restful/user/core/BaseRequest';
// import BaseRequest from '../../restful/admin/core/BaseRequest';
// import useEventBus from '../../composables/useEventBus'
import Notification from './Notification'
// import config from '../../config.js'

import LineChart from './admin_chart/LineChart.vue'
import DoughnutChart from './admin_chart/DoughnutChart.vue'
import BarChart from './admin_chart/BarChart.vue'
import ParticleVue32 from "../particle/ParticleVue32.vue";
import useEventBus from '../../composables/useEventBus'
import Paginate from 'vuejs-paginate-next';

// import Paginate from 'vuejs-paginate-next';

// import ParticleVue32 from "./particle/ParticleVue32.vue";

export default {
    name:"AdminLogs",
    components:{
        Notification,
    },
    setup() {
        // document.title = "Meta Shop - Statistical"
    },
    data(){
        return {
            logs:null,
            count:null,
            fullnames:[],
        }
    },
    mounted() {

        BaseRequest.get('attendances/')
        .then(data => {
            this.logs = data.results;
            this.count = data.count;
            const requests = [];
            for (let i = 0; i < this.count; i++) {
            const request = BaseRequest.get('full-name/?id_user=' + this.logs[i].id_user)
                .then(data => {
                this.fullnames[i] = data.fullname;
                })
                .catch(() => {
                this.fullnames[i] = 'UNKNOWN';
                });

            requests.push(request);
            }

            return Promise.all(requests);
        })
        .catch(() => {
            // Xử lý lỗi nếu có
        });
    },
    watch: {
    },
    methods:{
//         getName: function (id) {
//   return new Promise((resolve, reject) => {
//     BaseRequest.get('full-name/?id_user=' + id)
//       .then(data => {
//         const fullname = data.fullname;
//         resolve(fullname);
//         console.log(fullname);
//       })
//       .catch(() => {
//         reject(new Error('Failed to get full name'));
//       });
//   });
// }

    },
}
</script>

<style scoped>
  #adminlogs{
    position: relative;
    /* background-color: #F2F4F6; */
    padding: 30px 40px;
    /* height: 800px; */
    min-width: 100%;
  }
  
  #detail_adminlogs{
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 20px 40px !important;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    /* font-weight: bold; */
  }
</style>
