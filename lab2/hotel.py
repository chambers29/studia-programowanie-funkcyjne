#!/usr/bin/env python3
"""
Hotel Management System - Business Logic Module

Complete implementation of all functions marked with TODO.
Make sure to use proper type hints and leverage lambda functions,
pattern matching, and higher-order functions where appropriate.
"""

from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Optional

type RoomList = list["Room"]
type ReservationList = list["Reservation"]
type FilterFunction = Callable[["Room"], bool]
type SortFunction = Callable[["Room"], Any]


@dataclass(frozen=True)
class Room:
    """
    Represents a hotel room with its properties.
    """

    beds: int
    has_tv: bool
    has_bathtub: bool
    room_number: int
    price_per_night: float


@dataclass(frozen=True)
class Reservation:
    """
    Represents a room reservation.
    """

    guest_name: str
    room_number: int
    check_in: date
    check_out: date

    def __post_init__(self):
        assert self.check_in <= self.check_out, "Check in must be after check out"


@dataclass(frozen=True)
class Hotel:
    """
    Represents a hotel with rooms and reservations.

    Note: Although lists are mutable, the Hotel object itself is frozen.
          Be sure to clone lists to avoid memory issues!
    """

    # TODO: Add fields with proper type hints
    # HINT: Use field(default_factory=list) for list fields
    pass


def new_hotel(name: str) -> Hotel:
    """
    Creates new Hotel.

    Fields:
    - name: hotel name (str)

    Returns:
        New Hotel object
    """
    # TODO: Create new hotel instance
    raise NotImplementedError


def create_room(
    room_number: int,
    beds: int,
    has_bathtub: bool = False,
    has_tv: bool = False,
    price_per_night: float = 100.0,
) -> Room:
    """
    Create a new room object.

    Args:
        room_number: Unique room identifier
        beds: Number of beds in the room
        has_bathtub: Whether room has a bathtub
        has_tv: Whether room has a TV
        price_per_night: Price per night in PLN

    Returns:
        Room object
    """
    # TODO: Create and return Room object
    raise NotImplementedError


def add_room(hotel: Hotel, room: Room) -> Hotel:
    """
    Add a new room to the hotel.

    Args:
        hotel: Hotel object
        room: Room to be added

    Returns:
        Hotel object with the new room added
    """
    # TODO: Create a new Hotel with the room added
    # HINT: You can use dataclasses.replace() to create a new Hotel with updated rooms list
    raise NotImplementedError


def get_all_rooms(hotel: Hotel) -> RoomList:
    """
    Get all rooms of the hotel.

    Args:
        hotel: Hotel to acquire rooms from

    Returns:
        List of all hotel rooms
    """
    # TODO: Get all rooms
    raise NotImplementedError


def filter_rooms(hotel: Hotel, filter_func: FilterFunction) -> RoomList:
    """
    Filter rooms using a user-provided function.

    Args:
        hotel: Hotel with rooms to filter
        filter_func: Function that takes a Room and returns bool

    Returns:
        List of rooms that match the filter criteria

    Example usage:
        # Filter rooms with 2 or more beds
        big_rooms = filter_rooms(hotel, lambda r: r.beds >= 2)
    """
    # TODO: Filter rooms
    raise NotImplementedError


def sort_rooms(hotel: Hotel, sort_key: SortFunction) -> RoomList:
    """
    Sort rooms using a user-provided key function.

    Args:
        hotel: Hotel with rooms to be sorted
        sort_key: Function that takes a Room and returns a sortable value

    Returns:
        Sorted list of rooms

    Example usage:
        # Sort by price
        sorted_rooms = sort_rooms(hotel, lambda r: r.price_per_night)
    """
    # TODO: Sort rooms
    raise NotImplementedError


def get_all_reservations(hotel: Hotel) -> ReservationList:
    """
    Get all reservations of the hotel.

    Args:
        hotel: Hotel to acquire reservations from

    Returns:
        List of all hotel reservations
    """
    # TODO: Get all reservations
    raise NotImplementedError


def check_reservation_conflict(
    hotel: Hotel,
    room_number: int,
    check_in: date,
    check_out: date,
) -> bool:
    """
    Check if a new reservation would conflict with existing ones.

    Args:
        hotel: Hotel with reservations
        room_number: Room number to check
        check_in: Proposed check-in date
        check_out: Proposed check-out date

    Returns:
        True if there is a conflict, False otherwise

    Note:
        Two reservations conflict if they overlap in time for the same room.
        Consider that check-out on day X and check-in on day X do NOT conflict.
    """
    # TODO: Check for date overlaps in the same room
    raise NotImplementedError


