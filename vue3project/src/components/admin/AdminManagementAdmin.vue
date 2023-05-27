<template>
    <div class="_view-user">
        <ParticleVue32></ParticleVue32>
        <div class="_view-user-min" >
            <div class="_content">
    <div>
        <!-- <div class="d-flex justify-content-between">
            <div>
                <router-link to="/admin"> Dashboard Admin </router-link><i class="fa-solid fa-angles-right"></i>
                <router-link :to="{ name: 'AdminManagementUser' }"> Management User</router-link>
            </div>
            <div>
                <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
                    <i class="fa-solid fa-user-plus"></i>
                </button>
            </div>
        </div> -->
        <div class="row" >
            <div class="col-12">
                <div style="margin-bottom: 20px;color:gray"><i class="fa-solid fa-users"></i> MANAGEMENT USER</div>
            </div>
        </div>
        <div >
            <table class="table table-hover table-bordered">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">ID</th>
                        <!-- <th scope="col" class="text-center"><i class="fa-solid fa-envelope"></i> Email</th> -->
                        <th scope="col" ><i class="fa-solid fa-envelope"></i> Email</th>
                        <th scope="col" ><i class="fa-solid fa-at"></i> Full Name</th>
                        <th scope="col" ><i class="fa-solid fa-phone"></i> Phone</th>
                        <!-- <th scope="col" ><i class="fa-solid fa-layer-group"></i> Vector</th> -->
                        <!-- <th scope="col" ><i class="fa-solid fa-layer-group"></i> Image</th> -->
                        <th scope="col" ><i class="fa-regular fa-calendar-plus"></i> Create At</th>
                        <th scope="col" ><i class="fa-solid fa-calendar-plus"></i> Update At</th>
                        <!-- <th></th> -->
                        <th></th>
                    </tr>
                </thead>
                <tbody v-for="(user,index) in users" :key="index">
                    <tr>
                        <th scope="row">{{ (pageN-1)*6+index+1 }}</th>
                        <td>{{ user.id.length > 20 ? user.id.slice(0, 20) + '...' : user.id }}</td>
                        <td>{{ user.email.length > 30 ? user.email.slice(0, 30) + '...' : user.email }}</td>
                        <td>{{ user.fullname }}</td>
                        <td>{{ user.phone }}</td>
                        <!-- <td>{{ user.vector }}</td> -->
                        <!-- <td>{{ user.url_video }}</td> -->
                        <td>{{ processDate(user.create_at) }}</td>
                        <td>{{ processDate(user.update_at) }}</td>
                        <!-- <td>{{ user.update_time != null ? user.update_time.slice(0, 26) : user.update_time }}</td> -->
                        <!-- <td style=""><button type="button" class="btn btn-outline-primary" @click="editRole(ad.id,ad.role)">Save</button></td> -->
                        <td style=""><button v-if="user.id != admin.id" type="button" class="btn btn-outline-danger" @click="openModel(user.id)" data-toggle="modal" data-target="#exampleModalDelete">Delete</button></td>
                    </tr>
                </tbody>
            </table>
            <div>
                <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
                    <i class="fa-solid fa-user-plus"></i>
                </button>
            </div>
            <br>
            <div id="divpaginate2">
                <paginate class="pag" id="nvm"
                    :page-count="Math.ceil(this.quantity/6)"
                    :page-range="3"
                    :margin-pages="2"
                    :click-handler="clickCallback"
                    :initial-page="this.pageN"
                    :prev-text="'Prev'"
                    :next-text="'Next'"
                    :container-class="'pagination'"
                    :page-class="'page-item'">
                </paginate>

            </div>
        </div>

        <!-- Modal -->
        <div style="background-color: #3d3d3d99;" class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Add Account</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form @submit.prevent="register()" class="col-12">
                            <div class="form-group">
                                <label for="exampleInputEmail1">Email address</label>
                                <!-- minlength and maxlength -->
                                <input autocomplete="off" type="email" minlength="16" required v-model="user.email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputPassword1">Password</label>
                                <input required minlength="6" v-model="user.password" type="password" class="form-control" id="exampleInputPassword1">
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                                <label class="form-check-label" for="exampleCheck1">Check me out</label>
                            </div>
                            <div class="modal-footer">
                            <button id="closeAdd" type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            <button type="submit" class="btn btn-success"><i class="fa-solid fa-plus"></i> Add</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <!-- Model Delete Admin -->
        <div style="background-color: #3d3d3d99;" class="modal fade" id="exampleModalDelete" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Warning</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="alert alert-warning" role="alert">
                            Are you sure you want to delete this account ? <br>
                            This account will be permanently deleted from the system !
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-outline-secondary" data-dismiss="modal" @click="closeDelete" id="btnClose2">Close</button>
                        <button type="button" class="btn btn-outline-danger" @click="deleteUserInCollection"><i class="fa-solid fa-trash"></i> Delete</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Model Delete Admin -->
        <!-- {{ number1 }} -->
        <!-- <Notification></Notification> -->

    </div>
    </div>
    </div>
    </div>
