<template>
    <div id="statistical">
        <ParticleVue32></ParticleVue32>
        <div id="detail_statistical" class="col-12" style="background-color: white;">
            <div>
                <div style="margin-top: 30px;margin-bottom: 20px;color:gray;text-align: center;font-size: 23px;"><i class="fa-solid fa-chart-pie" style="margin-right: 10px;"></i> STATISTICAL</div>
                <!-- <router-link :to="{ name: 'AdminComp' }"> Dashboard Admin </router-link><i class="fa-solid fa-angles-right"></i> -->
                <!-- <router-link :to="{ name: 'AdminStatistical' }"> Admin Statistical </router-link> -->
            </div>
            <!-- <hr> -->
            <div>Statistics on the number of employees coming to work on time, coming to work late and leaving work by day, week, month and year</div>
            <br>
            <div class="row">
                <div class="col-6">
                    <div class="row">
                        <div class="col-12">
                            <LineChart></LineChart>
                        </div>
                    </div>
                    <div class="row mt-12">
                        <div class="col-12">
                            <BarChart></BarChart>
                        </div>
                    </div>
                </div>
                <div class="col-6">
                    <DoughnutChart></DoughnutChart>
                </div>
            </div>

            <div id="table_user">
                <div style="margin-bottom: 10px;display: flex;align-items: center;align-content: center;">Number of employees of the company : <span style="color: green;font-size: 20px;margin-left: 3px;"> {{ num_user}}</span></div>
                <div class="mx-auto">
                    <table class="table table-hover table-bordered" style="font-weight: 100;">
                        <thead class="thead-dark">
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">ID</th>
                                <!-- <th scope="col" class="text-center"><i class="fa-solid fa-envelope"></i> Email</th> -->
                                <th scope="col" ><i class="fa-solid fa-envelope"></i> Email</th>
                                <th scope="col" ><i class="fa-solid fa-at"></i> Full Name</th>
                                <th scope="col" ><i class="fa-solid fa-phone"></i> Phone</th>
                                <!-- <th scope="col" ><i class="fa-solid fa-layer-group"></i> Vector</th> -->
                                <!-- <th scope="col" ><i class="fa-solid fa-layer-group"></i> Image</th> -->
                                <!-- <th></th> -->
                                <th></th>
                            </tr>
                        </thead>
                        <tbody v-for="(_user,index) in users" :key="index">
                            <tr>
                                <th scope="row">{{ (pageN-1)*6+index+1 }}</th>
                                <td>{{ _user.id.length > 20 ? _user.id.slice(0, 20) + '...' : _user.id }}</td>
                                <td>{{ _user.email.length > 30 ? _user.email.slice(0, 30) + '...' : _user.email }}</td>
                                <td>{{ _user.fullname }}</td>
                                <td>{{ _user.phone }}</td>
                                <!-- <td>{{ user.vector }}</td> -->
                                <!-- <td>{{ user.url_video }}</td> -->
                                <!-- <td>{{ processDate(_user.create_at) }}</td>
                                <td>{{ processDate(_user.update_at) }}</td> -->
                                <!-- <td>{{ user.update_time != null ? user.update_time.slice(0, 26) : user.update_time }}</td> -->
                                <!-- <td style=""><button type="button" class="btn btn-outline-primary" @click="editRole(ad.id,ad.role)">Save</button></td> -->
                                <td style="display: flex;justify-content: center;"><button type="button" class="btn btn-outline-primary" @click="viewDetails(_user.id,_user)" data-toggle="modal" data-target="#exampleModalDelete"><i class="fa-solid fa-calendar-day"></i> View</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div id="divpaginate2">
                    <paginate class="pag" id="nvm"
                        :page-count="Math.ceil(this.quantity/6)"
                        :page-range="3"
                        :margin-pages="2"
                        :click-handler="clickCallback"
                        :initial-page="this.pageN"
                        :prev-text="'Prev'"
                        :next-text="'Next'"
                        :container-class="'pagination'"
                        :page-class="'page-item'">
                    </paginate>
                </div>
            </div>
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
    name:"AdminStatistical",
    components:{
        Notification,
        ParticleVue32,
        LineChart,
        DoughnutChart,
        BarChart,
        Paginate
    },
    setup() {
        // document.title = "Meta Shop - Statistical"
    },
    data(){
        return {
            user:{
                id:'',
                fullname:'',
                email:'',
                phone:'',
                password:'',
                create_at:'',
                update_at:'',
            },
            num_user:0,
            users:[],
            quantity:null,
            pageN:1,
            pageSize:6,
            quantity:null,
        }
    },
    mounted(){
        this.admin = JSON.parse(window.localStorage.getItem('admin'));
        document.title = "Statistical - PBL5";
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Statistical Success !');

        // number of users
        BaseRequest.get('num-user/')
        .then( data => {
            this.num_user = data.so_nhan_vien;
        })
        .catch( () => {})

        // user management
        BaseRequest.get('user-list/?page=1')
        .then( data => {
            this.users = data.results;
            this.quantity = data.count;
        })
        .catch( () => {
        })

    },
    methods:{
        formatDate(date) {
            const year = date.getFullYear();
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const day = String(date.getDate()).padStart(2, '0');
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const seconds = String(date.getSeconds()).padStart(2, '0');
            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },
        processDate(dateString){
            const date = new Date(dateString);
            const hours = date.getHours();
            const minutes = date.getMinutes();
            const seconds = date.getSeconds();
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
            return(`${day}/${month}/${year} ${hours}:${minutes}:${seconds}`);
        },
        getUsers(n) {
            BaseRequest.get('user-list/?page='+n)
                .then( data => {
                this.users = data.results;
                this.quantity = data.count;
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Get All User Success !');
            })
            .catch( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Get All User Fail !');
            })
        },
        clickCallback:function(pageNum){
            this.pageN = pageNum;
            this.getUsers(pageNum);
        },
        viewDetails:function(id_user,user){
            window.localStorage.setItem('user_statistical',JSON.stringify(user));
            this.$router.push({name:'StatisticalDetails',params:{id:id_user}}); 
        }
    },
    watch:{
    }
}
</script>

<style scoped>
  #statistical{
    position: relative;
    /* background-color: #F2F4F6; */
    padding: 30px 40px;
    /* height: 800px; */
    min-width: 100%;
  }
  
  #detail_statistical{
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 20px 40px !important;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    font-weight: bold;
  }
</style>
