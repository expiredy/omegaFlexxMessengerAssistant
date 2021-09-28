<template>
  <div id="app">
    <Information />
    <Questionnaire />
  </div>
</template>

<script>
import Questionnaire from './components/Questionnaire.vue'
import Information from './components/InfoPart.vue'

export default {
  name: 'App',
  components: {
    Questionnaire,
    Information
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
