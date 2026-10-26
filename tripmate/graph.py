from __future__ import annotations

from langgraph.graph import END, StateGraph

from .agents import activity_agent, flight_agent, hotel_agent, planner_agent, research_agent
from .state import TripState


def build_trip_graph():
    workflow = StateGraph(TripState)

    workflow.add_node("research", research_agent)
    workflow.add_node("flight", flight_agent)
    workflow.add_node("hotel", hotel_agent)
    workflow.add_node("activity", activity_agent)
    workflow.add_node("planner", planner_agent)

    workflow.set_entry_point("research")
    workflow.add_edge("research", "flight")
    workflow.add_edge("flight", "hotel")
    workflow.add_edge("hotel", "activity")
    workflow.add_edge("activity", "planner")
    workflow.add_edge("planner", END)

    return workflow.compile()
