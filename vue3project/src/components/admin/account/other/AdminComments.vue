<template>
    <div id="helpSupport">
        <ParticleVue32></ParticleVue32>
        <div id="comments">
            <h1 style="color: #0085FF;font-size: 24px;text-align: center;font-weight: bold;"><i class="fa-solid fa-circle-info"></i> Comments</h1>
            <div style="margin-top: 20px;">
                <div class="form-group">
                    <label for="formGroupExampleInput"><i class="fa-solid fa-blog"></i> Content of comments</label>
                    <textarea v-model="content" @keydown.enter.prevent="handleEnter" rows="10" type="text" class="form-control" id="formGroupExampleInput" placeholder="Write comments..."></textarea>
                </div>
                <button @click="submit" class="mt-4 btn-pers" id="login_button" ><i class="fa-solid fa-paper-plane"></i> Submit</button>
            </div>
        </div>
    </div>
</template>
<script>
import ParticleVue32 from "../../../particle/ParticleVue32.vue";
import useEventBus from '../../../../composables/useEventBus'
export default {
    name : "UserComments",
    components: {
        ParticleVue32,
    },
    data(){
        return{
            content:"",
        }
    },
    created(){
  
    },
    mounted(){
        window.document.title='Comments - PBL5';
    },
    methods:{
        handleEnter(event) {
            if (!event.shiftKey) {
                event.preventDefault();
                this.submit();
            }
        },
        submit:function(){
            const { emitEvent } = useEventBus();
            emitEvent('eventSuccess','Send Success !');
            this.content = "";
        }
    },
}
</script>
<style scoped>
#comments {
    margin: auto;
    width: 90%;
    height: 90%;
    margin-top: 40px;
    background-color: white;
    position: relative;
    border-radius: 10px;
    height: 88vh;
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgb(204, 219, 232) -3px -3px 6px 1px inset;
    padding: 20px;
    padding-top: 60px;
}
/* btn add */
.btn-pers {
  bottom: 30px;
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