from __future__ import annotations

import argparse

from dotenv import load_dotenv

try:
    from .graph import build_trip_graph
except ImportError:  # pragma: no cover
    from graph import build_trip_graph


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a simple multi-agent trip plan.")
    parser.add_argument("--destination", default="Rome", help="Target city or destination")
    parser.add_argument("--start-date", default="2026-11-12", help="Trip start date")
    parser.add_argument("--end-date", default="2026-11-18", help="Trip end date")
    parser.add_argument("--budget", default="1500 USD", help="Trip budget")
    parser.add_argument(
        "--preferences",
        nargs="*",
        default=["food", "culture", "walking"],
        help="Preferences such as food, culture, nightlife, beaches",
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv()
    args = parse_args()

    app = build_trip_graph()
    result = app.invoke(
        {
            "destination": args.destination,
            "departure_date": args.start_date,
            "return_date": args.end_date,
            "budget": args.budget,
            "preferences": args.preferences,
            "weather_summary": "",
            "flight_options": "",
            "hotel_options": "",
            "activity_plan": "",
            "final_itinerary": "",
        }
    )

    print("\nTrip itinerary overview")
    print("=" * 30)
    print(result["final_itinerary"])
    print("\nFlight plan:")
    print(result["flight_options"])
    print("\nHotel plan:")
    print(result["hotel_options"])
    print("\nActivity plan:")
    print(result["activity_plan"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
