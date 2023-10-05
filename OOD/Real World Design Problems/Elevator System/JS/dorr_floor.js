class Door {
  #status;
  constructor(status) {
    this.#status = status;
  }
  isOpen() {}
}

class Floor {
  #display;
  #panel;
  constructor(display, panel) {
    this.#display = display;
    this.#panel = panel;
  }
  isBottomMost() {}
  isTopMost() {}
}
