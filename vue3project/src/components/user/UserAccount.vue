<template>
    <div>
        <div v-if="isUser" class="d-flex justify-content-center">
            <div class="d-flex justify-content-center alert alert-primary col-6" role="alert" >
                My Account
            </div>
        </div>
        <div v-if="isUser" class="d-flex justify-content-center">
            <router-link class="mx-4" :to="{ name: 'UserProfile' }"> <i class="fa-solid fa-user-pen"></i> Profile </router-link>
            <router-link class="mx-4" :to="{ name: 'UserChangePassword' }"> <i class="fa-solid fa-key"></i> Change Password </router-link>
            <router-link class="mx-4" :to="{ name: 'UserUpfile' }"> <i class="fa-solid fa-images"></i> Upfile </router-link>
        </div>
        <router-view></router-view>
    </div>
</template>
<script>

export default {
    name: "UserAccount",
    components: {
    },
    computed: {
        isUser() {
            if(this.$route.path == '/main/account' || this.$route.path == '/main/account/') return true;
            else return false;
        },
    },
    data(){
        return {
            User:null,
        } 
    },
    methods: {
    
    },
    mounted(){
    }
}
</script>

<style>

</style>