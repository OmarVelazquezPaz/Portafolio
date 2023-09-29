class ParkingLot {
    #id;
    #name;
    #address;
    #parkingRate;

    constructor(id, name, address, parkingRate) {
        if (ParkingLot._instance){
            throw new Error("Singleton classes can't be instantiated more than once.")
        }
        // The ParkingLot is a singleton class that ensures it will have only one active instance at a time
        // Both the Entrance and Exit classes use this class to create and close parking tickets
        ParkingLot._instance = this;

        // Call the name, address, parking_rate elements of the customer in the parking lot from the database
        this.#id = id;
        this.#name = name;
        this.#address = address;
        this.#parkingRate = parkingRate;

        // Create initial entrance and exit hashmaps respectively
        this.entrance = new Map();
        this.exit = new Map();

        // Create a hashmap that identifies all currently generated tickets using their ticket number
        this.tickets = new Map();
    }
    // Created a static method to access the singleton instance of ParkingLot
    static getInstance() {
        if(!ParkingLot._instance){
            return new ParkingLot();
        }
        return ParkingLot._instance;
    }

    // entrance here refers to an instance of the Entrance class
    addEntrance(entrance) {}
    // exit here refers to an instance of the Exit class
    addExit(exit) {}

    // This function allows parking tickets to be available at multiple entrances
    // vehicle here refers to an instance of the Vehicle class
    // Returns a ParkingTicket instance
    getParkingTicket(vehicle) {}

    // type here refers to an instance of the ParkingSpot class
    isFull(type) {}
}