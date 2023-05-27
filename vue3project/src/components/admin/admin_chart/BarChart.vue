<template>
  <div >
    <div>
      <canvas id="barChart"></canvas>
    </div>
  </div>
</template>

<script >
import Chart from 'chart.js/auto';
// import useEventBus from '../../../composables/useEventBus'
import BaseRequest from '../../../restful/user/core/BaseRequest'

export default {
    name: 'BarChart' ,
    data(){
        return {

        }
    },
    mounted(){

        BaseRequest.get('week-absentee/')
        .then( data => {
            var barChart = document.getElementById('barChart');
            var labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
            var data = {
                labels: labels,
                datasets: [{
                    label: 'Absent',
                    data: data ,
                    backgroundColor: [
                        'rgb(29, 215, 48, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                        'rgb(29, 215, 48)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                    ],
                    borderWidth: 1
                }]
            };
            new Chart(barChart, {
                type: 'bar',
                data: data,
                options: {
                    scales: {
                        x : {
                            title: {
                                display: true,
                                text: 'Days of week'
                            },
                        },
                        y:{
                            title: {
                                display: true,
                                text: 'Absent'
                            },
                        }
                    }
                },
            });
        })
        .catch( () => {})

    // const { onEvent } = useEventBus()
    // onEvent('eventBarChart',data_chart=>{
    // });
    },
}

</script>
