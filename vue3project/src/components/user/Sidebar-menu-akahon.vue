<template>
  <div class="sidebar" :class="isOpened ? 'open' : ''" :style="cssVars">
    <div class="logo-details" style="margin: 10px 14px 0 14px;padding: 10px 0px;">
      <img src="../../assets/logo.png" alt="menu-logo" class="menu-logo icon" style="" @click="compadmin">
      <!-- <i v-else class="bx icon" :class="menuIcon"/> -->
      <div class="logo_name" @click="compadmin">Project PBL5 </div>
      <i style="color: #0085FF;" class="bx" :class="isOpened ? 'bx-menu-alt-right' : 'bx-menu'" id="btn" @click="openN"/>
    </div>
    <div style="display: flex ; flex-direction:column; justify-content: space-between; flex-grow: 1; max-height: calc(100% - 60px); ">
      <div id="my-scroll" style="margin: 6px 14px 0 14px;">
        <ul class="nav-list" style="overflow: visible;">
          <!-- <li v-if="isSearch" @click="isOpened = true">
            <i class="bx bx-search" />
            <input type="text" :placeholder="searchPlaceholder" @input="$emit('search-input-emit', $event.target.value)">
            <span class="tooltip">{{ searchTooltip }}</span>
          </li> -->
          

          <div class="line"></div>
          <span>
            <li @click="profile">
              <a :class="{adefault:true,aclick:colors[0]}"><i class="fa-regular fa-address-card"></i><span class="links_name">Profile</span></a>
              <span class="tooltip">Profile</span>
            </li>
          </span>

          <div class="line"></div>
          <span>
            <li @click="dashboard">
              <a :class="{adefault:true,aclick:colors[2]}"><i class="fa-solid fa-calendar-check"></i><span class="links_name">User Attentdance</span></a>
              <span class="tooltip">User Attentdance</span>
            </li>
          </span>

          <div class="line"></div>
          <span>
            <li @click="changepw">
              <a :class="{adefault:true,aclick:colors[1]}"><i class="fa-solid fa-key"></i><span class="links_name">Change Password</span></a>
              <span class="tooltip">Change Passowrd</span>
            </li>
          </span>

          <div class="line d-none"></div>
          <span class="d-none">
            <li @click="article">
              <a data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample" :class="{adefault:true,aclick:colors[3]}">
                <i class="fa-solid fa-bars-staggered"></i>
                <span class="links_name">Article</span>
                <i class="fa-solid fa-chevron-right"></i>
              </a>
              <span class="tooltip">Article </span>

              <div class="collapse" id="collapseExample" style="margin-left: 30px;">
                <div class="line"></div>
                <span>
                  <li @click="allArticle">
                    <a :class="{adefault:true,aclick:colors[4]}" ><i class="fa-solid fa-bookmark"></i><span class="links_name">All Article</span></a>
                    <span class="tooltip">All Article</span>
                  </li>
                </span>

                <div class="line"></div>
                <span>
                  <li @click="addArticle">
                    <a :class="{adefault:true,aclick:colors[5]}" ><i class="fa-solid fa-plus"></i><span class="links_name">Add Article</span></a>
                    <span class="tooltip">Add Article</span>
                  </li>
                </span>
              </div>

            </li>
          </span>

          <div class="line"></div>
          <span>
            <li @click="helpSupport">
              <a :class="{adefault:true,aclick:colors[6]}"><i class="fa-solid fa-circle-question"></i><span class="links_name">Help & Support</span></a>
              <span class="tooltip">Help & Support</span>
            </li>
          </span>


          <div class="line"></div>
          <span>
            <li @click="comments">
              <a :class="{adefault:true,aclick:colors[7]}"><i class="fa-solid fa-circle-info"></i><span class="links_name">Comments</span></a>
              <span class="tooltip">Comments</span>
            </li>
          </span>
          <div style="height: 300px;">

          </div>
        </ul>
      </div>
      
      <div v-if="isLoggedIn" class="profile" >
        <!-- Sau này có thời gian thì làm thêm cái ảnh nữa -->
        <div class="profile-details">
          <!-- <img v-if="profileImg" :src="profileImg" alt="profileImg"> -->
          <!-- <i v-else class="bx bxs-user-rectangle"/> -->
          <div class="name_job"> 
            <div class="name" v-if="inf.fullname">{{ inf.fullname }}</div>
            <div class="name" v-if="inf.fullname == null">User Full Name</div>
            <div class="job" style="margin-bottom: 10px;">User</div>
          </div>
        </div>
        <i v-if="isExitButton" style="cursor:pointer ;" class="bx bx-log-out" id="log_out" @click="logout"/>
      </div>
    </div>

  </div>
