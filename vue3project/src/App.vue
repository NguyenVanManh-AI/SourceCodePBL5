<template>
  <div class="">
    <router-view></router-view>
    <Notification></Notification>
  </div>
</template>

<script>

import Notification from './components/Notification';
export default {
  name: 'App',
  components:{
    Notification,
  },
  data(){
    return {

    }
  },
  mounted(){

  }
}
</script>

<style >
.modal-header .close {
    padding-right: 40px !important;
    padding-top: 20px !important;
}
.blue,label {
    color: #0085FF;
}
::-webkit-scrollbar {
  width: 13px;
}

::-webkit-scrollbar-track { 
  background: white; 
}
 
::-webkit-scrollbar-thumb {
    background: #888;  
    border-radius: 10px;
    border: 3px solid transparent;
    background-clip: content-box;
}

::-webkit-scrollbar-thumb:hover {
    background: #0085FF; 
    border-radius: 10px;
    border: 3px solid transparent;
    background-clip: content-box;
}

#view{
  display: grid;
  width: 100%;
  overflow-y: scroll;
}
#view::-webkit-scrollbar {
    display: none;
}
/* Hide scrollbar for IE, Edge and Firefox */
#view {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}







/* btn Login */
.btn-pers {
  position: relative;
  left: 50%;
  padding: 1em 2.5em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #000;
  background-color: #fff;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  transform: translateX(-50%);
}

.btn-pers:hover {
  background-color: #0085FF;
  /* background-color: #F84B2F; */
  box-shadow: 0px 15px 20px #adcdfc;
  color: #fff;
  transform: translate(-50%, -7px);
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}
/* btn Login */
</style>
