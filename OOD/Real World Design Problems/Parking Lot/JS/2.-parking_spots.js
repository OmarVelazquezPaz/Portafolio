// ParkingSpot is an abstract class
class ParkingSpot {
    #id;
    #isFree;
    #vehicle;
    constructor(id, isFree, vehicle) {
        if (this.constructor == ParkingSpot) {
            throw new Error("Abstract classes can't be instantiated.");
        }
        else {
            this.#id = id;
            this.#isFree = isFree;
            this.#vehicle = vehicle; // Refers to an instance of the Vehicle class
        }
    }
    getIsFree() { }
    // vehicle here refers to an instance of the Vehicle class
    assignVehicle(vehicle) { }
    removeVehicle() { }
}

class Handicapped extends ParkingSpot {
    // vehicle here refers to an instance of the Vehicle class
    assignVehicle(vehicle) {
        // definition
    }
}

class CompactSpot extends ParkingSpot {
    // vehicle here refers to an instance of the Vehicle class
    assignVehicle(vehicle) {
        // definition
    }
}

class LargeSpot extends ParkingSpot {
    // vehicle here refers to an instance of the Vehicle class
    assignVehicle(vehicle) {
        // definition
    }
}

class Motorcycle extends ParkingSpot {
    // vehicle here refers to an instance of the Vehicle class
    assignVehicle(vehicle) {
        // definition
    }
}