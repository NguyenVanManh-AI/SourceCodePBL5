<template>
    <div id="main">
      <!-- HIỆU ỨNG BACKGROUND HÌNH TRÒN -->
      <div id="container-inside"> 
        <div id="circle-small"></div>
        <div id="circle-medium"></div>
        <div id="circle-large"></div>
        <div id="circle-xlarge"></div>
        <div id="circle-xxlarge"></div>
        <ParticleVue3></ParticleVue3>    
      <!-- HIỆU ỨNG BACKGROUND HÌNH TRÒN -->
        <br><br><br><br><br>
        <div id="big">
          <div class="container col-4">
              <form  @submit.prevent="login()" class="p-3">
                <!-- <div class="col-6 mx-auto"><router-link :to="{ name: 'DashboardMain' }" style="text-decoration: none !important;"><h2 style="font-weight: bold;font-size: 20px;color: #0076e5;" class="text-center"><i class="fa-solid fa-seedling"></i> PBL5</h2></router-link></div> -->
                <div class="col-6 mx-auto" style="text-decoration: none !important;"><h2 style="font-weight: bold;font-size: 20px;color: #F84B2F;" class="text-center"><i class="fa-solid fa-shield" style="margin-right: 5px;"></i>Admin PBL5</h2></div>
                <br>
                <div class="form-group row">
                  <label for="staticEmail" class="col-3 col-form-label pl-0 pr-0"><i class="fa-solid fa-envelope-circle-check"></i> Email </label> 
                  <input style="padding-left: 10px;" required v-model="user.email" type="email" class="form-control col-9" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <br>
                <div class="form-group row">
                  <label for="staticEmail" class="col-3 col-form-label pl-0 pr-0"><i class="fa-solid fa-key"></i> Password  </label> 
                  <input style="padding-left: 10px;" required v-model="user.password" type="password" class="form-control col-9" id="exampleInputPassword1" placeholder="Password">
                </div>
                <!-- <a class="under" style="text-decoration: none;color: #F84B2F;" href="#" data-toggle="modal" data-target="#exampleModalForgotPassword" >Forgot your password ? </a><br> -->
                <!-- <router-link :to="{ name: 'UserRegister' }"><a class="under float-right" style="text-decoration: none;color: #F84B2F;" href="#" data-toggle="modal" data-target="#exampleModalForgotPassword" ><i class="fa-solid fa-user-plus"></i> Register ? </a></router-link><br> -->
                <button type="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-paper-plane"></i> Login </button>
              </form>
            </div><br>
          </div>
          <div id="goUser" @click="gotoUser()">
            <i class="fa-solid fa-house"></i>
          </div>
      <!-- <Notification></Notification> -->
      </div>
    </div>
  </template>
  
  <script>
  // import BaseRequest from '../../restful/user/core/BaseRequest';
  // import Notification from './../Notification'
  
  import ParticleVue3 from "./../particle/ParticleVue3";
  // import config from '../../config.js';

