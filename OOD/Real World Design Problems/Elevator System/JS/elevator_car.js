class ElevatorCar {
  #id;
  #door;
  #state;
  #display;
  #panel;
  constructor(id, door, state, display, panel) {
    this.#id = id;
    this.#door = door;
    this.#state = state;
    this.#display = display;
    this.#panel = panel;
  }
  move() {}
  stop() {}
}
