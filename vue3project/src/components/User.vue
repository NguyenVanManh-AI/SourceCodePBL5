<template>
    <div>
        <SidebarMenuAkahon v-if="user"></SidebarMenuAkahon>
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

import SidebarMenuAkahon from './user/Sidebar-menu-akahon.vue';
import useEventBus from './../composables/useEventBus' 

export default {
    name : "UserComp",
    components: {
        SidebarMenuAkahon
    },
    data(){
        return{
            user:null,
        }
    },
    created(){

    },
    mounted(){
        window.document.title = "User Login - PBL5"
        this.$router.push({name:"UserProfile"});
        this.user = window.localStorage.getItem('user');
        const { onEvent } = useEventBus()
        onEvent('eventLogout',()=>{
            this.admin = null;
            this.$router.push({name:"UserLogin"});
            window.location = window.location.href;
        })
    },
    methods:{
        
    },
}
</script>
<style >
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
.blue, label {
    color: #0085FF !important;
}
.btn-pers:hover {
    background-color: #0085FF !important;
    box-shadow: 0px 15px 20px #86c1f8;
    color: #fff;
    transform: translate(-50%, -7px);
  }
</style>