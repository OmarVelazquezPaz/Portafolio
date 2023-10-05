class ElevatorPanel {
    #floorButtons;
    #openButton;
    #closeButton;
    constructor(openButton, closeButton) {
        this.#openButton = openButton;
        this.#closeButton = closeButton;
        this.#floorButtons = new Array();
    }
}

class HallPanel {
    #up;
    #down;
    constructor(up, down) {
        this.#up = up;
        this.#down = down;
    }
}