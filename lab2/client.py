#!/usr/bin/env python3
"""
Hotel Management System - Test Client
"""

import traceback
from datetime import date, timedelta

from hotel import (
    Hotel,
    add_room,
    calculate_reservation_cost,
    cancel_reservation,
    check_reservation_conflict,
    create_room,
    filter_reservations,
    filter_rooms,
    get_all_reservations,
    get_all_rooms,
    get_available_rooms,
    make_reservation,
    new_hotel,
    sort_rooms,
)

TODAY = date(2025, 1, 1)


def __pretty_ok(ok: bool):
    return "✓" if ok else "✗"


def test_basic_functionality() -> Hotel:
    """Test basic hotel creation and room management."""
    print("=== Test: Podstawowa funkcjonalność ===")

    # Create hotel
    hotel = new_hotel("Grand Hotel Warszawa")
    print(f"Utworzono hotel: {hotel}")

    # Add rooms
    rooms_to_add = [
        create_room(101, beds=1, has_tv=True, price_per_night=120.0),
        create_room(102, beds=2, has_tv=True, has_bathtub=False, price_per_night=180.0),
        create_room(103, beds=2, has_tv=True, has_bathtub=True, price_per_night=250.0),
        create_room(201, beds=1, has_tv=False, has_bathtub=False, price_per_night=90.0),
        create_room(202, beds=3, has_tv=True, has_bathtub=True, price_per_night=320.0),
        create_room(203, beds=2, has_tv=True, has_bathtub=True, price_per_night=280.0),
    ]

    for room in rooms_to_add:
        hotel = add_room(hotel, room)

    print(f"Dodano {len(get_all_rooms(hotel))} pokoi:")
    for room in get_all_rooms(hotel):
        amenities = []
        if room.has_tv:
            amenities.append("TV")
        if room.has_bathtub:
            amenities.append("wanna")
        amenities_str = ", ".join(amenities) if amenities else "brak"
        print(
            f"  Pokój {room.room_number}: {room.beds} łóżka, "
            f"{amenities_str}, {room.price_per_night:.2f} PLN/noc"
        )

    print()
    return hotel


def test_filtering(hotel: Hotel) -> None:
    """Test room filtering with user functions."""
    print("=== Test: Filtrowanie pokoi ===")

    # Filter rooms with 2 beds
    two_bed_rooms = filter_rooms(hotel, lambda r: r.beds == 2)
    print(f"Pokoje z 2 łóżkami ({len(two_bed_rooms)} znalezionych):")
    assert len(two_bed_rooms) == 3
    for room in two_bed_rooms:
        print(f"  Pokój {room.room_number}")

    # Filter rooms with bathtub
    bathtub_rooms = filter_rooms(hotel, lambda r: r.has_bathtub)
    print(f"\nPokoje z wanną ({len(bathtub_rooms)} znalezionych):")
    assert len(bathtub_rooms) == 3
    for room in bathtub_rooms:
        print(f"  Pokój {room.room_number}")

    # Filter budget rooms (price < 150)
    budget_rooms = filter_rooms(hotel, lambda r: r.price_per_night < 150)
    print(f"\nPokoje budżetowe < 150 PLN ({len(budget_rooms)} znalezionych):")
    assert len(budget_rooms) == 2
    for room in budget_rooms:
        print(f"  Pokój {room.room_number}: {room.price_per_night:.2f} PLN/noc")

    print()


def test_sorting(hotel: Hotel) -> None:
    """Test room sorting with user functions."""
    print("=== Test: Sortowanie pokoi ===")

    # Sort by price
    by_price = sort_rooms(hotel, lambda r: r.price_per_night)
    print("Pokoje sortowane po cenie (rosnąco):")
    for room in by_price:
        print(f"  Pokój {room.room_number}: {room.price_per_night:.2f} PLN/noc")

    # Sort by number of beds (descending)
    by_beds = sort_rooms(hotel, lambda r: -r.beds)
    print("\nPokoje sortowane po liczbie łóżek (malejąco):")
    for room in by_beds:
        print(f"  Pokój {room.room_number}: {room.beds} łóżka")

    # Sort by room number
    by_number = sort_rooms(hotel, lambda r: r.room_number)
    print("\nPokoje sortowane po numerze:")
    for room in by_number:
        print(f"  Pokój {room.room_number}")

    print()


def test_reservations(hotel: Hotel) -> Hotel:
    """Test making and managing reservations."""
    print("=== Test: Rezerwacje ===")

    # Make some reservations
    tomorrow = TODAY + timedelta(days=1)
    in_3_days = TODAY + timedelta(days=3)
    in_5_days = TODAY + timedelta(days=5)
    in_7_days = TODAY + timedelta(days=7)
    in_9_days = TODAY + timedelta(days=9)

    for reservation_args, expected_result in [
        ((101, "Jan Kowalski", TODAY, in_3_days), True),
        ((102, "Anna Nowak", tomorrow, in_5_days), True),
        ((101, "Piotr Wiśniewski", tomorrow, in_5_days), False),
        ((101, "Ewa Wiśniewska", in_3_days, in_7_days), True),
        ((201, "Adam Grek", in_3_days, in_7_days), True),
        ((201, "Anna Grek", tomorrow, in_7_days), False),
        ((201, "Anna Grek", in_5_days, in_7_days), False),
        ((201, "Anna Grek", in_5_days, in_9_days), False),
        ((201, "Anna Grek", tomorrow, in_3_days), True),
        ((102, "Kacper Kowalewski", in_5_days, in_7_days), True),
    ]:
        success, res, hotel = make_reservation(hotel, *reservation_args)
        print(f"Rezerwacja {reservation_args}: {__pretty_ok(success)}")
        if expected_result:
            assert success is True, (
                f"Rezerwacja {reservation_args} powinna się udać, lecz NIE udała się"
            )
        else:
            assert success is False, (
                f"Rezerwacja {reservation_args} NIE powinna się udać, lecz udała się"
            )
            assert res is None

    print(f"\nLiczba aktywnych rezerwacji: {len(get_all_reservations(hotel))}")
    assert len(get_all_reservations(hotel)) == 6

    print()

    return hotel