</template>

<script>

// import useEventBus from '../../composables/useEventBus'

  export default {
    name: 'SidebarMenuAkahon',
    props: {
      //! Menu settings
      isMenuOpen: {
        type: Boolean,
        default: true,
      },
      menuTitle: {
        type: String,
        default: 'Akahon',
      },
      menuLogo: {
        type: String,
        default: '',
      },
      menuIcon: {
        type: String,
        default: 'bxl-c-plus-plus',
      },
      isPaddingLeft: {
        type: Boolean,
        default: true,
      },
       menuOpenedPaddingLeftBody: {
        type: String,
        default: '250px'
      },
      menuClosedPaddingLeftBody: {
        type: String,
        default: '78px'
      },

      //! Search
      isSearch: {
        type: Boolean,
        default: true,
      },
      searchPlaceholder: {
        type: String,
        default: 'Search...',
      },
      searchTooltip: {
        type: String,
        default: 'Search',
      },

      //! Profile detailes
      profileImg: {
        type: String,
        default: require('../../assets/avatar.png'),
      },
      isExitButton: {
        type: Boolean,
        default: true,
      },
      isLoggedIn: {
        type: Boolean,
        default: true,
      },

      //! Styles
      bgColor: {
        type: String,
        default: '#11101d',
      },
      secondaryColor: {
        type: String,
        default: '#1d1b31',
      },
      homeSectionColor: {
        type: String,
        default: '#e4e9f7',
      },
      logoTitleColor: {
        type: String,
        default: '#fff',
      },
      iconsColor: {
        type: String,
        default: '#fff',
      },
      itemsTooltipColor: {
        type: String,
        default: '#e4e9f7',
      },
      searchInputTextColor: {
        type: String,
        default: '#fff',
      },
      menuItemsHoverColor: {
        type: String,
        default: '#fff',
      },
      menuItemsTextColor: {
        type: String,
        default: '#fff',
      },
      menuFooterTextColor: {
        type: String,
        default: '#fff',
      },
    },
    data() {
      return {
        isOpened: false,
        colors:[false,false,false,false,false,false,false,false],
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
        inf:{
            role:'',
            fullname:'',
        },
      }
    },
    mounted() {
      this.isOpened = this.isMenuOpen;
      this.user = JSON.parse(window.localStorage.getItem('user'));
      this.inf.fullname = this.user.fullname;
    },
    methods:{

      openN:function(){
        this.isOpened = !this.isOpened
      },

      profile:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[0]=true;
        this.$router.push({name:'UserProfile'});
      },
      changepw:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[1]=true;
        this.$router.push({name:'UserChangePassword'});
      },
      dashboard:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[2]=true;
        this.$router.push({name:'UserAttentdance'});
      },
      article:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[3]=true;
      },
      allArticle:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[3]=true;
        this.colors[4]=true;
        this.$router.push({name:'ArticleAll'});
      },
      addArticle:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[3]=true;
        this.colors[5]=true;
        this.$router.push({name:'ArticleNew'});
      },
      helpSupport:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[6]=true;
        this.$router.push({name:'UserHelpSupport'});
      },
      comments:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[7]=true;
        this.$router.push({name:'UserComments'});
      },


      statistical:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[8]=true;
        this.$router.push({name:'StatisticalAdmin'});
      },
      customer:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[9]=true;
        this.$router.push({name:'CustomerAdmin'});
      },
      administrator:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        this.colors[10]=true;
        this.$router.push({name:'ManagementAdmin'});
      },

      compadmin:function(){
        for(var i=0;i<this.colors.length;i++) this.colors[i] = false;
        // window.location = window.location.origin + '/main/dashboard';
        this.$router.push({name:"DashboardMain"});
      },
      logout:function(){
        // const { emitEvent } = useEventBus()
        // window.localStorage.clear();
        window.localStorage.removeItem('user');
        // this.$router.push({name:"UserLogin"});
        window.location = window.origin+'/main/login';
        // emitEvent('eventLogout');
      }
    },
    computed: {
      cssVars() {
        return {
          // '--padding-left-body': this.isOpened ? this.menuOpenedPaddingLeftBody : this.menuClosedPaddingLeftBody,
          '--bg-color': this.bgColor,
          '--secondary-color': this.secondaryColor,
          '--home-section-color': this.homeSectionColor,
          '--logo-title-color': this.logoTitleColor,
          '--icons-color': this.iconsColor,
          '--items-tooltip-color': this.itemsTooltipColor,
          '--serach-input-text-color': this.searchInputTextColor,
          '--menu-items-hover-color': this.menuItemsHoverColor,
          '--menu-items-text-color': this.menuItemsTextColor,
          '--menu-footer-text-color': this.menuFooterTextColor,
        }
      },
    },
    watch: {
      isOpened() {
        window.document.body.style.paddingLeft = this.isOpened && this.isPaddingLeft ? this.menuOpenedPaddingLeftBody : this.menuClosedPaddingLeftBody
        var collapseExample = window.document.getElementById('collapseExample');
        if(this.isOpened == false){
          collapseExample.style='margin-left: 0px;';
        }
        if(this.isOpened == true){
          collapseExample.style='margin-left: 30px;';
        }
      }
    }
  }