</template>

<script>

// import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
// import { getAuth } from "firebase/auth";
// import { getAuth,deleteUser, createUserWithEmailAndPassword } from "firebase/auth";
import { fireStoreCore } from './../../configs/firebase';
import firebase from 'firebase/compat/app';
import bcrypt from 'bcryptjs';

import useEventBus from '../../composables/useEventBus'
import Paginate from 'vuejs-paginate-next';
// import Notification from './Notification'
import BaseRequest from '../../restful/user/core/BaseRequest'


export default {

    name: "AdminManagementAdmin",
    components: {
        // Notification,
        paginate: Paginate,
    },
    data(){
        return {
            user:{
                email:'',
                password:'',
                role:"admin"
            },
            uid:null,
            number1:0,
            users:[],
            quantity:null,
            pageN:1,
            pageSize:6,
            idDelete:null,
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
        // setInterval(() => {
        //     this.number1++;
        // }, 1000);
        window.document.title='Admin Management - PBL5';
        this.admin = JSON.parse(window.localStorage.getItem('admin'));
        BaseRequest.get('admin-list/?page=1')
            .then( data => {
            this.users = data.results;
            this.quantity = data.count;
            const { emitEvent } = useEventBus();
            emitEvent('eventSuccess','Get All Admin Success !');
        })
        .catch( () => {
            const { emitEvent } = useEventBus();
            emitEvent('eventError','Get All Admin Fail !');
        })

    },
    methods: {
        formatDate(date) {
            const year = date.getFullYear();
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const day = String(date.getDate()).padStart(2, '0');
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const seconds = String(date.getSeconds()).padStart(2, '0');
            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },
        processDate(dateString){
            const date = new Date(dateString);
            const hours = date.getHours();
            const minutes = date.getMinutes();
            const seconds = date.getSeconds();
            const day = date.getDate();
            const month = date.getMonth() + 1;
            const year = date.getFullYear();
            return(`${day}/${month}/${year} ${hours}:${minutes}:${seconds}`);
        },
        // register(){ // Không thêm tài khoản vào Authentication nữa 
            // createUserWithEmailAndPassword(getAuth(),this.user.email,this.user.password)
            // .then((data) => {
            //     // console.log(data);
            //     this.uid = data.user.uid;
            //     this.setData(data);
            //         // create admin 
            //         // let id_admin = fireStoreCore.collection("users").doc().id;
            // })
            // .catch((error) => {
            //     const { emitEvent } = useEventBus();
            //     emitEvent('eventError',error.code);
            //     // console.log(error);
            // })
        // },
        register() {
            BaseRequest.post('users/',this.user)
            .then( () => {
                this.getUsers(this.pageN);
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Add Admin Success !');
                this.user = {
                    email:'',
                    password:'',
                    role:"admin"
                };
            })
            .catch( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Add Admin Fail !');
            })
        },
        getUsers(n) {
            BaseRequest.get('admin-list/?page='+n)
                .then( data => {
                this.users = data.results;
                this.quantity = data.count;
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Get All Admin Success !');
            })
            .catch( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Get All Admin Fail !');
            })
        },
        clickCallback:function(pageNum){
            this.pageN = pageNum;
            this.getUsers(pageNum);
        },
        openModel:function(id){
            this.idDelete = id;
        },
        deleteUserInCollection(){
            BaseRequest.delete('users/'+this.idDelete+'/')
            .then( () => {
                var close_btn = window.document.getElementById('btnClose2');
                close_btn.click();
                const { emitEvent } = useEventBus();
                emitEvent('eventSuccess','Delete Admin Success !');
                // tải lại resource mới mà không cần phải reload lại trang 
                this.getUsers(this.pageN);
            })
            .catch( () => {
                const { emitEvent } = useEventBus();
                emitEvent('eventError','Delete Admin Fail !');
            })
        },
        // deleteAdminInAuthentication(){ // Với Authentication Chỉ có thể xóa tài khoản hiện tại của bản thân 
        //     // không cho phép xóa tài khoản khác . 
        //     const auth = getAuth(fireStoreCore);
        //     deleteUser(auth, '46ql3c7DZyQoK6ebSowWvFpUc2v1')
        //         .then(() => {
        //         console.log("User deleted successfully.");
        //         // Do something after user is deleted
        //         })
        //         .catch((error) => {
        //         console.error("Error deleting user:", error);
        //         });
        // }
    }
}
</script>
<style scoped>
#divpaginate {
    position: absolute;
    bottom: 10%;
}
</style>