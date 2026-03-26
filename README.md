# ✈️ Multi-Agent Hospitality System

> **AAI-08 | Datagami — Agentic AI | D4 Group 12**  
> A collaborative AI system that researches destinations and crafts complete travel itineraries using two specialized agents.

---

## 🧠 What is this?

A **Multi-Agent Hospitality System** built with **CrewAI** and **Groq (LLaMA 3.1)**. You enter a travel request, and two AI agents collaborate — one researches your destination in real-time, and the other writes a beautifully structured itinerary.

---

## 🤖 Agent Architecture

```
User Input (Travel Request)
        │
        ▼
┌──────────────────────────┐
│  Researcher Agent         │
│  • Hotels & stays         │
│  • Restaurants & dining   │
│  • Attractions & activities│
│  • Weather & transport    │
│  • Travel tips            │
└──────────────────────────┘
        │ hands off research
        ▼
┌──────────────────────────┐
│  Writer Agent             │
│  • Day-by-day schedule    │
│  • Morning/afternoon/eve  │
│  • Budget breakdown       │
│  • Practical tips         │
└──────────────────────────┘
        │
        ▼
  Complete Travel Itinerary
```

---

## ✨ Features

- 🔍 **Real-time web search** — agents search the web for live, accurate info
- 🏨 **Hotel recommendations** — with price range and key features
- 🍽️ **Restaurant suggestions** — with cuisine type and must-try dishes
- 🗺️ **Local attractions** — woven into a day-by-day schedule
- 💰 **Budget estimates** — daily cost breakdown
- 🎨 **Beautiful UI** — warm luxury travel-themed Streamlit interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Multi-Agent Framework | CrewAI |
| LLM | Groq — LLaMA 3.1 8B Instant |
| Web Search | Serper API |
| Frontend | Streamlit |

---

## 📁 Project Structure

```
hospitality-system/
├── app.py              # Streamlit UI
├── agents.py           # Researcher + Writer agents
├── tasks.py            # Research & writing tasks
├── crew_setup.py       # CrewAI crew configuration
├── main.py             # CLI entry point
├── requirements.txt    # Dependencies
└── .env                # API keys (not pushed)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ry0-23/hospitality-system.git
cd hospitality-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
OPENAI_API_KEY=dummy-not-used
```

Get your free API keys:
- Groq → https://console.groq.com/keys
- Serper → https://serper.dev

### 4. Run the app
```bash
streamlit run app.py
```

---

## 👥 Team — D4 Group 12

| # | Name | Enrollment No |
|---|---|---|
| 1 | Harsh Rai | EN22CS301393 |
| 2 | Hemant Dhakad | EN22CS301421 |
| 3 | Gaurav Dwivedi | EN23CS3L1008 |
| 4 | Goutam Verma | EN22CS301375 |
| 5 | Harshwardhan Yadav | EN22CS301416 |

---

## 📄 License

MIT License

---

> *Datagami Agentic AI Course — Project AAI-08 — March 2026* 🌍
