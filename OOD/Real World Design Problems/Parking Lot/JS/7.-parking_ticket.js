class ParkingTicket{
    #ticketNo;
    #timestamp;
    #exit;
    #amount;
    #status;
    #vehicle;
    #payment;
    #entrance;
    #exitIns;

    constructor(ticketNo, timestamp, exit,amount, status, vehicle, payment, entrance, exitIns) {
        this.#ticketNo = ticketNo;
        this.#timestamp = timestamp;
        this.#exit = exit;
        this.#amount = amount;
        this.#status = status;

        // Following are the instances of their respective classes
        this.#vehicle = vehicle;
        this.#payment = payment;
        this.#entrance = entrance;
        this.#exitIns = exitIns;
    }
}