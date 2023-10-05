class Button {
    #status
    constructor(status = null) {
        if (this.constructor == Button) {
          throw new Error("Abstract classes can't be instantiated.");
        }
        else {
          this.#status = status;
        }
    }
    pressDown();
    isPressed();
}

class HallButton extends Button  {
    #buttonSign;
    constructor(status, buttonSign) {
        this.#buttonSign = buttonSign;
        super(status);
    }
    isPressed() {
        // definition
    }
}

class ElevatorButton extends Button  {
    #destinationFloorNumber;
    constructor(status, destinationFloorNumber) {
        this.#destinationFloorNumber = destinationFloorNumber;
        super(status);
    }
    isPressed() {
        // definition
    }
}