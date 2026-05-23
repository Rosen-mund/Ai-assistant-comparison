# AI Assistant Comparison

## Project Overview

This project compares:
- an Open Source Assistant using Qwen2.5-0.5B-Instruct
- a Frontier Assistant using Gemini 2.0 Flash API

The application supports:
- multi-turn conversations
- conversational memory
- safety guardrails
- latency tracking
- analytics dashboard
- interaction logging

Deployment:
[Your Hugging Face Space Link]

---

# Features

- Open-source AI assistant
- Frontier AI assistant
- Separate conversational memory
- Harmful prompt guardrails
- Latency benchmarking
- Analytics dashboard
- Interaction logging
- Public deployment on Hugging Face Spaces

---

# Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- Qwen2.5-0.5B-Instruct
- Google Gemini API
- Pandas

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone YOUR_REPO_LINK
cd Ai-assistant-comparison
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
.\venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key
```

---

## 5. Run Application

```bash
streamlit run app.py
```

---

# Architecture Decisions

## 1. Separate Memory Per Assistant

Separate session states were implemented for OSS and Frontier assistants to ensure independent conversational memory and cleaner evaluation.

---

## 2. Lightweight OSS Model Selection

Qwen2.5-0.5B-Instruct was selected because:
- lightweight deployment
- CPU-friendly inference
- Hugging Face deployment compatibility

This involved a tradeoff between reasoning quality and deployment efficiency.

---

## 3. Guardrail Layer

A custom keyword-based safety filtering layer was implemented before model inference to block harmful prompts such as malware or hacking-related instructions.

---

## 4. Latency Tracking

Latency measurement was integrated to compare:
- local inference performance
- hosted API performance

This helped evaluate infrastructure tradeoffs.

---

# Tradeoffs Made

| Decision | Benefit | Tradeoff |
|---|---|---|
| Small OSS model | Faster deployment | Higher hallucination rate |
| Local inference | Low cost | Higher latency |
| Gemini API | Better reasoning | External API dependency |
| Keyword guardrails | Simple implementation | Limited robustness |

---

# Evaluation Summary

The Frontier Assistant demonstrated:
- stronger reasoning
- lower hallucination rates
- better conversational consistency

The OSS Assistant provided:
- lower deployment cost
- local control
- lightweight deployment

---

# Future Improvements

With more development time, the following improvements could be implemented:

- vector database memory
- retrieval augmented generation (RAG)
- advanced guardrails
- authentication system
- tool calling support
- long-term memory
- automated evaluation pipelines
- observability dashboards

---

# Deployment

Hugging Face Space:
[YOUR_DEPLOYMENT_LINK]

---

# Screenshots

(Add screenshots here)

---

# Author

Anwesha Banerjee
