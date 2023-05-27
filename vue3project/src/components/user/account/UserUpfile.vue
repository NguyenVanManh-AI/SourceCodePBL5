<template>
    <div >
        <div>
            <router-link :to="{ name: 'UserAccount' }"> My Account </router-link><i class="fa-solid fa-angles-right"></i>
            <router-link :to="{ name: 'UserUpfile' }"> Upfile </router-link>
        </div>
        <br>
        <hr>
        <br>
        <div class="col-sm-12" >
            <div class="row">
                <div class="col-12" id="uploadimg">
                    <div class="newimg col-4"><FilePicker></FilePicker></div>
                    <div class="preview-box col-8" v-if="images!=null">
                        <p>Old image</p>
                        <div v-for="(image,index) in images" :key="index" class="img-container"> 
                            <img :src="API_URL + image.image_path" class="preview-img" >
                            <img  src="../../../assets/error.png" v-on:click="removeFile(index);" class="close" alt="Remove">
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <button class="col-2 btn btn-outline-success mx-auto mt-4" v-on:click="funcUpdateProduct()"><i class="fa-solid fa-floppy-disk"></i> Save</button>
            </div>

        </div>
        <!-- <div class="mt-6">
            <op  v-for="(image,index) in images" :key="index">
                <span>
                    {{ API_URL + image.image_path }}
                </span>
                <img style="width: 100px;display: inline-block;" :src="API_URL + image.image_path">
            </op>
        </div> -->
        <br>
        <hr>
        <br>
        <button @click="logout" type="button" class="btn btn-danger"><i class="fa-solid fa-arrow-right-from-bracket"></i> Logout</button>
        <Notification></Notification>
    </div>
</template>

<script>
import FilePicker from './FilePicker.vue';
import config from '../../../config.js'; /// +++
import BaseRequest from '../../../restful/user/core/BaseRequest'; /// +++
import useEventBus from '../../../composables/useEventBus' /// +++
import Notification from './../Notification'

export default {
    name: "UserUpfile",
    components: {
        FilePicker,
        Notification
    },
    data(){
        return{
            user:{
                id:'',
                fullname:'',
                email:'',
                phone:'',
                img_url:'',
                vector:'',
                password:'',
                create_at:'',
                update_at:'',
            },
            images:null,
            API_URL:config.API_URL,
            imgRemove:[],
        }
    },
    mounted(){

        this.user = JSON.parse(window.localStorage.getItem('user')); /// +++

        BaseRequest.get('api/images?id_user='+this.user.id,{
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log(response);
          this.images = response.data;
          const { emitEvent } = useEventBus();
          emitEvent('eventSuccess','Get all images successfully !');
        })
        .catch(error => {
          console.log(error);
          const { emitEvent } = useEventBus();
          emitEvent('eventError','Get all images fail !');
        });
    },
    methods: {
        removeFile:function(index){
            this.imgRemove.push(this.images[index].id);
            this.images.splice(index, 1);
        },
        funcUpdateProduct:function(){
            var s = this.imgRemove.toString(); // nó mặt định sẽ chuyển [1,2,3,4,5] => '1,2,3,4,5'
            // ngăn cách nhau bởi dấu ',' => lên server split ra 
            BaseRequest.get('api/update-images?id_removeimages='+s)
            .then( (data) =>{
                console.log(data);
                const { emitEvent } = useEventBus();
                emitEvent('eventUpfile');
                // setTimeout(()=>{emitEvent('eventResetUpfile');}, 2000);

                emitEvent('eventSuccess','Update avatars successfully !'); // 1
                // nguyên nhân là do bất đồng bộ => 1,2 chạy trước cả event eventUpfile nên ảnh không được upload lên 
                // setTimeout(()=>{window.location=window.location.href;}, 2000); // 2
            }) 
            .catch(error=>{
                console.log(error);
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Update avatars false !');
            })
        },
        logout(){
            window.localStorage.removeItem('user');
            this.$router.push({name:'UserLogin'}); 
        }
    }
}
</script>
<style scoped>
#selectcate option:hover {
    background-color: #0085FF;
    color:white;
}

/* HIỂN THỊ CÁC ẢNH CŨ */
.img-container{
    position: relative;
    display: inline-block;
    padding: 10px;
}
.preview-img{
    width: 80px;
    padding: 10px;
    border: 1px dotted #b3b3b39e;
}
.preview-box{
    display: inline-block;
    width: 55%;
    background-color: white;
    border-radius: 20px;
    padding: 10px 10px;
    min-height: 300px;
    min-width: 300px;

    background-color: #ffffff;
    -webkit-box-shadow: 2px 4px 20px 2px #dadada;
    box-shadow: 2px 4px 20px 2px #dadada;
    margin-left: 20px;
}
.close{
    position: absolute;
    top: 0px;
    right: 0px;
    width: 20px;
}

/* HIỂN THỊ CÁC ẢNH CŨ */

/* HIỂN THỊ ẢNH MỚI */
#uploadimg{
    display: flex;
}
.newimg{
    min-width: 10%;
}
</style>