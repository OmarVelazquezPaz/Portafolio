// Enumeration
const PaymentStatus = Object.freeze({
  COMPLETED ,
  FAILED ,
  PENDING ,
  UNPAID ,
  REFUNDED
});

const AccountStatus = Object.freeze({
  ACTIVE,
  CLOSED,
  CANCELED,
  BLACKLISTED,
  NONE
});

// Custom Person data type class
class Person {
  #name;
  #address;
  #email;
  #phone;

  constructor(name, address, phone, email) {
    this.#name = name;
    this.#address = address;
    this.#phone = phone;
    this.#email = email;
  }
}

// Custom Address data type class
class Address {
  #zipCode;
  #address;
  #city;
  #state;
  #country;

  constructor(zipCode, address, city, state, country) {
    this.#zipCode = zipCode;
    this.#address = address;
    this.#city = city;
    this.#state = state;
    this.#country = country;
  }
}