def test_reservation_conflicts(hotel: Hotel) -> None:
    """Test conflict detection."""
    print("=== Test: Wykrywanie konfliktów ===")

    in_4_days = TODAY + timedelta(days=4)

    for reservation_args, expected_result in [
        ((102, TODAY, in_4_days), True),
        ((203, TODAY, in_4_days), False),
    ]:
        has_conflict = check_reservation_conflict(hotel, *reservation_args)
        print(f"Czy jest konflikt dla {reservation_args}: {__pretty_ok(has_conflict)}")
        assert has_conflict is expected_result

    print()


def test_filtering_reservations(hotel: Hotel) -> None:
    """Test filtering reservations."""
    print("=== Test: Filtrowanie rezerwacji ===")

    # Filter by guest name
    jan_reservations = filter_reservations(
        hotel, lambda r: r.guest_name == "Jan Kowalski"
    )
    print(f"Rezerwacje dla Jan Kowalski ({len(jan_reservations)} znalezionych):")
    assert len(jan_reservations) == 1
    for res in jan_reservations:
        print(f"  Pokój {res.room_number}: {res.check_in} - {res.check_out}")

    # Filter by room number
    room_101_reservations = filter_reservations(hotel, lambda r: r.room_number == 101)
    print(f"\nRezerwacje pokoju 101 ({len(room_101_reservations)} znalezionych):")
    assert len(room_101_reservations) == 2
    for res in room_101_reservations:
        print(f"  {res.guest_name}: {res.check_in} - {res.check_out}")

    print()


def test_available_rooms(hotel: Hotel) -> None:
    """Test getting available rooms."""
    print("=== Test: Dostępne pokoje ===")

    in_2_days = TODAY + timedelta(days=2)
    in_4_days = TODAY + timedelta(days=4)

    # Get all available rooms
    available = get_available_rooms(hotel, in_2_days, in_4_days)
    print(f"Dostępne pokoje ({in_2_days} - {in_4_days}): {len(available)} pokoi")
    for room in available:
        print(f"  Pokój {room.room_number}: {room.price_per_night:.2f} PLN/noc")

    # Get available rooms with filter (only with bathtub)
    available_with_bathtub = get_available_rooms(
        hotel, in_2_days, in_4_days, lambda r: r.has_bathtub
    )
    print(f"\nDostępne pokoje z wanną: {len(available_with_bathtub)} pokoi")
    for room in available_with_bathtub:
        print(f"  Pokój {room.room_number}")
    assert len(available_with_bathtub) == 3

    print()


def test_cancellation(hotel: Hotel) -> None:
    """Test reservation cancellation."""
    print("=== Test: Anulowanie rezerwacji ===")

    initial_count = len(get_all_reservations(hotel))

    # Cancel existing reservation
    success, hotel = cancel_reservation(hotel, 101, "Jan Kowalski", TODAY)
    print(f"Anulowanie rezerwacji Jan Kowalski, pokój 101: {__pretty_ok(success)}")
    assert success is True
    assert len(get_all_reservations(hotel)) == initial_count - 1

    # Try to cancel non-existent reservation
    success, hotel = cancel_reservation(hotel, 999, "Nieistniejący Gość", TODAY)
    print(f"Anulowanie nieistniejącej rezerwacji: {__pretty_ok(success)}")
    assert success is False

    print()


def test_cost_calculation(hotel: Hotel) -> None:
    """Test reservation cost calculation."""
    print("=== Test: Kalkulacja kosztów ===")

    for reservation in get_all_reservations(hotel):
        cost = calculate_reservation_cost(reservation, hotel)
        nights = (reservation.check_out - reservation.check_in).days
        print(
            f"Rezerwacja {reservation.guest_name}, pokój {reservation.room_number}: "
            f"{nights} nocy = {cost:.2f} PLN"
        )

    print()


def main() -> None:
    """Run all tests."""
    print("=" * 60)
    print("Hotel Management System - Test Client")
    print("=" * 60)
    print()

    try:
        hotel = test_basic_functionality()
        test_filtering(hotel)
        test_sorting(hotel)
        hotel = test_reservations(hotel)
        test_reservation_conflicts(hotel)
        test_available_rooms(hotel)
        test_filtering_reservations(hotel)
        test_cancellation(hotel)
        test_cost_calculation(hotel)

        print("=" * 60)
        print("Wszystkie testy zakończone pomyślnie!")
        print("=" * 60)

    except NotImplementedError as e:
        print(f"\nFunkcja nie została jeszcze zaimplementowana: {e}")
        traceback.print_exc()
    except AssertionError as e:
        print(f"\nTest nie powiódł się: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"\nBłąd podczas testowania: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
