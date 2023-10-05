class Display {
    #floor;
    #capacity;
    #direction;

    constructor(floor, capacity, direction) {
        this.#floor = floor;
        this.#capacity = capacity;
        this.#direction = direction;
    }

    showElevatorDisplay(){};
    showHallDisplay(){};
}