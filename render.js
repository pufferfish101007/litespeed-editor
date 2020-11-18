export default function(h) {
  if (this.error) return h("errorScreen", this.error);
  else if (this.loading || this.error) {
    return h(
      "div",
      { style: { backgroundColor: "#4C97FF", width: "100%", height: "100%", color: "white" } },
      [
        this.error ? h("div", {class: "errorText"}, this.error) : h("loadingText", {class: ["loading-text"]})
        ]
    );
  }
  else
    return h(
      "h1",
      {
        on: {
          click: this.onclick
        }
      },
      this.string
    );
  
}
