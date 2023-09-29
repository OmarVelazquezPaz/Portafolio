// Vehicle is an abstract class
class Vehicle {
  #licenseNo;

  constructor(licenseNo) {
    if (this.constructor == Vehicle) {
      throw new Error("Abstract classes can't be instantiated.");
    }
    else {
      this.#licenseNo = licenseNo;
    }
  }

  // ticket here refers to an instance of the ParkingTicket class
  assignTicket(ticket) { }
}

class Car extends Vehicle {
  // ticket here refers to an instance of the ParkingTicket class
  assignTicket(ticket) {
        // definition
    }
}

class Van extends Vehicle {
  // ticket here refers to an instance of the ParkingTicket class
  assignTicket(ticket) {
        // definition
    }
}

class Truck extends Vehicle {
  // ticket here refers to an instance of the ParkingTicket class
  assignTicket(ticket) {
        // definition
    }
}

class MotorCycle extends Vehicle {
  // ticket here refers to an instance of the ParkingTicket class
  assignTicket(ticket) {
        // definition
    }
}