from __future__ import annotations

from typing import List

from .state import TripState


def research_agent(state: TripState) -> TripState:
    destination = state["destination"]
    preferences = ", ".join(state["preferences"]) or "city sightseeing"
    weather_summary = (
        f"{destination} is a strong fit for a trip focused on {preferences}. "
        "The destination offers a balanced mix of culture, food, and convenience for a short getaway."
    )
    return {
        **state,
        "weather_summary": weather_summary,
    }


def flight_agent(state: TripState) -> TripState:
    destination = state["destination"]
    budget = state["budget"]
    flight_options = (
        f"Recommended flight plan for {destination}: book a morning departure, keep travel times under 8 hours, "
        f"and target a fare around {budget}."
    )
    return {**state, "flight_options": flight_options}


def hotel_agent(state: TripState) -> TripState:
    destination = state["destination"]
    preferences = ", ".join(state["preferences"]) or "comfortable and well-located"
    hotel_options = (
        f"Stay in a central district near {destination} with walkable access to {preferences}. "
        "Prioritize a boutique hotel or well-rated apartment with easy transit connections."
    )
    return {**state, "hotel_options": hotel_options}


def activity_agent(state: TripState) -> TripState:
    destination = state["destination"]
    preferences = ", ".join(state["preferences"]) or "local experiences"
    activity_plan = (
        f"Plan a balanced itinerary in {destination} with must-see landmarks, local food stops, and downtime. "
        f"Focus on {preferences} while leaving at least one flexible afternoon for spontaneous exploration."
    )
    return {**state, "activity_plan": activity_plan}


def planner_agent(state: TripState) -> TripState:
    destination = state["destination"]
    departure_date = state["departure_date"]
    return_date = state["return_date"]
    budget = state["budget"]
    final_itinerary = (
        f"Itinerary for {destination}: travel from {departure_date} to {return_date}. "
        f"Use the flight plan to stay within {budget}, secure a centrally located stay, and structure the trip around the weather summary and activity plan. "
        f"Suggested flow: arrival day, local highlights, food and culture day, flexible exploration day, and a final departure day."
    )
    return {**state, "final_itinerary": final_itinerary}
