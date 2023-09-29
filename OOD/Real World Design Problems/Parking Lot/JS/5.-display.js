class DisplayBoard {
    // Data members
    #id;
    #handicapped;
    #compact;
    #large;
    #motorCycle;

    constructor(id, handicappedSpot, compactSpot, largeSpot, motorCycleSpot) {
        this.#id = id;
        this.#handicapped = new Array();
        this.#compact = new Array();
        this.#large = new Array();
        this.#motorCycle = new Array();
    }

    // Member functions
    showFreeSlot() {}
}

class ParkingRate {
    // Data members
    #id;
    #hours;
    #rate;
    constructor(id, hours, rate) {
        this.#id = id;
        this.#hours = hours;
        this.#rate = rate;
    }

    // Member function
    calculate() {}
}