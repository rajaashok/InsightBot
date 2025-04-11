# 💬 InsightBot: Natural Language Chat for Self-Service Data Insights

![Python](https://img.shields.io/badge/python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-brightgreen)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> 🧠 Ask questions. 💡 Get insights. ⚡ No SQL needed.

**InsightBot** is a conversational AI interface that enables teams to ask natural language questions about business metrics — and get real-time answers from your database. Built with **OpenAI GPT-4**, **Flask**, and **PostgreSQL**, InsightBot empowers cross-functional teams to explore data independently, without writing SQL.

---

## 🌟 Features

- ✅ Ask natural language questions
- 🧠 LLM-generated SQL queries (OpenAI GPT-4)
- 🗂️ Ingests database metadata for better query context
- 💬 Lightweight chat UI
- 🔌 Connects to PostgreSQL (easy to extend to other DBs)
- 🧱 Flask backend with API endpoints

---

## 🖼️ Demo Screenshot

![InsightBot Chat UI](./screenshot.png)

---

## 🛠️ Tech Stack

| Component    | Stack                   |
|--------------|-------------------------|
| Backend      | Flask (Python)          |
| LLM          | OpenAI GPT-4            |
| Database     | PostgreSQL              |
| Metadata     | JSON-based Schema Descriptions |
| Frontend     | HTML/CSS + Vanilla JS   |
| LLM Toolkit  | LangChain (tools + function calling) |

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/insightbot.git
cd insightbot
