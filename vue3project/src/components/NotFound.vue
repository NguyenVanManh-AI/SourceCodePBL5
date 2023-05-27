<template>
	<div id="notFound">
		<h1 style="font-size: 100px;text-align: center;padding-top: 100px;">PAGE NOT FOUND !</h1>
		<div style="display: flex;justify-content: center;width: 100%;">
			<img width="300" src="./../assets/404.jpg" style="display:block;">
		</div>
		<button @click="home" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-house"></i> HOME</button>
	</div>
</template>

<script>
export default{
    name : 'NotFound',
    setup() {
      document.title = "Page Not Found";
    },
    methods:{
      home:function(){
        this.$router.push({name:'UserLogin'});
      }
    }
}

</script>

<style scoped>
#notFound {
	height: 100vh;
}
/* btn add */
.btn-pers {
  bottom: 100px;
  position: absolute;
  left: 50%;
  padding: 1em 2.5em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #0085FF;
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
  background-color: #0085FF;
  box-shadow: 0px 15px 20px rgba(46, 138, 229, 0.4);
  color: #fff;
  transform: translate(-50%, -7px);
}

.btn-pers:active {
  transform: translate(-50%, -1px);
}

</style>