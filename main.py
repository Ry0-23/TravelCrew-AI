from crew_setup import hospitality_crew

print("\n🌍 Welcome to the Multi-Agent Hospitality System\n")
travel_request = input("Enter your travel request (e.g. '5 days in Paris for a couple'): ")

print("\n🤖 Your hospitality crew is working on your itinerary...\n")
result = hospitality_crew.kickoff(inputs={"travel_request": travel_request})

print("\n" + "="*60)
print("✈️  YOUR TRAVEL ITINERARY")
print("="*60)
print(result)
