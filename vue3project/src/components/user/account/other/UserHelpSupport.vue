<template>
    <div id="helpSupport">
        <ParticleVue32></ParticleVue32>
        <div id="helpSupport_content">
            <h1 style="color: #0085FF;font-size: 24px;text-align: center;font-weight: bold;"><i class="fa-regular fa-circle-question"></i> Help Support</h1>
            <h1 class="title">User manual</h1>
            <li class="features">Add,Edit,View All Article</li>
            <li class="features">Comment Article</li>
            <li class="features">Change Password</li>
            <li class="features">Update Profile</li>
            <h1 class="title">About US</h1>
            <div style="text-align: center;color: #0085FF;font-weight: bold;margin-bottom: 20px;"><a href="tel:0971404372"><i class="fa-solid fa-phone-volume"></i> 0971404372</a></div>
            <div class="col-8 mx-auto">
                <table class="table table-borderless">
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col"><i class="fa-brands fa-dev"></i> Name</th>
                        <th scope="col"><i class="fa-solid fa-envelope"></i> Email</th>
                        <th scope="col"><i class="fa-solid fa-address-card"></i> MSSV</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">01</th>
                        <td>Nguyễn Văn Mạnh</td>
                        <td><a href="mailto:nguyenvanmanh2001it1@gmail.com">nguyenvanmanh2001it1@gmail.com</a></td>
                        <td>102200024</td>
                    </tr>
                    <tr>
                        <th scope="row">02</th>
                        <td>Nguyễn Công Cường</td>
                        <td><a href="mailto:ncc02@gmail.com">ncc02@gmail.com</a></td>
                        <td>102200013</td>
                    </tr>
                    <tr>
                        <th scope="row">03</th>
                        <td>Nguyễn Văn Hoàng Phúc</td>
                        <td><a href="mailto:phantiendat2102@gmail.com">toilaphucnguyen@gmail.com</a></td>
                        <td>102200028</td>
                    </tr>
                    <tr>
                        <th scope="row">04</th>
                        <td>Trần Thanh Nguyên</td>
                        <td><a href="mailto:phantiendat2102@gmail.com">boydut@gmail.com</a></td>
                        <td>102200027</td>
                    </tr>
                </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>

import ParticleVue32 from "../../../particle/ParticleVue32.vue";
export default {
    name : "HelpSupport",
    components: {
        ParticleVue32,
    },
    data(){
        return{
  
        }
    },
    created(){
  
    },
    mounted(){
        window.document.title='Help & Support';
    },
    methods:{
        
    },
}
</script>
<style scoped>
#helpSupport_content {
    margin: auto;
    background-color: white;
    width: 90%;
    height: 90%;
    margin-top: 40px;
    position: relative;
    border-radius: 10px;
    height: 88vh;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 20px;
    padding-top: 60px;
}
.title {
    font-weight: bold;
    font-size: 20px;
    color: #0085FF;
    margin-bottom: 10px;
    margin-top: 30px;
    text-align: center;
}
.features {
    font-weight: bold;
    font-size: 16px;
    color: rgb(96, 96, 96);
    margin-left: 20px;
    text-align: center;
}
</style>