</script>

<style scoped>
  /* Google Font Link */
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
  @import url('https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css');
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }
  body {
    transition: all 0.5s ease;
  }
  .adefault{
    background: #0085FF;
  }
  .aclick{
    background: #07131d;
  }
  .line {
    width: 100%;
    height: 2px;
    background-color: white;
    margin: 6px 0px;
    border: 1px solid white;

  }
  .menu-logo {
    width: 30px;
    margin: 0 10px 0 10px;
    cursor: pointer;
  }
  .sidebar {
    position: relative;
    display: flex;
    flex-direction: column;
    position: fixed;
    left: 0;
    top: 0;
    height: 100%;
    min-height: min-content;
    /* overflow-y: auto; */
    width: 78px;
    background: #0085FF;
    /* padding: 6px 14px 0 14px; */
    z-index: 99;
    transition: all 0.5s ease;
  }
  .sidebar.open {
    width: 250px;
  }
  .sidebar .logo-details {
    height: 60px;
    display: flex;
    align-items: center;
    position: relative;
    background-color: white;
    color: #0085FF;
    border-radius: 12px ;
  }
  .sidebar .logo-details .icon {
    opacity: 0;
    transition: all 0.5s ease;
  }
  .sidebar .logo-details .logo_name {
    cursor: pointer;
    color: #0085FF;
    font-size: 20px;
    font-weight: 600;
    opacity: 0;
    transition: all 0.5s ease;
  }
  .sidebar.open .logo-details .icon,
  .sidebar.open .logo-details .logo_name {
    opacity: 1;
  }
  .sidebar .logo-details #btn {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    font-size: 22px;
    transition: all 0.4s ease;
    font-size: 23px;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s ease;
  }
  .sidebar.open .logo-details #btn {
    text-align: right;
  }
  .bx-menu-alt-right::before{
    margin-right: 10px;
  }
  .sidebar i {
    color: var(--icons-color);
    height: 60px;
    min-width: 50px;
    font-size: 28px;
    text-align: center;
    line-height: 60px;
  }
  .sidebar .nav-list {
    margin-top: 20px;
    /* margin-bottom: 60px; */
    /* height: 100%; */
    /* min-height: min-content; */
  }
  .sidebar li {
    position: relative;
    margin: 8px 0;
    list-style: none;
    cursor: pointer;
  }
  .sidebar li .tooltip {
    position: absolute;
    top: -20px;
    left: calc(100% + 15px);
    z-index: 3;
    background: var(--items-tooltip-color);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 15px;
    font-weight: 400;
    opacity: 0;
    white-space: nowrap;
    pointer-events: none;
    transition: 0s;
  }
  .sidebar li:hover .tooltip {
    opacity: 1;
    pointer-events: auto;
    transition: all 0.4s ease;
    top: 50%;
    transform: translateY(-50%);
  }
  .sidebar.open li .tooltip {
    display: none;
  }
  .sidebar input {
    font-size: 15px;
    color: var(--serach-input-text-color);
    font-weight: 400;
    outline: none;
    height: 50px;
    width: 100%;
    width: 50px;
    border: none;
    border-radius: 12px;
    transition: all 0.5s ease;
    background: var(--secondary-color);
  }
  .sidebar.open input {
    padding: 0 20px 0 50px;
    width: 100%;
  }
  .sidebar .bx-search {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 22px;
    background: var(--secondary-color);
    color: var(--icons-color);
  }
  .sidebar.open .bx-search:hover {
    background: var(--secondary-color);
    color: var(--icons-color);
  }
  .sidebar .bx-search:hover {
    background: var(--menu-items-hover-color);
    color: var(--bg-color);
  }
  .sidebar li a {
    display: flex;
    height: 100%;
    width: 100%;
    border-radius: 12px;
    align-items: center;
    text-decoration: none;
    transition: all 0.4s ease;
    /* background: #0085FF; */
  }
  .sidebar li a:hover {
    background-color: white;
  }
  .sidebar li a .links_name {
    color: var(--menu-items-text-color);
    font-size: 15px;
    font-weight: 400;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: 0.4s;
    font-weight: 500;
  }
  .sidebar.open li a .links_name {
    opacity: 1;
    pointer-events: auto;
  }
  .sidebar li a:hover .links_name,
  .sidebar li a:hover i {
    transition: all 0.5s ease;
    color: #0085FF;
  }
  .sidebar li i {
    height: 50px;
    line-height: 50px;
    font-size: 18px;
    border-radius: 12px;
  }
  .sidebar div.profile {
    position: relative;
    height: 74px;
    width: 78px;
    /* left: 0;
    bottom: 0; */
    padding: 10px 14px;
    background: var(--secondary-color);
    transition: all 0.5s ease;
    overflow: hidden;
  }
  .sidebar.open div.profile {
    width: 250px;
  }
  .sidebar div .profile-details {
    display: flex;
    align-items: center;
    flex-wrap: nowrap;
  }
  .sidebar div img {
    height: 45px;
    width: 45px;
    object-fit: cover;
    border-radius: 6px;
    margin-right: 10px;
  }
  .sidebar div.profile .name,
  .sidebar div.profile .job {
    font-size: 15px;
    font-weight: 400;
    color: var(--menu-footer-text-color);
    white-space: nowrap;
  }
  .sidebar div.profile .job {
    font-size: 12px;
  }
  .sidebar .profile #log_out {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    background: var(--secondary-color);
    width: 100%;
    height: 60px;
    line-height: 60px;
    border-radius: 0px;
    transition: all 0.5s ease;
  }
  .sidebar.open .profile #log_out {
    width: 50px;
    background: var(--secondary-color);
    opacity: 0;
  }
  .sidebar.open .profile:hover #log_out {
    opacity: 1;
  }
  .sidebar.open .profile #log_out:hover {
    opacity: 1;
    color: red;
  }
  .sidebar .profile #log_out:hover {
    color: red;
  }
  .home-section {
    position: relative;
    background: var(--home-section-color);
    min-height: 100vh;
    top: 0;
    left: 78px;
    width: calc(100% - 78px);
    transition: all 0.5s ease;
    z-index: 2;
  }
  .sidebar.open ~ .home-section {
    left: 250px;
    width: calc(100% - 250px);
  }
  .home-section .text {
    display: inline-block;
    color: var(--bg-color);
    font-size: 25px;
    font-weight: 500;
    margin: 18px;
  }
  .my-scroll-active {
    overflow-y: auto;
  }
  #my-scroll {
    overflow-y: auto;
    height: calc(100% - 60px);
  }
  #my-scroll::-webkit-scrollbar{
    display:none;
    /* background-color: rgba(255, 255, 255, 0.2); 
    width: 10px;
    border-radius:5px  */
  }
  /* #my-scroll::-webkit-scrollbar-thumb{
    background-color: red;
    border-radius:5px 
  }
  #my-scroll::-webkit-scrollbar-button:vertical:start:decrement{
    display:none;
  }
  #my-scroll::-webkit-scrollbar-button:vertical:end:increment{
    display:none;
  } */
  @media (max-width: 420px) {
    .sidebar li .tooltip {
      display: none;
    }
}
/* @media print{
  .sidebar { 
    display: none;
    padding: 0px;
    margin: 0px;
  }
  body {
    padding:0px;
  }
} */
</style>
