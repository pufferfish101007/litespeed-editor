/* global Vue */

import loadingText from "./loadingText.js"

import render from "./render.js";
import data from "./data.js";
import computed from "./computed.js";
import methods from "./methods.js"

/* Vue.component("app", {
  components: {
    loadingScreen
  },
  render,
  data() {
    return data;
  },
  computed,
  methods
}); */

var app = new Vue({
  el: "#app",
  render,
  data () {
    return data;
  },
  computed,
  methods,
  components: {
    loadingText
  }
});


setTimeout(() => {
  app.loading = false;
}, 5000)