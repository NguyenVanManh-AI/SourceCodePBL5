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
                                <div style="margin-top: 30px;margin-bottom: 20px;color:gray;font-weight: bold;"><i class="fa-solid fa-repeat"></i> UPDATE PROFILE</div>
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"><i class="fa-solid fa-at"></i> Full Name</label>
                            <div class="col-sm-10">
                                <input type="text" v-model="user.fullname" required class="form-control-plaintext" placeholder="Full Name">
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="staticEmail" class="col-sm-2 col-form-label"><i class="fa-solid fa-envelope"></i> Email</label>
                            <div class="col-sm-10">
                                <input disabled type="email" v-model="user.email" required class="form-control-plaintext" placeholder="email@example.com">
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-phone"></i> Phone</label>
                            <div class="col-sm-10">
                                <input type="tel" v-model="user.phone" required class="form-control-plaintext" placeholder="Phone">
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-photo-film"></i> File Video</label>
                            <div class="col-sm-10">
                                <div v-if="videoSrc == null && user.url_video">
                                    <video width="320" ref="player" controls :src="link_video" @ready="onPlayerReady"></video>
                                </div>
                                <div v-if="videoSrc">
                                    <video width="320" ref="player" controls :src="videoSrc" @ready="onPlayerReady"></video>
                                </div>
                                <div v-else>
                                    <input type="file" name="url_video" @change="handleFileUpload" accept="video/*" class="form-control-plaintext" placeholder="File Video">
                                </div>
                                <button v-if="videoSrc" type="button" class="mt-2 btn-sm btn btn-secondary" @click="remove">Remove</button>
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-calendar-plus"></i> Create At</label>
                            <div class="col-sm-10">
                                <!-- <input :value="convertTimestampToDatetime(user.create_at)" class="form-control-plaintext" type="text" disabled required > -->
                                <input v-model=user.create_at class="form-control-plaintext" type="text" disabled required >
                            </div>
                        </div>
                        <div class="form-group row">
                            <label for="inputPassword" class="col-sm-2 col-form-label"><i class="fa-solid fa-calendar-check"></i> Update At</label>
                            <div class="col-sm-10">
                                <input v-model=user.update_at type="text" disabled required class="form-control-plaintext" >
                            </div>
                        </div>
                        <button type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-floppy-disk"></i> Save </button>
                        <!-- <button type="submit" class="btn btn-outline-success"><i class="fa-solid fa-floppy-disk"></i> Save</button> -->
                    </form>
                    <!-- <button @click="logout" type="button" class="btn btn-danger"><i class="fa-solid fa-arrow-right-from-bracket"></i> Logout</button> -->
                    <!-- <Notification></Notification> -->
                    <br>
            </div>
        </div>
    </div>
</template>

<script>
import { fireStoreCore } from './../../../configs/firebase';
import firebase from 'firebase/compat/app';
import useEventBus from '../../../composables/useEventBus'
// import Notification from './../Notification'
import BaseRequest from '../../../restful/user/core/BaseRequest';
import VideoPlayer from 'vue-video-player';
import ParticleVue32 from "../../particle/ParticleVue32.vue";
import config from '../../../config.js';

export default {
    name: "UserProfile",
    components: {
        // Notification
        VideoPlayer,
        ParticleVue32
    },
    data(){
        return{
            user:{
                id:null,
                email:null,
                role:null,
                password:null,
                fullname:null,
                url_video:null,
                phone:null,
                create_at:null,
                update_at:null,
            },
            selectedFileVideo: null,
            videoSrc:null,
            link_video:null,
        }
    },
    mounted(){
        this.user = JSON.parse(window.localStorage.getItem('user'));
        if (this.user.url_video.includes('8000')) {
            this.link_video = this.user.url_video;
        } else {
            this.link_video = config.API_URL + this.user.url_video.slice(1);
        }
        if(this.user.fullname) {
            window.document.title = this.user.fullname + ' - PBL5';
        }
        else {
            window.document.title = 'Profile User - PBL5';
        }
    },
    methods: {
        convertTimestampToDatetime(timestamp) {
            const date = new Date(timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000);
            return date.toLocaleString();
        },
        async handleFileUpload(event) {
            this.selectedFileVideo = event.target.files[0];
            if (this.selectedFileVideo) {
                const blobUrl = URL.createObjectURL(this.selectedFileVideo);
                await this.$nextTick();
                this.videoSrc = blobUrl;
            } else {
                this.videoSrc = null;
            }
        },
        onPlayerReady() {
            this.$refs.player.play();
        },
        remove(){
            this.selectedFileVideo = null;
            this.videoSrc = null;
        },
        save() {
            const formData = new FormData();
            formData.append('fullname', this.user.fullname);
            formData.append('phone', this.user.phone);
            if(this.selectedFileVideo){
                formData.append('url_video', this.selectedFileVideo);
            }
            BaseRequest.patch('users/'+this.user.id+'/update/',formData)
            .then( (data) =>{
                this.user = data;
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Edit Information Success !');
                window.localStorage.setItem('user',JSON.stringify(this.user));
                setTimeout(()=>{
                    window.location=window.location.href;
                }, 1500);
            }) 
            .catch(()=>{
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Edit Information Fail !');
            })
        },
        // getNewUser(){
        //     fireStoreCore.collection('users').doc(this.user.id)
        //     .get()
        //     .then(doc => {
        //         if (doc.exists) {
        //             this.user = doc.data();
        //             this.user.id = doc.id;
        //             window.localStorage.setItem('user', JSON.stringify(this.user));
        //         } 
        //     })
        //     .catch({});
        //     window.localStorage.setItem('user',JSON.stringify(this.user));
        // },
        // logout(){
        //     window.localStorage.removeItem('user');
        //     this.$router.push({name:'UserLogin'}); 
        // }
    }
}
</script>
<style scoped>
form {
    width: 100%;
    background-color: #000;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 10px 40px;
    padding-bottom: 20px;
    border-radius: 10px;
    position: relative;
    background-color: white;
    background-color: rgba(255, 255, 255, 0.545);
    font-weight: bold;
}
</style>