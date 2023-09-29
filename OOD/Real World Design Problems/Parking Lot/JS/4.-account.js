class Account {
  #userName;
  #password;
  #person;
  #status;

  // Data members
  constructor(userName, password, person, status) {
    if (this.constructor == Account) {
      throw new Error("Abstract classes can't be instantiated.");
    }
    else {
      this.#userName = userName
      this.#password = password
      this.#person = person // Refers to an instance of the Person class
      this.#status = status // Refers to the AccountStatus enum
    }
  }

  resetPassword() {}
}

class Admin extends Account {
  // spot here refers to an instance of the ParkingSpot class
  addParkingSpot(spot) {}
  // displayBoard here refers to an instance of the DisplayBoard class
  addDisplayBoard(displayBoard) {}
  // entrance here refers to an instance of the Entrance class
  addEntrance(entrance) {}
  // exit here refers to an instance of the Exit class
  addExit(exit) {}

  // Will implement the functionality in this class
  resetPassword() {
    // definition
  }
}

class ParkingAttendant extends Account {
  processTicket(ticketNumber) {}

  // Will implement the functionality in this class
  resetPassword() {
    // definition
  }
}