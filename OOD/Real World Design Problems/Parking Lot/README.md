# Problem definition
A parking lot is a designated area for parking vehicles and is a feature found
in almost all popular venues such as shopping malls, sports stadiums, offices,
etc. In a parking lot, there are a fixed number of parking spots available for
different types of vehicles. Each of these spots is charged according to the
time the vehicle has been parked in the parking lot. The parking time is tracked
with a parking ticket issued to the vehicle at the entrance of the parking lot.
Once the vehicle is ready to exit, it can either pay at the automated exit panel
or to the parking agent at the exit using a card or cash payment method.

## Design approach
To design this parking lot system using the bottom-up design approach.

## The following design patterns can be used to design the parking lot system:

Creational Design Patterns

* Singleton design pattern (there will only be a single instance of the parking lot system.)
* Abstract Factory design pattern (entrance, exit, parking spots, parking rates)
* Factory design pattern (entrance, exit, parking spots, parking rates)

## Requirements collection
The requirements for the parking lot problem:

R1: The parking lot should have the capacity to park 40,000 vehicles.

R2: The four different types of parking spots are handicapped, compact, large,
and motorcycle.

R3: The parking lot should have multiple entrance and exit points.

R4: Four types of vehicles should be allowed to park in the parking lot, which
are as follows:
* Car
* Truck
* Van
* Motorcycle

R5: The parking lot should have a display board that shows free parking spots
for each parking spot type.

R6: The system should not allow more vehicles in the parking lot if the maximum
capacity (40,000) is reached.

R7: If the parking lot is completely occupied, the system should show a message
on the entrance and on the parking lot display board.

R8: Customers should be able to collect a parking ticket from the entrance and
pay at the exit.

R9: The customer can pay for the ticket either with an automated exit panel or
pay the parking agent at the exit.

R10: The payment should be calculated at an hourly rate.

R11: Payment can be made using either a credit/debit card or cash.