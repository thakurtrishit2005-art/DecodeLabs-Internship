# Project 1: Rule-Based AI Chatbot
### Domain: Control Flow & Deterministic Logic
**Developer:** Trishi Thakur  
**Batch:** 2026  
**Provider:** DecodeLabs Industrial Training Track  

---

## Project Overview
This repository contains the official implementation of **Project 1: The Rule-Based AI Chatbot**. Moving away from the unconstrained probabilities of generative AI models, this project focuses on constructing a highly precise, deterministic "White Box" logic skeleton using strict control flow constraints. 

By mapping discrete user intents to exact programmatic decisions, this script manages user interactions flawlessly without any hallucination risks, ensuring total compliance and predictability.

---

## Architectural Framework: Input -> Process -> Output (IPO)
The system utilizes a structured execution lifecycle to continuously process user expressions:

1. **Input & Sanitization (Raw Feed):**
   * Captures string queries via an interactive loop.
   * Cleans text using standard string normalizations (`.lower().strip()`) to eliminate case and whitespace inconsistencies.
2. **Process (The Logic Skeleton):**
   * Evaluates inputs sequentially using structured conditional workflows.
   * Integrates dynamic utilities such as the native `datetime` module for time/date evaluation.
   * Safely parses inline mathematical strings via isolated algorithmic blocks (`calculate`).
3. **Output (Feedback Loop):**
   * Delivers deterministic responses based on predefined conditions.
   * Gracefully falls back to standard handlers when encountering completely unknown inputs.

---

## Core Project Files
* **`chatbot.py`** — The principal executable script containing the core control loops, sanitization, tracking structures, and interactive command interfaces.

---

## Key Capabilities & Features Covered
* **Infinite Heartbeat Cycle:** Runs in a continuous interactive loop until an explicit kill command (`bye`, `exit`, `quit`) is caught.
* **Temporal Tracking:** Provides instant time and date updates dynamically fetched from system parameters.
* **Inline Math Parsing Engine:** Extracts numeric sub-expressions starting with the keyword `calculate` and returns computed mathematical values.
* **Deterministic Guardrails:** Implements an atomic lookup and fallback mechanism to prevent runtime crashing on unrecognized inputs.

---

## How To Run the Project
Ensure you have Python installed on your local environment (Python 3.x recommended). Run the executable script via your standard command interface:

```bash
python chatbot.py
```

### Example Interaction Block:
```text
Smart AI Assistant
Type 'bye' to exit.

What's your name? Trishi

Hello Trishi! Nice to meet you.

Trishi: hi
Bot: Hello! How are you?

Trishi: calculate (12 * 5) + 8
Bot: Answer = 68

Trishi: time
Bot: Current time is 13:23:27

Trishi: bye
Bot: Goodbye! Have a nice day.
```

---
*Developed as part of the DecodeLabs AI Engineering Framework Portfolio.*