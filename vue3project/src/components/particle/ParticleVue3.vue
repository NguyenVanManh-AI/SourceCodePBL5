<template>
  <div class="wrapper">
    <Particles
      class="custom"
      id="particles"
      :particlesInit="particlesInit"
      :particlesLoaded="particlesLoaded"
      :options="particleConfig"
    />
    <!-- <Text class="alignment" /> -->
  </div>
</template>

<script>
// import Text from "./Text.vue";

export default {
  name: "ParticleVue3",
  components: {
    // Text,
  },
  mounted(){
  },
  setup() {
    const particleConfig = {
      background: {
        color: "transparent",
      },
      particles: {
        number: {
          value: 200,
          density: {
            enable: true,
            value_area: 800,
          },
        },
        color: {
          value: "#ffffff",
        },
        shape: {
          type: "circle",
          stroke: {
            width: 0,
            color: "#ffffff",
          },
          polygon: {
            nb_sides: 5,
          },
        },
        opacity: {
          value: 0.5,
          random: false,
          anim: {
            enable: false,
            speed: 1,
            opacity_min: 0.1,
            sync: false,
          },
        },
        size: {
          value: 5,
          random: true,
          anim: {
            enable: false,
            speed: 40,
            size_min: 0.1,
            sync: false,
          },
        },
        line_linked: {
          enable: true,
          distance: 150,
          color: "#ffffff",
          opacity: 0.4,
          width: 1,
        },
        move: {
          enable: true,
          speed: 2,
          direction: "none",
          random: false,
          straight: false,
          out_mode: "out",
          bounce: false,
          attract: {
            enable: false,
            rotateX: 600,
            rotateY: 1200,
          },
        },
      },
      interactivity: {
        detect_on: "canvas",
        events: {
          onhover: {
            enable: true,
            mode: "grab",
          },
          onclick: {
            enable: true,
            mode: "push",
          },
          resize: true,
        },
        modes: {
          grab: {
            distance: 140,
            line_linked: {
              opacity: 1,
            },
          },
          bubble: {
            distance: 400,
            size: 40,
            duration: 2,
            opacity: 8,
            speed: 3,
          },
          repulse: {
            distance: 200,
            duration: 0.4,
          },
          push: {
            particles_nb: 4,
          },
          remove: {
            particles_nb: 2,
          },
        },
      },
      retina_detect: true,
    };
    return { particleConfig };
  },
};
</script>

<style scoped>
.custom {
  height: 100%;
  position: fixed;
  width: 100%;
}
.wrapper {
  height: 300px;
  width: 1220px;
  position: fixed;
}
/* .alignment {
  position: absolute;
  min-width: 100%;
  top: 25%;
} */
canvas{
  /* margin-top: 300px; */
  /* margin-left: 300px; */
  /* position: absolute; */
  /* top:0px; */
  /* left: 300px; */
  /* position: fixed; */
  /* max-width: 40%;
  max-height: 80px;
  margin-top: 10px;
  margin-left: 40%; */
}
</style>