from typing import List, TypedDict


class TripState(TypedDict):
    destination: str
    departure_date: str
    return_date: str
    budget: str
    preferences: List[str]
    weather_summary: str
    flight_options: str
    hotel_options: str
    activity_plan: str
    final_itinerary: str
