# 🚀 InsightBot: Chat With Your Database Like a Boss

> 💡 Turn questions into insights. No SQL. No tickets. Just answers — instantly.

Welcome to **InsightBot** — the AI-powered sidekick your cross-functional teams have been begging for. It's like having a personal data analyst… who works 24/7, never complains, and answers in seconds.

🔮 Powered by **OpenAI GPT-4**  
⚙️ Built with **Flask + PostgreSQL**  
📊 Designed for **humans, not engineers**

---

## 🔥 Why This Exists

Let’s be real — most teams **hate asking for data.**  
You open a ticket, wait 3 days, and get a dashboard that *almost* answers your question.

**InsightBot changes that.**  
Now, anyone on your team can ask:

> “What was our revenue in India last week?”  
> “How many new riders signed up in NYC this month?”  
> “Trend of completed rides in Brazil Q1 vs Q2?”

🎯 Instant answers. No SQL. No bottlenecks. Just **business velocity.**

---

## 🧠 What It Does

✅ Translates natural language → perfect SQL  
✅ Understands your database schema  
✅ Talks to your PostgreSQL backend  
✅ Returns results in a clean, chat-style UI  
✅ Trained on your table metadata for scary-good accuracy

---

## 🖼️ Screenshots That Sell It

> _“WHAT IS THE AVERAGE WAIT TIME FOR A RIDE IN MINUTES? ”_  
<img width="683" alt="image" src="https://github.com/user-attachments/assets/42366a5b-3035-421f-aaed-7e7f8a94aebd" />


> _Boom. SQL generated. Results delivered._  
```sql
 SELECT AVG(EXTRACT(EPOCH FROM avg_wait_time) / 60.0) AS average_wait_time_minutes FROM daily_rides;
```
