import { createRouter, createWebHistory } from 'vue-router'
// import useEventBus from '../composables/useEventBus'

// admin 
import AdminComp from './../components/Admin'
import AdminLogin from './../components/admin/AdminLogin'
import AdminResetPassword from './../components/admin/AdminResetPassword'
import AdminAccount from './../components/admin/AdminAccount'
import AdminProfile from './../components/admin/account/AdminProfile'
import AdminChangePassword from './../components/admin/account/AdminChangePassword'
import AdminComments from './../components/admin/account/other/AdminComments'
import AdminHelpSupport from './../components/admin/account/other/AdminHelpSupport'
import AdminDashboard from './../components/admin/AdminDashboard'
import AdminManagementAdmin from './../components/admin/AdminManagementAdmin'
import AdminManagementUser from './../components/admin/AdminManagementUser'
import AdminStatistical from './../components/admin/AdminStatistical'
import StatisticalDetails from './../components/admin/StatisticalDetails'
import AdminLogs from './../components/admin/AdminLogs'

// user 
import UserComp from './../components/User'
import UserLogin from './../components/user/UserLogin'
import UserResetPassword from './../components/user/UserResetPassword'
import UserAccount from './../components/user/UserAccount'
import UserProfile from './../components/user/account/UserProfile'
import UserChangePassword from './../components/user/account/UserChangePassword'
import UserComments from './../components/user/account/other/UserComments'
import UserHelpSupport from './../components/user/account/other/UserHelpSupport'
import UserUpfile from './../components/user/account/UserUpfile'
import UserAttentdance from './../components/user/UserAttentdance'

// other 
import NotFound from './../components/NotFound'

