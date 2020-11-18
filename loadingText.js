export default {
  render(h) {
    return h("div", [
      h("svg", { id: "loading-blocks-svg" }, this.loadingBlocksSvg),
      h("h2", "Loading project"),
      h("transition",  {name: "loading-text"}, [h("p", this.loadingText)])
    ]);
  },
  data () {
    return {
      loadingText: "Creating blocks ...",
      loadingBlocksSvg: null,
      textTimeout: null,
      svgInterval: null
    }
  },
  mounted () {
    this.svgUpdater();
    this.textUpdater();
  },
  beforeDestroy () {
    clearTimeout(this.textTimeout);
    clearInterval(this.svgInterval);
  },
  methods: {
    textUpdater () {
      this.textTimeout = setTimeout(() => {
        this.loadingText = "Loading sprites ..."
      }, 3000)
    },
    svgUpdater () {
      
    }
  }
};
