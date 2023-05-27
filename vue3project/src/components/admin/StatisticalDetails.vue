<template>
    <div id="statistical">
        <ParticleVue32></ParticleVue32>
        <div id="detail_statistical" class="col-12" style="background-color: white;">
            <div style="margin-top: 10px;margin-bottom: 20px;color:gray;text-align: center;font-size: 23px;"><i class="fa-solid fa-calendar-check" style="margin-right: 10px;"></i>Detailed statistics for each employee in <span style="color: green;"><span><span v-if="_currentMonth<10">0</span>{{ _currentMonth }}/{{ currentYear }}</span></span></div>
            <div>
                <table class="table table-hover table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col" ><i class="fa-solid fa-envelope"></i> Email</th>
                        <th scope="col" ><i class="fa-solid fa-at"></i> Full Name</th>
                        <th scope="col" ><i class="fa-solid fa-phone"></i> Phone</th>
                        <th scope="col" ><i class="fa-regular fa-calendar-plus"></i> Create At</th>
                        <th scope="col" ><i class="fa-solid fa-calendar-plus"></i> Update At</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ user_statistical.id.length > 20 ? uuser_statisticalser.id.slice(0, 20) + '...' : user_statistical.id }}</td>
                        <td>{{ user_statistical.email.length > 30 ? user_statistical.email.slice(0, 30) + '...' : user_statistical.email }}</td>
                        <td>{{ user_statistical.fullname }}</td>
                        <td>{{ user_statistical.phone }}</td>
                        <td>{{ processDate(user_statistical.create_at) }}</td>
                        <td>{{ processDate(user_statistical.update_at) }}</td>
                    </tr>
                </tbody>
            </table>
            </div>
            <div>
                <form>
                    <div class="form-group row">
                        <label class="col-sm-1 col-form-label">Month</label>
                        <div class="col-sm-2">
                            <select @change="statisticalMonth" class="form-control col-12" id="exampleFormControlSelect1" v-model="_currentMonth">
                                <!-- +currentMonth là ép kiểu về kiểu số 02 => 2 -->
                                <!-- <option v-if="1<= +currentMonth" value="1">January</option>
                                <option v-if="2<= +currentMonth" value="2">February</option>
                                <option v-if="3<= +currentMonth" value="3">March</option>
                                <option v-if="4<= +currentMonth" value="4">April</option>
                                <option v-if="5<= +currentMonth" value="5">May</option>
                                <option v-if="6<= +currentMonth" value="6">June</option>
                                <option v-if="7<= +currentMonth" value="7">July</option>
                                <option v-if="8<= +currentMonth" value="8">August</option>
                                <option v-if="9<= +currentMonth" value="9">September</option>
                                <option v-if="10<=+currentMonth" value="10">October</option>
                                <option v-if="11<=+currentMonth" value="11">November</option>
                                <option v-if="12<=+currentMonth" value="12">December</option> -->
                                <option value="1">January</option>
                                <option value="2">February</option>
                                <option value="3">March</option>
                                <option value="4">April</option>
                                <option value="5">May</option>
                                <option value="6">June</option>
                                <option value="7">July</option>
                                <option value="8">August</option>
                                <option value="9">September</option>
                                <option value="10">October</option>
                                <option value="11">November</option>
                                <option value="12">December</option>
                            </select>
                        </div>
                    </div>
                </form>
                <div class="container">
                    <div class="box" v-for="(day,index) in daysInMonth" :key="index">
                        <div v-if="_currentMonth < +currentMonth">
                            <div class="box_inner" :class="{'green':works.includes(day),'red':!works.includes(day)}">
                                <span v-if="works.includes(day)" style="color: green;"><i class="fa-solid fa-circle-check"></i></span>
                                <span v-if="!works.includes(day)" :class="{'red':!works.includes(day)}"><i class="fa-solid fa-xmark"></i></span>
                                <br>
                                <span v-if="day<10">0</span>{{ day }} - <span v-if="_currentMonth<10">0</span>{{ _currentMonth }} - {{ currentYear }}
                            </div>
                        </div>

                        <div v-if="_currentMonth== +currentMonth">
                            <div class="box_inner" :class="{'green':works.includes(day),'red':!works.includes(day),'silver':day>currentDay}">
                                <span v-if="works.includes(day)" style="color: green;"><i class="fa-solid fa-circle-check"></i></span>
                                <span v-if="!works.includes(day)" :class="{'red':!works.includes(day),'silver':day>currentDay}"><i class="fa-solid fa-xmark" v-if="day<=currentDay"></i></span>
                                <br>
                                <span v-if="day<10">0</span>{{ day }} - {{ currentMonth }} - {{ currentYear }}
                            </div>
                        </div>

                        <div v-if="_currentMonth > +currentMonth">
                            <div class="box_inner silver">
                                <br>
                                <span v-if="day<10">0</span>{{ day }} - <span v-if="_currentMonth<10">0</span>{{ _currentMonth }} - {{ currentYear }}
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="text_center">
                    Number of working days in <span class="month_year"><span v-if="_currentMonth<10">0</span>{{ _currentMonth }}/{{ currentYear }}</span> is : <span style="color:green;margin-left: 5px;">{{ count }}</span> 
                </div>
                <div class="text_center" v-if="_currentMonth < + currentMonth">
                    Number of days off in <span class="month_year"><span v-if="_currentMonth<10">0</span>{{ _currentMonth }}/{{ currentYear }}</span> is : <span style="color:red;margin-left: 5px;">{{ daysInMonth - count }}</span> 
                </div>

                <div class="text_center" v-if="_currentMonth == + currentMonth">
                    Number of days off in <span class="month_year"><span v-if="_currentMonth<10">0</span>{{ _currentMonth }}/{{ currentYear }}</span> is : <span style="color:red;margin-left: 5px;">{{ currentDay - count }}</span> 
                </div>

                <div class="text_center" v-if="_currentMonth > + currentMonth">
                    Number of days off in <span class="month_year"><span v-if="_currentMonth<10">0</span>{{ _currentMonth }}/{{ currentYear }}</span> is : <span style="color:red;margin-left: 5px;">0</span> 
                </div>
                <br>
                <hr v-if="check_in">
                <br v-if="check_in">
                <div v-if="check_in">
                    <div style="margin-top: 10px;margin-bottom: 20px;color:gray;text-align: center;font-size: 23px;">Today's attendance information</div>
                    <div class="col-12 mx-auto">
                        <table class="table table-bordered">
                            <thead class="thead-light">
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Image</th>
                                    <th scope="col">Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">1</th>
                                    <td style="display: flex;justify-content: center;"><img width="300" :src="check_in.image" alt="Check In"></td>
                                    <td>{{ check_in.checkin }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
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
    name:"StatisticalDetails",
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
            id_user:null,
            status:true,
            works:[],
            checkday:true,
            day:null,
            daysInMonth:0, // số ngày của tháng hiện tại 
            currentDay:null, // ngày hiện tại 
            currentMonth:null, // tháng hiện tại 
            currentYear:null, // năm hiện tại 
            count:null, // số ngày làm trong tháng 
            _currentMonth:1,

            // Thông tin chi tiết của user đó 
            user_statistical:{
                id:'',
                fullname:'',
                email:'',
                phone:'',
                password:'',
                create_at:'',
                update_at:'',
            },

            // check in 
            check_in : {
                id_user:null,
                image:null,
                checkin:null,
            }
        }
    },
    mounted(){
        this.admin = JSON.parse(window.localStorage.getItem('admin'));
        const { emitEvent } = useEventBus();
        emitEvent('eventSuccess','Statistical Success !');

        // id_user 
        var url = window.location.href; 
        var parts = url.split("/");
        this.id_user = parts[parts.length - 1];

        // Lấy ngày hiện tại
        var currentDate = new Date();
        var currentDay = currentDate.getDate();
        var currentMonth = currentDate.getMonth() + 1;
        this._currentMonth = currentMonth;
        var currentYear = currentDate.getFullYear();

        // Lấy số ngày của tháng 
        // Tạo một đối tượng Date mới với ngày đầu tiên của tháng kế tiếp
        var nextMonthFirstDay = new Date(currentYear, currentMonth, 1);
        // Tạo một đối tượng Date mới với ngày cuối cùng của tháng hiện tại
        var currentMonthLastDay = new Date(nextMonthFirstDay.getTime() - 1);
        // Lấy số ngày trong tháng hiện tại
        this.daysInMonth = currentMonthLastDay.getDate();

        if(currentDay<10) currentDay = '0'+currentDay;
        if(currentMonth<10) currentMonth = '0'+currentMonth;
        var day = currentYear + '-' + currentMonth + '-' + currentDay;
        this.day = day;

        BaseRequest.get('attendance/'+this.id_user+'/'+currentYear+'/'+currentMonth+'/')
        .then( (data) =>{
            this.count = data.count;
            for(var i=0; i<data.count; i++){
                var day = data.results[i].date.split('-')[2]; // lấy ngày 
                day = day.replace(/^0+/, ''); // chuyển "02" thành "2";
                day = +day;// ép sang kiểu số 
                this.works.push(day);
            }
            const { emitEvent } = useEventBus();
            emitEvent('eventSuccess','Get Attentdance Success !');
        }) 
        .catch(()=>{
            const { emitEvent } = useEventBus();
            emitEvent('eventError','Get Attentdance Fail !');
        })

        BaseRequest.get('checkins/?id_user='+this.id_user)
        .then( (data) =>{
            this.check_in =  data.results[0];
        }) 
        .catch(()=>{
        })

        this.currentDay = currentDay;
        this.currentMonth = currentMonth;
        this.currentYear = currentYear;

        // Thông tin chi tiết của user đó 
        this.user_statistical = JSON.parse(localStorage.getItem('user_statistical'));
        if(this.user_statistical.fullname) document.title = this.user_statistical.fullname + " - Statistical Detail - PBL5";
        else document.title = "Statistical Detail - PBL5";

    },
    methods:{
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
        statisticalMonth(){
            BaseRequest.get('attendance/'+this.user_statistical.id+'/'+this.currentYear+'/'+this._currentMonth+'/')
            .then( (data) =>{
                console.log(data);
                this.works = [];
                this.count = data.count;
                for(var i=0; i<data.count; i++){
                    var day = data.results[i].date.split('-')[2]; // lấy ngày 
                    day = day.replace(/^0+/, ''); // chuyển "02" thành "2";
                    day = +day;// ép sang kiểu số 
                    this.works.push(day);
                }
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Get Attentdance Success !');
            }) 
            .catch(()=>{
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Get Attentdance Fail !');
            })

            // Lấy số ngày của tháng 
            // Tạo một đối tượng Date mới với ngày đầu tiên của tháng kế tiếp
            var nextMonthFirstDay = new Date(this.currentYear, this._currentMonth, 1);
            // Tạo một đối tượng Date mới với ngày cuối cùng của tháng hiện tại
            var currentMonthLastDay = new Date(nextMonthFirstDay.getTime() - 1);
            // Lấy số ngày trong tháng hiện tại
            this.daysInMonth = currentMonthLastDay.getDate();
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
    padding: 10px 40px;
    /* height: 800px; */
    min-width: 100%;
  }
  
  #detail_statistical{
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 10px 40px !important;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    font-weight: bold;
  }


.container {
  display: flex;
  flex-wrap: wrap;
  padding: 0px;
  margin: 0px;
}

.box {
  width: calc(100% / 7);
  height: 100px;
  padding: 5px;
}
.box_inner {
    /* border: 1px solid black; */
    width: 100%;
    height: 100%;
    border-radius: 5px;
    padding: 5px;
    text-align: center;
    /* background-color: rgba(255, 255, 255, 0.545); */
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding-top: 20px;
}
.green {
    color: green;
}
.red {
    color: red;
}

.silver {
    color: silver;
}

.text_center {
    display: flex;
    align-items: center;
    align-content: center;
    line-height: 100%;
    margin-bottom: 15px;
}

.month_year {
    color: #0085FF;
    margin: 0px 6px;
}
</style>
