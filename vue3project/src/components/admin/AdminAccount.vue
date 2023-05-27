<template>
    <div>
        <div v-if="isAdmin" class="d-flex justify-content-center">
            <div class="d-flex justify-content-center alert alert-primary col-6" role="alert" >
                My Account
            </div>
        </div>
        <div v-if="isAdmin" class="d-flex justify-content-center">
            <router-link class="mx-4" :to="{ name: 'AdminProfile' }"> <i class="fa-solid fa-user-shield"></i> Profile </router-link>
            <router-link class="mx-4" :to="{ name: 'AdminChangePassword' }"> <i class="fa-solid fa-key"></i> Change Password </router-link>
        </div>
        <router-view></router-view>
    </div>
</template>
<script>

export default {
    name: "AdminAccount",
    components: {
    },
    computed: {
        isAdmin() {
            if(this.$route.path == '/admin/account' || this.$route.path == '/admin/account/') return true;
            else return false;
        },
    },
    data(){
        return {
            Admin:null,
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