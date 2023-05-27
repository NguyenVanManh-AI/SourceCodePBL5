<template>
    <div class="_view-user">
        <ParticleVue32></ParticleVue32>
        <div class="_view-user-min" >
            <div class="_content">
                <!-- <h1 class="text-center" style="font-size: 26px;font-weight: bold;color: #0085FF;"><i class="fa-solid fa-address-card"></i> Update Profile</h1> -->
                <br>
        <form style="border-radius: 10px;background-color: white;" class="p-4 col-10 mx-auto" @submit.prevent="save()">
            <div class="row" >
                    <div class="col-12">
                        <div style="margin-top: 30px;margin-bottom: 20px;color:gray"><i class="fa-solid fa-address-card"></i> UPDATE PROFILE</div>
                    </div>
                </div>
            <div class="form-group row">
                <label for="staticEmail" class="col-sm-2 col-form-label"><i class="fa-solid fa-at"></i> Full Name</label>
                <div class="col-sm-10">
                    <input type="text" v-model="admin.fullname" required class="form-control-plaintext" placeholder="Full Name">
                </div>
            </div>
            <div class="form-group row">
                <label for="staticEmail" class="col-sm-2 col-form-label"><i class="fa-solid fa-envelope"></i> Email</label>
                <div class="col-sm-10">
                    <input type="email" disabled v-model="admin.email" required class="form-control-plaintext" placeholder="email@example.com">
                </div>
            </div>
            <div class="form-group row">
                <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-phone"></i> Phone</label>
                <div class="col-sm-10">
                    <input type="tel" v-model="admin.phone" required class="form-control-plaintext" placeholder="Phone">
                </div>
            </div>
            <div class="form-group row">
                <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-calendar-plus"></i> Create At</label>
                <div class="col-sm-10">
                    <input v-model="admin.create_at" type="text" disabled required class="form-control-plaintext" >
                </div>
            </div>
            <div class="form-group row">
                <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-calendar-check"></i> Update At</label>
                <div class="col-sm-10">
                    <input v-model="admin.update_at" type="text" disabled required class="form-control-plaintext" >
                </div>
            </div>
            <button type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-floppy-disk"></i> Save </button>
            <!-- <button type="submit" class="btn btn-outline-success"><i class="fa-solid fa-floppy-disk"></i> Save</button> -->
        </form>
        <!-- <hr> -->
        <br>
        <!-- <button @click="logout" type="button" class="btn btn-danger"><i class="fa-solid fa-arrow-right-from-bracket"></i> Logout</button> -->
        <!-- <Notification></Notification> -->
    </div>
    </div>
    </div>
</template>

<script>
import { fireStoreCore } from './../../../configs/firebase';
import firebase from 'firebase/compat/app';
import useEventBus from '../../../composables/useEventBus'
// import Notification from './../Notification'
import ParticleVue32 from "../../particle/ParticleVue32.vue";
import BaseRequest from '../../../restful/user/core/BaseRequest';

export default {
    name: "AdminProfile",
    components: {
        // Notification
        ParticleVue32
    },
    data(){
        return{
            admin:{
                id:null,
                email:null,
                role:null,
                password:null,
                fullname:null,
                url_video:null,
                phone:null,
                create_at:null,
                update_at:null,
            }
        }
    },
    mounted(){
        this.admin = JSON.parse(window.localStorage.getItem('admin'));
        if(this.admin.fullname) {
            window.document.title = this.admin.fullname + ' - PBL5';
        }
        else {
            window.document.title = 'Profile Admin - PBL5';
        }
    },
    methods: {
        convertTimestampToDatetime(timestamp) {
            const date = new Date(timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000);
            return date.toLocaleString();
        },
        save() {
            BaseRequest.patch('users/'+this.admin.id+'/',this.admin)
            .then( (data) =>{
                this.admin = data;
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Edit Information Success !');
                window.localStorage.setItem('admin',JSON.stringify(this.admin));
                setTimeout(()=>{
                    window.location=window.location.href;
                }, 1500);
            }) 
            .catch(()=>{
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Edit Information Fail !');
            })
        },
    }
}
</script>
<style scoped>
form {
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 10px 40px !important;
    padding-bottom: 20px !important;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    font-weight: bold;
}
.blue, label {
    color: #F84B2F !important;
}

  /* btn login */
  .btn-pers {
  position: relative;
  left: 50%;
  padding: 1em 2.5em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #F84B2F;
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
    box-shadow: 0px 15px 20px #fcc4bb;
    /* color: #fff; */
    transform: translate(-50%, -7px);
  }
  
  .btn-pers:active {
  transform: translate(-50%, -1px);
  }
</style>