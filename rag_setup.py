from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os

# ===============================
# EMBEDDINGS
# ===============================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

CHROMA_DIR = "travel_knowledge_db"

# ===============================
# SEED DATA — Built-in travel knowledge
# (No PDFs needed — knowledge is hardcoded here)
# ===============================
TRAVEL_KNOWLEDGE = [
    # ── PARIS ──
    Document(page_content="Paris is best visited in spring (April-June) and fall (September-November). Avoid August when locals leave and it gets crowded with tourists.", metadata={"destination": "Paris", "category": "weather"}),
    Document(page_content="Top hotels in Paris: Le Meurice (luxury, near Tuileries), Hotel des Grands Boulevards (mid-range, trendy), Generator Paris (budget, great location near Canal Saint-Martin).", metadata={"destination": "Paris", "category": "hotels"}),
    Document(page_content="Must-visit attractions in Paris: Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, Montmartre, Palace of Versailles (day trip), Musée d'Orsay, Le Marais district.", metadata={"destination": "Paris", "category": "attractions"}),
    Document(page_content="Best restaurants in Paris: L'Ami Jean (French bistro), Septime (modern French, book ahead), Breizh Café (best crepes), Chez Janou (Provençal), Du Pain et des Idées (best bakery).", metadata={"destination": "Paris", "category": "restaurants"}),
    Document(page_content="Paris transport: Metro is the best way to get around, day pass costs €8. Taxis and Uber available. RER train connects to airports. Vélib bike sharing is great for short trips.", metadata={"destination": "Paris", "category": "transport"}),

    # ── TOKYO ──
    Document(page_content="Tokyo is best visited in spring (March-May) for cherry blossoms or fall (October-November) for autumn leaves. Avoid rainy season in June-July.", metadata={"destination": "Tokyo", "category": "weather"}),
    Document(page_content="Top hotels in Tokyo: Park Hyatt Tokyo (luxury, Shinjuku), Trunk Hotel (mid-range, Shibuya), Khaosan Tokyo (budget, Asakusa). Book well in advance especially during cherry blossom season.", metadata={"destination": "Tokyo", "category": "hotels"}),
    Document(page_content="Must-visit attractions in Tokyo: Senso-ji Temple in Asakusa, Shibuya Crossing, Shinjuku Gyoen Park, teamLab Planets, Tsukiji Outer Market, Akihabara, Harajuku, Tokyo Skytree.", metadata={"destination": "Tokyo", "category": "attractions"}),
    Document(page_content="Best restaurants in Tokyo: Ichiran Ramen (solo ramen booths), Sushi Saito (world-class sushi, reservation required), Gonpachi Nishi-Azabu (inspired Kill Bill), Tsukiji for fresh seafood breakfast.", metadata={"destination": "Tokyo", "category": "restaurants"}),
    Document(page_content="Tokyo transport: IC Card (Suica/Pasmo) is essential — works on all trains, metros, and buses. 24/72 hour metro passes available. Taxis are expensive. Walking is great in districts like Shibuya and Harajuku.", metadata={"destination": "Tokyo", "category": "transport"}),

    # ── BALI ──
    Document(page_content="Bali is best visited during dry season (April-October). Avoid wet season November-March. Ubud is cooler and cultural, Seminyak is beach and nightlife, Canggu is trendy and surfing.", metadata={"destination": "Bali", "category": "weather"}),
    Document(page_content="Top hotels in Bali: Four Seasons Sayan (luxury, Ubud), Alaya Resort Ubud (mid-range), Finn's Beach Club area villas (Canggu). Many beautiful private pool villas available at mid-range prices.", metadata={"destination": "Bali", "category": "hotels"}),
    Document(page_content="Must-visit attractions in Bali: Tanah Lot Temple, Tegallalang Rice Terraces, Uluwatu Temple, Mount Batur sunrise trek, Sacred Monkey Forest Sanctuary, Tirta Empul holy water temple.", metadata={"destination": "Bali", "category": "attractions"}),
    Document(page_content="Best restaurants in Bali: Locavore (fine dining, Ubud), Sarong (Asian fusion, Seminyak), Naughty Nuri's (ribs and cocktails), Warung Babi Guling Ibu Oka (famous suckling pig, Ubud).", metadata={"destination": "Bali", "category": "restaurants"}),
    Document(page_content="Bali transport: Rent a scooter (cheapest, ~$5/day) or hire a private driver (~$40-50/day for full day). Grab (Uber equivalent) works in southern Bali. No reliable public transport.", metadata={"destination": "Bali", "category": "transport"}),

    # ── GENERAL TRAVEL TIPS ──
    Document(page_content="General hotel booking tips: Book at least 2-3 months in advance for peak season. Check cancellation policies. Read recent reviews on TripAdvisor. Consider location over luxury — being central saves transport costs.", metadata={"destination": "general", "category": "tips"}),
    Document(page_content="General travel safety tips: Always get travel insurance. Keep digital copies of passport and important documents. Use hotel safes for valuables. Research local scams before visiting.", metadata={"destination": "general", "category": "safety"}),
    Document(page_content="General budget travel tips: Street food is usually safer and better than tourist restaurants. Use public transport over taxis. Visit free attractions like parks, markets, and temples. Travel shoulder season for better prices.", metadata={"destination": "general", "category": "budget"}),
    Document(page_content="Packing tips for tropical destinations: Light breathable clothes, reef-safe sunscreen, insect repellent, portable charger, universal adapter, microfiber towel. Always pack a light rain jacket.", metadata={"destination": "general", "category": "packing"}),

    # ── INDIA ──
    Document(page_content="India best time to visit: October to March for most regions. Avoid monsoon season June-September except for Kerala backwaters. Rajasthan is best in winter (November-February).", metadata={"destination": "India", "category": "weather"}),
    Document(page_content="Top attractions in India: Taj Mahal in Agra, Jaipur Pink City, Kerala Backwaters, Varanasi ghats, Goa beaches, Leh-Ladakh mountains, Mumbai street food scene.", metadata={"destination": "India", "category": "attractions"}),
    Document(page_content="Indian cuisine must-try dishes: Butter chicken, biryani, dosas, chaat, pani puri, Rajasthani dal baati churma, Kerala fish curry, Hyderabadi biryani, Mumbai vada pav.", metadata={"destination": "India", "category": "restaurants"}),
]


# ===============================
# BUILD OR LOAD VECTOR DB
# ===============================
def get_vector_db():
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        # Load existing DB
        print("📚 Loading existing travel knowledge base...")
        vector_db = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embeddings
        )
    else:
        # Build new DB from seed data
        print("🔨 Building travel knowledge base for the first time...")
        vector_db = Chroma.from_documents(
            documents=TRAVEL_KNOWLEDGE,
            embedding=embeddings,
            persist_directory=CHROMA_DIR
        )
        print(f"✅ Knowledge base built with {len(TRAVEL_KNOWLEDGE)} travel documents!")

    return vector_db


# ===============================
# RETRIEVER
# ===============================
vector_db = get_vector_db()
retriever = vector_db.as_retriever(search_kwargs={"k": 5})