def make_reservation(
    hotel: Hotel,
    room_number: int,
    guest_name: str,
    check_in: date,
    check_out: date,
) -> tuple[bool, Optional[Reservation], Hotel]:
    """
    Make a reservation if the room is available.

    Args:
        hotel: Hotel object
        room_number: Room number to reserve
        guest_name: Name of the guest
        check_in: Check-in date
        check_out: Check-out date

    Returns:
        Tuple of (success: bool, reservation: Optional[Reservation], new_hotel: Hotel)
        - If successful: (True, Reservation object, updated Hotel)
        - If failed: (False, None, original Hotel)

    Note: Returns a NEW Hotel object with the reservation added (functional approach)
    """
    # TODO: Implement reservation logic
    # 1. Check if room exists
    # 2. Check for conflicts
    # 3. If no conflict, create reservation and return new Hotel with it added
    # 4. If conflict or room doesn't exist -> fail
    # HINT: Use dataclasses.replace() to create new Hotel with updated reservations
    raise NotImplementedError


def get_available_rooms(
    hotel: Hotel,
    check_in: date,
    check_out: date,
    filter_func: Optional[FilterFunction] = None,
) -> RoomList:
    """
    Get list of available rooms for given dates, optionally filtered.

    Args:
        hotel: Hotel object
        check_in: Check-in date
        check_out: Check-out date
        filter_func: Optional filter function to apply to available rooms

    Returns:
        List of available rooms (optionally filtered)
    """
    # TODO: Implement availability check
    # 1. Find rooms that have no conflicting reservations
    # 2. If filter_func is provided, apply it to the results
    raise NotImplementedError


def filter_reservations(
    hotel: Hotel, filter_func: Callable[[Reservation], bool]
) -> ReservationList:
    """
    Filter reservations using a user-provided function.

    Args:
        hotel: Hotel to filter reservations from
        filter_func: Function that takes a Reservation and returns bool

    Returns:
        List of reservations that match the filter criteria

    Example usage:
        # Filter reservations for a specific guest
        guest_reservations = filter_reservations(
            hotel.reservations,
            lambda r: r.guest_name == "Jan Kowalski"
        )
    """
    # TODO: Filter reservations
    raise NotImplementedError


def cancel_reservation(
    hotel: Hotel, room_number: int, guest_name: str, check_in: date
) -> tuple[bool, Hotel]:
    """
    Cancel an existing reservation.

    Args:
        hotel: Hotel object
        room_number: Room number of the reservation
        guest_name: Name of the guest
        check_in: Check-in date of the reservation

    Returns:
        Tuple of (success: bool, new_hotel: Hotel)
        - If found: (True, updated Hotel without the reservation)
        - If not found: (False, original Hotel)
    """
    # TODO: Find and remove the matching reservation
    raise NotImplementedError


def calculate_reservation_cost(reservation: Reservation, hotel: Hotel) -> float:
    """
    Calculate total cost of a reservation.

    Args:
        reservation: Reservation object
        hotel: Hotel object

    Returns:
        Total cost in PLN (Nan if reservation is invalid)
    """
    # TODO: Calculate cost based on number of nights and room price
    raise NotImplementedError


# BONUS: Advanced Functions using Pattern Matching (Python 3.10+)


def get_room_description(room: Room) -> str:
    """
    Get a text description of the room using pattern matching.

    Args:
        room: Room object

    Returns:
        Description string

    Example:
        "Pokój 101: 2 łóżka, z wanną i TV, 150.00 PLN/noc"
    """
    # TODO (BONUS): Use match/case to create different descriptions
    raise NotImplementedError


def categorize_room(room: Room) -> str:
    """
    Categorize room into: "Budget", "Standard", "Premium" using pattern matching.

    Args:
        room: Room object

    Returns:
        Category name

    Criteria:
    - Budget: price < 150 PLN
    - Premium: price >= 300 PLN and (bathtub or TV)
    - Standard: everything else
    """
    # TODO (BONUS): Use match/case with guards to categorize
    raise NotImplementedError


# Example usage and testing
if __name__ == "__main__":
    # TODO (OPTIONAL): Add test code here to verify your functions work
    pass