const routes = [
    {
        path: '/main',
        component: UserComp,
        name:'UserComp',
        children : [
            {path:'login',name:'UserLogin',component:UserLogin},
            {path:'reset-password',name:'UserResetPassword',component:UserResetPassword},

            {path:'account',name:'UserAccount',component:UserAccount,
                children : [
                    {path:'profile',name:'UserProfile',component:UserProfile},
                    {path:'change-password',name:'UserChangePassword',component:UserChangePassword},
                    {path:'comments',name:'UserComments',component:UserComments},
                    {path:'help-support',name:'UserHelpSupport',component:UserHelpSupport},
                    {path:'upfile',name:'UserUpfile',component:UserUpfile,},
                ]
            },
            {path:'attentdance',name:'UserAttentdance',component:UserAttentdance},
        ]
    },   
    {
        path: '/admin',
        component: AdminComp,
        name:'AdminComp',
        children : [
            {path:'login',name:'AdminLogin',component:AdminLogin},
            {path:'reset-password',name:'AdminResetPassword',component:AdminResetPassword},

            {path:'account',name:'AdminAccount',component:AdminAccount,
                children : [
                    {path:'profile',name:'AdminProfile',component:AdminProfile},
                    {path:'change-password',name:'AdminChangePassword',component:AdminChangePassword},
                    {path:'comments',name:'AdminComments',component:AdminComments},
                    {path:'help-support',name:'AdminHelpSupport',component:AdminHelpSupport},
                ]
            },

            {path:'dashboard',name:'AdminDashboard',component:AdminDashboard},

            {path:'management-admin',name:'AdminManagementAdmin',component:AdminManagementAdmin},
            {path:'management-user',name:'AdminManagementUser',component:AdminManagementUser},
            {path:'statistical',name:'AdminStatistical',component:AdminStatistical},
            {path:'logs',name:'AdminLogs',component:AdminLogs},
            {path:'statistical-details/:id',name:'StatisticalDetails',component:StatisticalDetails},
        ]
    }, 
    {path: '/:NotFound(.*)*',component: NotFound,name:'NotFound'}
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach((to,from,next)=>{

    if(to.path == '/' || to.path == '') {
        next({name:'UserComp'});
    }

    let user = localStorage.getItem('user');
    if (!user && to.path.startsWith('/main/') && to.path !== '/main/login') {
        next({ name: 'UserLogin', replace: true });
    } 
    // else {
    //   next(); không được thêm đoạn này , này phải để cuối , nếu không đoạn sau nó sẽ không check nữa 
    // }
        
    // if(to.path.includes('/main')){
    //     if(to.path == '/main/account' || to.path == '/main/account/'){
    //         next({name:'UserProfile'});
    //     }
    // }

    if(to.path.includes('/admin')){
        if(to.path == '/admin/') {
            next({name:'AdminComp'});
        }
        // if(to.path == '/admin/account' || to.path == '/admin/account/'){
        //     next({name:'AdminProfile'});
        // }

        let user = localStorage.getItem('admin');
        if (!user && to.path.startsWith('/admin') && to.path !== '/admin/login') {
            next({ name: 'AdminLogin', replace: true });
        } 
    }
    next();
}) 

export default router

// -----------------------------------------------------------------------------

// import { createRouter, createWebHistory } from 'vue-router'
// import useEventBus from '../composables/useEventBus'


// // admin
// import AdminComp from './../components/Admin'
// import LoginAdmin from './../components/admin/Login'
// import ResetPasswordAdmin from './../components/admin/ResetPassword'
// import DashboardAdmin from './../components/admin/Dashboard'
// import ProfileAdmin from './../components/admin/Profile'

// import CategoryAdmin from './../components/admin/Category'
// import CustomerAdmin from './../components/admin/Customer'
// import ManagementAdmin from './../components/admin/ManagementAdmin'
// import AdminOrderDetails from './../components/admin/AdminOrderDetails'
// import AdminOrderPrintPDF from './../components/admin/AdminOrderPrintPDF'
// import OrderAdmin from './../components/admin/Order'
// import ProductAdmin from './../components/admin/Product'
// import ProductAdd from './../components/admin/ProductAdd'
// import ProviderAdmin from './../components/admin/Provider'
// import StatisticalAdmin from './../components/admin/Statistical'
// import ProductDetails from './../components/admin/ProductDetails'
// import WareHouse from './../components/admin/Warehouse'
// import WarehouseImport from './../components/admin/WarehouseImport'
// import ImportDetails from './../components/admin/ImportDetails'
// import ImportProduct from './../components/admin/ImportProduct'

// // admin order 
// import AdminDeliveredComp from './../components/admin/purchase/AdminDeliveredComp'
// import AdminDeliveringComp from './../components/admin/purchase/AdminDeliveringComp'
// import AdminWaitForConfirmation from './../components/admin/purchase/AdminWaitForConfirmation'
// import AdminWaitingForShipping from './../components/admin/purchase/AdminWaitingForShipping'

// // user 
// import UserComp from './../components/User'
// import LoginUser from './../components/user/Login'
// import RegisterUser from './../components/user/Register'
// import ResetPasswordUser from './../components/user/ResetPassword'

// import AccountUser from './../components/user/Account'
// import ProfileUser from './../components/user/account/Profile'
// import ChangePasswordUser from './../components/user/account/ChangePassword'
// import PurchaseOrderUser from './../components/user/account/PurchaseOrder' 
// import ShippingAddressUser from './../components/user/account/ShippingAddress'  
// import OrderDetails from './../components/user/account/OrderDetails'  

// import DashboardUser from './../components/user/Dashboard'
// import ProductUserDetails from './../components/user/ProductUserDetails'
// import UserOrder from './../components/user/UserOrder'
// import InforUser from './../components/user/InforUser' 

// // user order 
// import CancelledComp from './../components/user/purchase/CancelledComp'
// import DeliveredComp from './../components/user/purchase/DeliveredComp'
// import DeliveringComp from './../components/user/purchase/DeliveringComp'
// import WaitForConfirmation from './../components/user/purchase/WaitForConfirmation'
// import WaitingForShipping from './../components/user/purchase/WaitingForShipping'


// // other 
// import NotFound from './../components/NotFound'
// import ChangeComp from './../components/Change'

// const routes = [

//     {
//         path: '/main',
//         component: UserComp,
//         name:'UserComp',
//         children : [
//             {path:'login',name:'LoginUser',component:LoginUser},
//             {path:'register',name:'RegisterUser',component:RegisterUser},
//             {path:'reset-password',name:'ResetPasswordUser',component:ResetPasswordUser},

//             {path:'account',name:'AccountUser',component:AccountUser,
//                 children : [
//                     {path:'profile',name:'ProfileUser',component:ProfileUser},
//                     {path:'change-password',name:'ChangePasswordUser',component:ChangePasswordUser},
//                     {
//                         path:'purchase-order',
//                         name:'PurchaseOrderUser',
//                         component:PurchaseOrderUser,
//                         children : [
//                             {path:'cancelled',name:'CancelledComp',component:CancelledComp},
//                             {path:'delivered',name:'DeliveredComp',component:DeliveredComp},
//                             {path:'delivering',name:'DeliveringComp',component:DeliveringComp},
//                             {path:'confirmation',name:'WaitForConfirmation',component:WaitForConfirmation},
//                             {path:'shipping',name:'WaitingForShipping',component:WaitingForShipping},
//                         ]
//                     },
//                     {path:'shipping-address',name:'ShippingAddressUser',component:ShippingAddressUser},
//                     {path:'order-details/:id',name:'OrderDetails',component:OrderDetails},
//                 ]
//             },

//             {path:'dashboard',name:'DashboardUser',component:DashboardUser},
//             {path:'product/:id',name:'ProductUserDetails',component:ProductUserDetails},
//             {path:'order',name:'UserOrder',component:UserOrder},
//             {path:'infor-user',name:'InforUser',component:InforUser},
//         ]
//     },   
//     {
//         path: '/admin',
//         component: AdminComp,
//         name:'AdminComp',
//         children : [
//             {path:'login',name:'LoginAdmin',component:LoginAdmin},
//             {path:'reset-password',name:'ResetPasswordAdmin',component:ResetPasswordAdmin},
//             {path:'dashboard',name:'DashboardAdmin',component:DashboardAdmin},
//             {path:'profile-admin',name:'ProfileAdmin',component:ProfileAdmin},

//             {path:'category',name:'CategoryAdmin',component:CategoryAdmin},
//             {path:'customer',name:'CustomerAdmin',component:CustomerAdmin},
//             {path:'management-admin',name:'ManagementAdmin',component:ManagementAdmin},
//             {
//                 path:'order',
//                 name:'OrderAdmin',
//                 component:OrderAdmin,
//                 children : [
//                     {path:'delivered',name:'AdminDeliveredComp',component:AdminDeliveredComp},
//                     {path:'delivering',name:'AdminDeliveringComp',component:AdminDeliveringComp},
//                     {path:'confirmation',name:'AdminWaitForConfirmation',component:AdminWaitForConfirmation},
//                     {path:'shipping',name:'AdminWaitingForShipping',component:AdminWaitingForShipping},
//                 ]
//             },
//             {path:'order-details/:id',name:'AdminOrderDetails',component:AdminOrderDetails},
//             {path:'print/:id',name:'AdminOrderPrintPDF',component:AdminOrderPrintPDF},
//             {path:'product',name:'ProductAdmin',component:ProductAdmin},
//             {path:'product/add',name:'ProductAdd',component:ProductAdd},
//             {path:'product/:id',name:'ProductDetails',component:ProductDetails},
//             {path:'provider',name:'ProviderAdmin',component:ProviderAdmin},
//             {path:'warehouse',name:'WareHouse',component:WareHouse},
//             {path:'warehouse-import',name:'WarehouseImport',component:WarehouseImport},
//             {path:'warehouse-import/:id',name:'ImportDetails',component:ImportDetails},
//             {path:'import-product',name:'ImportProduct',component:ImportProduct},
//             {path:'statistical',name:'StatisticalAdmin',component:StatisticalAdmin},
//         ]
//     }, 
//     {path: '/',component: ChangeComp,name:'ChangeComp'},
//     {path: '/:NotFound(.*)*',component: NotFound,name:'NotFound'}


    
// ];

// const router = createRouter({
//     history: createWebHistory(),
//     routes: routes
// })

// router.beforeEach((to,from,next)=>{
//     if(to.path.includes('/main')){

//         if(to.path == '/main' || to.path == '/main/'){
//             next({name:'DashboardUser'});
//         }

//         if(to.path.includes('/main/product/')) next(); // (1) 
//         if(to.path.includes('/main/order')) next(); // (1) 

//         let excludePages = ['/main/login','/main/dashboard','/main/register','/main/reset-password'];
//         let requiredlogin = !excludePages.includes(to.path); 

//         let user = localStorage.getItem('user');
//         if(requiredlogin && !user){
//             if(to.path != "/main"){
//                 next({name:'LoginUser'});
//                 const { emitEvent } = useEventBus();
//                 emitEvent('eventError401',"Bạn chưa đăng nhập !");
//             }
//         }

//         // account
//         if(to.path == '/main/account' || to.path == '/main/account/'){
//             next({name:'ProfileUser'});
//         }

//         // purchase-order
//         if(to.path == '/main/account/purchase-order' || to.path == '/main/account/purchase-order/'){
//             next({name:'WaitForConfirmation'});
//         }

//     }

//     if(to.path.includes('/admin')){
//         let excludePages = ['/admin/login','/admin/reset-password'];
//         let requiredlogin = !excludePages.includes(to.path);
//         let admin = localStorage.getItem('admin');
//         if(requiredlogin && !admin){
//             if(to.path != "/admin"){
//                 next({name:'LoginAdmin'});
//                 const { emitEvent } = useEventBus();
//                 emitEvent('eventError401',"Admin chưa đăng nhập !");
//             }
//         }
//     }
//     next();
// }) 

// export default router
