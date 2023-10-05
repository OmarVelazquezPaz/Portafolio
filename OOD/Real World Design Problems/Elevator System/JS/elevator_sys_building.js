class ElevatorSystem {
  #building;
  constructor(building) {
    this.#building = building;
  }
  monitoring() {}
  dispatcher() {}

  // the ElevatorSystem is a Singleton class that ensures it will have
  // only one active instance at a time
  #system = null;

  // Created a static method to access the singleton instance of
  // ElevatorSystem class

  static getInstance() {
    if (system == null) {
      system = new ElevatorSystem();
    }
    return system;
  }
}

class Building {
  #floor;
  #elevator;

  #building = null;

  constructor() {
    this.#floor = new Array();
    this.#elevator = new Array();
  }

  getInstance() {
    if (building == null) {
      building = new Building();
    }
    return building;
  }
}
