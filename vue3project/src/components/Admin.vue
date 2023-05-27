<template>
    <div>
        <SidebarMenuAkahon v-if="admin"></SidebarMenuAkahon>
        <div id="view-user">
            <div id="view-user-min">
                <div id="content">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
  </template>
<script>

import SidebarMenuAkahon from './admin/Sidebar-menu-akahon.vue';
import useEventBus from './../composables/useEventBus' 

export default {
    name : "AdminComp",
    components: {
        SidebarMenuAkahon
    },
    data(){
        return{
            admin:null,
        }
    },
    created(){

    },
    mounted(){
        this.admin = window.localStorage.getItem('admin');
        const { onEvent } = useEventBus()
        onEvent('eventLogout',()=>{
            this.admin = null;
            this.$router.push({name:"AdminLogin"});
            window.location = window.location.href;
        })
    },
    methods:{
        
    },
}
</script>
<style >
.blue, label {
    color: #F84B2F !important;
}

._view-user {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: white;
}
._view-user-min {
    box-shadow: rgba(99, 127, 152, 0.48) 6px 2px 16px 0px, rgba(255, 255, 255, 0.8) -6px -2px 16px 0px;
    border-radius: 20px;
    height: 93vh;
    width: 96%;
    padding: 16px;
}
._content {
    width: 100%;
    height: 100%;
    overflow: hidden;
    overflow-y: scroll;
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
  background-color: #F84B2F !important;
  /* background-color: #F84B2F; */
  box-shadow: 0px 15px 20px #ffbea5;
  color: #fff;
  transform: translate(-50%, -7px);
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}
/* btn Login */

</style>