// import bcrypt from 'bcryptjs';
// import { fireStoreCore } from './../../configs/firebase';
import useEventBus from '../../composables/useEventBus'
// import Notification from './Notification'
import LoginRequest from '../../restful/user/requests/LoginRequest'

  
  export default {
      name: "AdminLogin",
      components: {
        // Notification,
        ParticleVue3,
      },
      setup() {
        // document.title = "Meta Shop - Login";
      },
      data(){
          return {
            user:{
              email:'',
              password:''
            },
            error:null,
            showpw:false,
            passwordType:'password',
        }
      },
      mounted(){
  
        window.document.title='Login - PBL5';
        if(window.localStorage.getItem('admin')){
          this.$router.push({name:"AdminProfile"});
        }
  
        if (document.body.style.paddingLeft !== "0px") {
          document.body.style.paddingLeft = "0px";
        }
  
      },
      methods: {
        login:function(){
            var v = this.user;
            LoginRequest.post('login/',this.user)
            .then( data => {
              if(data.role == 'user'){
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Login fail !');
              }
              else {
                this.setdata(data);
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Login Success !');
                setTimeout(()=>{
                  // this.$router.push({name:'UserProfile'}); 
                  window.location = window.origin+'/admin/account/profile';
                }, 1000);
              }
            })
            .catch( () => {
              this.user = v; 
              const { emitEvent } = useEventBus();
              emitEvent('eventError','Login fail !');
            })
        },
        setdata:function(data){
            var user = {
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
            user = data;
            window.localStorage.setItem('admin',JSON.stringify(user));
        },
        gotoUser:function(){
          this.$router.push({name:"UserLogin"});
        }
      },
      watch:{
        /*
        showpw:function(){
          if(this.showpw == true) this.passwordType = 'text';
          else this.passwordType = 'password'; 
        }
        */
      },
  
  }
  </script>
  <style scoped>
    #goUser {
    position: absolute;
    width: 60px;
    height: 60px;
    border: 6px solid silver;
    transition: all 0.5s ease;
    border-radius: 30px;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    cursor: pointer;
    color: silver;
    left: 20px;
    bottom: 20px;
  }
  #goUser:hover {
    border: 6px solid #F84B2F;
    color: #F84B2F; 
  }
  .blue, label {
    color: #F84B2F !important;
}
  /* @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap'); */
  
  
  /* HIỆU ỨNG BACKGROUND HÌNH TRÒN */
  /* THAMKHAO : https://blog.stackfindover.com/css-background-animation-examples/ */
  /*  */
  /* RESET COLOR INPUT AND BUTTON */
  
  /* thay đổi màu cho button */
  .btn-pers:hover {
    background-color: #F84B2F !important;
    box-shadow: 0px 15px 20px #ff9180;
    color: #fff;
    transform: translate(-50%, -7px);
  }
  .btn-outline-primary,  .btn-outline-primary:active, .btn-outline-primary:visited {
  border-color: #F84B2F ;
  color: #F84B2F ;
  outline-color: #F84B2F;
  }
  .btn{
  transition: all 0.6s ease;
  }
  .btn:focus, .btn:active {
  outline: none !important;
  box-shadow: none !important;
  }
  .btn-outline-primary:hover{
  background-color: #F84B2F !important;
  border-color: #F84B2F ;
  }
  
  /* RESET COLOR INPUT AND BUTTON */
  #main{
      background: #F84B2F;
      background: -moz-linear-gradient(-45deg, #F84B2F 0%, #0076e5 100%);
      background: -webkit-linear-gradient(-45deg, #F84B2F 0%,#0076e5 100%);
      background: linear-gradient(135deg, #F84B2F 0%,#0076e5 100%);
      filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00adef', endColorstr='#0076e5',GradientType=1 );
      position: relative;
      width: 100%;
      margin: 0px auto;
      padding: 0px auto;
      overflow: hidden; /* ẩn bớt phần dư của các hình trong đi */
  }
  
  #container-inside {
      position: relative;
      min-width: 100%;
      height: auto;
      min-height: 100%;
      margin: 0px auto;
      padding: 0px auto;
      overflow: visible;
  }
  
  #circle-small {
    -webkit-animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation-timing-function: cubic-bezier(.6, 0, .4, 1);
    animation-delay: 0s;
    position: absolute;
    top: 200px;
    left: -150px;
    background: #fff;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    opacity: 0.4;
  }
  
  #circle-medium {
    -webkit-animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation-timing-function: cubic-bezier(.6, 0, .4, 1);
    animation-delay: 0.3s;
    position: absolute;
    top: 50px;
    left: -300px;
    background: #fff;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    opacity: 0.3;
  }
  
  #circle-large {
    -webkit-animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation-timing-function: cubic-bezier(.6, 0, .4, 1);
    animation-delay: 0.6s;
    position: absolute;
    top: -100px;
    left: -450px;
    background: #fff;
    width: 900px;
    height: 900px;
    border-radius: 50%;
    opacity: 0.2;
  }
  
  #circle-xlarge {
    -webkit-animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation-timing-function: cubic-bezier(.6, 0, .4, 1);
    animation-delay: 0.9s;
    position: absolute;
    top: -250px;
    left: -600px;
    background: #fff;
    width: 1200px;
    height: 1200px;
    border-radius: 50%;
    opacity: 0.1;
  }
  
  #circle-xxlarge {
    -webkit-animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation: circle-small-scale 3s ease-in-out infinite alternate;
    animation-timing-function: cubic-bezier(.6, 0, .4, 1);
    animation-delay: 1.2s;
    position: absolute;
    top: -400px;
    left: -750px;
    background: #fff;
    width: 1500px;
    height: 1500px;
    border-radius: 50%;
    opacity: 0.05;
  }
  
  @-webkit-keyframes circle-small-scale {
      0% {
          -webkit-transform: scale(1.0);
      }
      100% {
          -webkit-transform: scale(1.1);
      }
  }
  
  @keyframes circle-small-scale {
      0% {
          transform: scale(1.0);
      }
      100% {
          transform: scale(1.1);
      }
  }
  
  /* HIỆU ỨNG BACKGROUND HÌNH TRÒN */
  
  /* @import url('https://fonts.googleapis.com/css?family=Exo:400,700'); */
  
   *{
     margin: 0;
     padding: 0;
     outline: none;
     box-sizing: border-box;
     /* font-family: 'Exo', sans-serif; */
   }
   #main{
    background-color: #F2F4F6;
    /* padding-top: 10px; */
    /* padding-left: 30px; */
    /* padding-right: 30px; */
    height: 100vh;
   }
   body{
     display: flex;
     align-items: center;
     justify-content: center;
     min-height: 100vh;
     background: linear-gradient(to right, #EF629F, #EECDA3);
   }
  
   /* input */
   .container{
    border-radius: 36px;
    /* width: 450px; */
    background: #fff;
    padding: 30px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
   }
   .container .input-form{
     height: 40px;
     width: 100%;
     position: relative;
   }
   .container .input-form input{
     height: 100%;
     width: 100%;
     border: none;
     font-size: 17px;
     border-bottom: 2px solid silver;
   }
   .input-form input:focus ~ label,
   .input-form input:valid ~ label{
     transform: translateY(-20px);
     font-size: 15px;
     color: #F84B2F;
   }
   .container .input-form label{
     position: absolute;
     bottom: 10px;
     left: 0;
     color: grey;
     pointer-events: none;
     transition: all 0.3s ease;
   }
   .input-form .underline{
     position: absolute;
     height: 2px;
     width: 100%;
     bottom: 0;
   }
   .input-form .underline:before{
     position: absolute;
     content: "";
     height: 100%;
     width: 100%;
     background: #F84B2F;
     transform: scaleX(0);
     transform-origin: center;
     transition: transform 0.3s ease;
   }
   .input-form input:focus ~ .underline:before,
   .input-form input:valid ~ .underline:before{
     transform: scaleX(1);
   }
  /* input */
  
  /* show password */
  
  @import url('https://fonts.googleapis.com/css2?family=Reem+Kufi+Ink');
  
  #big {
      justify-content: center;
      display: flex;
      position: relative; /* LÀM NHƯ THẾ NÀY ĐỂ KHÔNG BỊ HIỆU ỨNG background HÌNH TRÒN ĐÈ LÊN PHÍA TRÊN */
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
    background-color: #F84B2F;
    box-shadow: 0px 15px 20px #f7cbc4;
    color: #fff;
    transform: translate(-50%, -7px);
  }
  
  .btn-pers:active {
    transform: translate(-50%, -1px);
  }
   /* btn Login */
  
   /* under */
  .under{
      position: relative;
      padding: 0px 0px;
  }
  .under::after{
      content: ' ';
      position: absolute;
      left: 0;
      bottom: -4px;
      width: 0;
      height: 2px;
      background:#F84B2F;
      transition: width 0.3s;
  }
  .under:hover::after {
      width: 100%;
      transition: width 0.3s;
  }
   /* under */
  
  
  
  
  
  </style>
  
  