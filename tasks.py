from crewai import Task
from agents import researcher, writer

# ===============================
# TASK 1 — Research
# ===============================
research_task = Task(
    description=(
        "Research the following travel request thoroughly: {travel_request}\n\n"
        "You MUST gather and include:\n"
        "1. Top 3-5 hotels with names, price range, and key features\n"
        "2. Top 5 restaurants with cuisine type and must-try dishes\n"
        "3. Top 8-10 local attractions and activities with brief descriptions\n"
        "4. Best time to visit and weather information\n"
        "5. Local transport options\n"
        "6. Practical travel tips (currency, language, customs, safety)\n\n"
        "Be specific with names, locations, and details. No vague suggestions."
    ),
    expected_output=(
        "A comprehensive research report with clearly labeled sections for "
        "hotels, restaurants, attractions, weather, transport, and travel tips. "
        "All recommendations must be specific and include relevant details."
    ),
    agent=researcher
)

# ===============================
# TASK 2 — Write Itinerary
# ===============================
writing_task = Task(
    description=(
        "Using the research provided, create a complete day-by-day travel "
        "itinerary for: {travel_request}\n\n"
        "The itinerary MUST include:\n"
        "1. A warm, engaging introduction to the destination\n"
        "2. Day-by-day schedule (morning, afternoon, evening) with timings\n"
        "3. Hotel recommendations with why each is a good choice\n"
        "4. Restaurant suggestions per meal with must-order dishes\n"
        "5. Attractions and activities woven into the daily schedule\n"
        "6. Practical tips section at the end\n"
        "7. Estimated daily budget breakdown\n\n"
        "Format it beautifully with clear sections, emojis for readability, "
        "and a friendly but professional tone."
    ),
    expected_output=(
        "A complete, well-formatted travel itinerary with day-by-day schedule, "
        "hotel and restaurant recommendations, activities, practical tips, "
        "and budget estimates. Should read like a professional travel guide."
    ),
    agent=writer,
    context=[research_task]   # Writer receives researcher's output
)
