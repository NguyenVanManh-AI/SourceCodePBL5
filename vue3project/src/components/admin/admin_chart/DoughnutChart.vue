<template>
  <div style="margin-left: 0px;">
    <div>
        <div class="form-group">
            <label for="exampleFormControlSelect1">Absence and late statistics</label>
            <select class="form-control" id="exampleFormControlSelect1" @change="SelectTime()" v-model="time">
                <option value="day">Day</option>
                <option value="month">Month</option>
                <option value="year">Year</option>
            </select>
        </div>
      <canvas id="myChart2"></canvas>
    </div>
  </div>
</template>

<script >
  // import {Chart} from 'chart.js'
import Chart from 'chart.js/auto';
import useEventBus from '../../../composables/useEventBus'
// import BaseRequest from '../../../restful/admin/core/BaseRequest';
import BaseRequest from '../../../restful/user/core/BaseRequest'

export default {
    name: 'DoughnutChart' ,
    data(){
        return {
            labels_donut : ['Arrive on time','Late','Off work'],
            time:'month',
            mc:null,
        }
    },
    mounted(){
        BaseRequest.get('attendance-month/')
        .then( data => {
            var data_donut = [];
            data_donut.push(data.dung_gio);
            data_donut.push(data.tre_gio);
            data_donut.push(data.vang_mat);
            const ctx = document.getElementById('myChart2');
            var data = {
                labels: this.labels_donut,
                datasets: [{
                    label: 'Order number',
                    data: data_donut,
                    backgroundColor: [
                        '#008037',
                        'rgb(255, 205, 86)',
                        'rgb(255, 99, 132)',
                    ],
                    hoverOffset: 4
                }]
            };
            this.mc = new Chart(ctx, {
                type: 'doughnut',
                data: data,
                options: {
                    plugins: {
                    }
                }
            });
        })
        .catch( () => {})
    },
    methods:{
        SelectTime(){
            var data_donut = [];
            if(this.time == 'year'){
                BaseRequest.get('attendance-year/')
                .then( data => {
                    data_donut.push(data.dung_gio);
                    data_donut.push(data.tre_gio);
                    data_donut.push(data.vang_mat);
                    this.mc.destroy(); 
                    const ctx = document.getElementById('myChart2');
                    var data = {
                        labels: this.labels_donut,
                        datasets: [{
                            label: 'Order number',
                            data: data_donut,
                            backgroundColor: [
                                '#008037',
                                'rgb(255, 205, 86)',
                                'rgb(255, 99, 132)',
                            ],
                            hoverOffset: 4
                        }]
                    };
                    this.mc = new Chart(ctx, {
                        type: 'doughnut',
                        data: data,
                        options: {
                            plugins: {
                            }
                        }
                    });
                })
                .catch( () => {})
            }
            else if (this.time == 'month'){
                BaseRequest.get('attendance-month/')
                .then( data => {
                    data_donut.push(data.dung_gio);
                    data_donut.push(data.tre_gio);
                    data_donut.push(data.vang_mat);
                    this.mc.destroy(); 
                    const ctx = document.getElementById('myChart2');
                    var data = {
                        labels: this.labels_donut,
                        datasets: [{
                            label: 'Order number',
                            data: data_donut,
                            backgroundColor: [
                                '#008037',
                                'rgb(255, 205, 86)',
                                'rgb(255, 99, 132)',
                            ],
                            hoverOffset: 4
                        }]
                    };
                    this.mc = new Chart(ctx, {
                        type: 'doughnut',
                        data: data,
                        options: {
                            plugins: {
                            }
                        }
                    });
                })
                .catch( () => {})
            }
            else {
                BaseRequest.get('attendance-day/')
                .then( data => {
                    data_donut.push(data.dung_gio);
                    data_donut.push(data.tre_gio);
                    data_donut.push(data.vang_mat);
                    this.mc.destroy(); 
                    const ctx = document.getElementById('myChart2');
                    var data = {
                        labels: this.labels_donut,
                        datasets: [{
                            label: 'Order number',
                            data: data_donut,
                            backgroundColor: [
                                '#008037',
                                'rgb(255, 205, 86)',
                                'rgb(255, 99, 132)',
                            ],
                            hoverOffset: 4
                        }]
                    };
                    this.mc = new Chart(ctx, {
                        type: 'doughnut',
                        data: data,
                        options: {
                            plugins: {
                            }
                        }
                    });
                })
                .catch( () => {})
            }
        }
    }
}

</script>
