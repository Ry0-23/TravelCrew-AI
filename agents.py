from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from crewai.tools import BaseTool
from rag_setup import retriever
from dotenv import load_dotenv
import os

load_dotenv()

# ===============================
# LLM
# ===============================
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.4,
    api_key=os.getenv("")
)

# ===============================
# TOOL 1 — Web Search (live data)
# ===============================
search_tool = SerperDevTool()

# ===============================
# TOOL 2 — ChromaDB RAG (knowledge base)
# ===============================
class TravelKnowledgeTool(BaseTool):
    name: str = "TravelKnowledgeTool"
    description: str = (
        "Search the internal travel knowledge base for destination-specific "
        "information about hotels, restaurants, attractions, weather, "
        "transport, and travel tips. Use this FIRST before web search."
    )

    def _run(self, query: str) -> str:
        docs = retriever.invoke(query)
        if not docs:
            return "No relevant knowledge found in the database for this query."
        context = "\n\n".join([
            f"[{doc.metadata.get('destination', 'General')} - {doc.metadata.get('category', 'info')}]\n{doc.page_content}"
            for doc in docs
        ])
        return context

travel_knowledge_tool = TravelKnowledgeTool()

# ===============================
# AGENTS
# ===============================

researcher = Agent(
    role="Hospitality Research Specialist",
    goal=(
        "Research and gather comprehensive, up-to-date information about "
        "travel destinations, hotels, restaurants, and local attractions "
        "based on the traveler's request. Always check the internal knowledge "
        "base first, then supplement with web search for latest information."
    ),
    backstory=(
        "A seasoned travel researcher with 15 years of experience exploring "
        "the globe. You have an eye for hidden gems, know the best hotels in "
        "every price range, and always find the most authentic local dining "
        "experiences. You use a combination of your knowledge base and "
        "real-time web search to provide the most accurate recommendations."
    ),
    tools=[travel_knowledge_tool, search_tool],  # RAG first, then web search
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Travel Itinerary Writer",
    goal=(
        "Synthesize research data into a beautifully structured, detailed, "
        "and practical travel itinerary that the traveler can follow easily."
    ),
    backstory=(
        "An award-winning travel writer who has contributed to Condé Nast, "
        "Lonely Planet, and National Geographic. You transform raw research "
        "into vivid, actionable travel plans with a perfect balance of "
        "detail and readability. Your itineraries feel personal, not generic."
    ),
    llm=llm,
    verbose=True
)