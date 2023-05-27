<template>
  <div >
    <div>
      <canvas id="myChart"></canvas>
    </div>
  </div>
</template>

<script >
// import {Chart} from 'chart.js'
import useEventBus from '../../../composables/useEventBus'
import Chart from 'chart.js/auto';
// import BaseRequest from '../../../restful/admin/core/BaseRequest';
import BaseRequest from '../../../restful/user/core/BaseRequest'

export default {
  name: 'LineChart' ,
  data(){
    return{
        // datas_revenue:[2,4,3,5,6,6,3,9,1,3,0,2,1],
        // datas_import:[1,2,3,4,4,3,5,6,7,3,2,3,4,6],
        labels_line:['January','February','March','April','May','June','July','August','September','October','November','December']
    }
  },
  mounted(){
    BaseRequest.get('year-absentee/')
    .then( data => {
      var datas_revenue= data;
      var ctx = document.getElementById('myChart');
      var data = {
        labels: this.labels_line,
        datasets: [
          {
            label: 'Absent',
            data: datas_revenue,
            fill: false,
            borderColor: 'green',
            tension: 0.1
          },
          // {
          //   label: 'Present',
          //   data: this.datas_import,
          //   fill: false,
          //   borderColor: 'rgb(0, 190, 248)',
          //   tension: 0.1
          // }
        ]
      };
      var mc = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
          scales: {
            x : {
              title: {
                display: true,
                text: 'The months of the year'
              },
            },
            y: {
                ticks: {
                    // callback: function(value, index, ticks) {
                    callback: function(value) {
                      return new Intl.NumberFormat().format(value);
                    }
                },
                title: {
                  display: true,
                  text: 'Absent'
                },
            }
          },
          plugins: {
            // title: {
            //     display: true,
            //     text: 'Custom Chart Title',
            //     padding: {
            //         top: 10,
            //         bottom: 30
            //     }
            // }
          }
        }
      });
      const { onEvent } = useEventBus()
      onEvent('eventAdminStatistical',ob=>{
        mc.destroy(); // RẤT QUAN TRỌNG , biểu đồ trước đó phải được hủy thì mới tạo lại được biểu đồ mới 
        // https://stackoverflow.com/questions/40056555/destroy-chart-js-bar-graph-to-redraw-other-graph-in-same-canvas
        data = {
            labels: ob.labels_line,
            datasets: [
              {
                label: 'Revenue',
                data: ob.datas_revenue,
                fill: false,
                borderColor: 'green',
                tension: 0.1
              },
              {
                label: 'Import goods',
                data: ob.datas_import,
                fill: false,
                borderColor: 'rgb(0, 190, 248)',
                tension: 0.1
              }
            ]
          };
          mc = new Chart(ctx, {
            type: 'line',
            data: data,
            options: {
              scales: {
                x : {
                  title: {
                    display: true,
                    text: 'Time'
                  },
                },
                y: {
                  ticks: {
                      callback: function(value) {
                        return new Intl.NumberFormat().format(value);
                      }
                  },
                  title: {
                    display: true,
                    text: 'Money'
                  },
                }
              },
              plugins: {
                // title: {
                //     display: true,
                //     text: 'Custom Chart Title',
                //     padding: {
                //         top: 10,
                //         bottom: 30
                //     }
                // }
              }
            }
          });
      });
    })
    .catch( () => {})
  },
}

</script>
