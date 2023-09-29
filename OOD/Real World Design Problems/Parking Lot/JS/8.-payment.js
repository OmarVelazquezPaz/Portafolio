// Payment is an abstract class
class Payment {
    #amount;
    #status;
    #timestamp;

    constructor(amount, status, timestamp) {
        if (this.constructor == Payment) {
            throw new Error("Abstract classes can't be instantiated.");
        }
        else {
            this.#amount = amount;
            this.#status = status; // Refers to the PaymentStatus enum
            this.#timestamp = timestamp;
        }
    }
    initiateTransaction() { }
}
class Cash extends Payment{
    initiateTransaction(){
        // definition
    }
}
class CreditCard extends Payment{
    initiateTransaction(){
        // definition
    }
}