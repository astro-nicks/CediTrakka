# CediTrakka



# ✅ **1. `run.sh` (One‑Click Runner Script)**

Create a file called **`run.sh`** in your project root:

```bash
#!/bin/bash

echo "========================================"
echo "   Cedi Trakka – Intelligent Agent"
echo "   DCIT 403 | SPADE Implementation"
echo "========================================"

# Activate virtual environment if one exists
if [ -d "venv" ]; then
    echo "[INFO] Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies if missing
echo "[INFO] Installing required Python packages..."
pip install spade >/dev/null 2>&1

# Run the SPADE agent
echo "[INFO] Starting the Cedi Trakka agent..."
python3 cedi_trakka_agent.py
```

### ✅ Make the script executable

In the Codespaces terminal:

```bash
chmod +x run.sh
```

### ✅ Run the agent with one command:

```bash
./run.sh
```

***

# ✅ **2. `README.md` (GitHub‑Ready Project Documentation)**

Create **`README.md`** in your repository root:

````markdown
# 📱💰 Cedi Trakka – Intelligent Financial Tracking Agent
### DCIT 403 – Intelligent Agent Systems  
### Built with Python + SPADE | Prometheus Methodology

---

# ✅ Project Overview

Cedi Trakka is an **intelligent agent** designed to automatically process **mobile money transaction notifications** (MTN MoMo, Telecel Cash, AirtelTigo) and generate meaningful **financial insights** such as:

- Spending summaries  
- Category classifications  
- Budget warnings  
- Monthly reports  

This project demonstrates how intelligent agents can perceive, reason, act, and interact with an environment using the **Prometheus design methodology**.

---

# ✅ Features

- ✅ Detects and processes mobile money notifications  
- ✅ Extracts amount, type, and timestamp  
- ✅ Classifies spending into categories (Food, Bills, Transport, etc.)  
- ✅ Maintains a transaction history  
- ✅ Analyzes user behavior  
- ✅ Produces alerts (e.g., overspending warnings)  
- ✅ Generates monthly summaries  
- ✅ Follows the perceive → decide → act agent loop  

---

# ✅ Technologies Used

| Component | Details |
|----------|---------|
| **Language** | Python 3.9+ |
| **Agent Framework** | SPADE (Smart Python Agent Development Environment) |
| **Dev Environment** | GitHub Codespaces |
| **Storage** | JSON file (transactions.json) |

---

# ✅ Installation & Setup

### 🔹 1. Clone the repository

```bash
git clone https://github.com/<your-username>/cedi-trakka-agent.git
cd cedi-trakka-agent
````

### 🔹 2. Install dependencies

```bash
pip install spade
```

### 🔹 3. Configure your XMPP Account

Cedi Trakka requires an XMPP account for agent communication.  
Create one at:

*   <https://jabber.hot-chilli.net>
*   <https://conversations.im>
*   <https://jabber.at>

Replace the placeholders in `cedi_trakka_agent.py`:

```python
agent_jid = "youraccount@jabber.hot-chilli.net"
agent_pw = "yourpassword"
```

***

# ✅ Running the Agent

### 🔹 Option A: One‑click shell script

```bash
./run.sh
```

### 🔹 Option B: Run manually

```bash
python3 cedi_trakka_agent.py
```

***

# ✅ How the System Works

### 1. **Perceive**

Simulated mobile money notifications are sent to the agent.

### 2. **Decide**

The agent:

*   Parses the text
*   Extracts structured data
*   Classifies the transaction
*   Analyzes spending patterns

### 3. **Act**

*   Stores transaction in `transactions.json`
*   Sends alerts/warnings
*   Prints insights to console (prototype dashboard)

***

# ✅ Project Structure

    .
    ├── cedi_trakka_agent.py       # Main SPADE agent
    ├── run.sh                     # One-click run script
    ├── transactions.json          # Stored beliefs/transaction history
    └── README.md                 # Documentation                     


***

# ✅ Prometheus Mapping (Design → Implementation)

| Prometheus Artifact | Implementation                                                     |
| ------------------- | ------------------------------------------------------------------ |
| **Percepts**        | Incoming message events                                            |
| **Capabilities**    | SPADE behaviours (Cyclic, Periodic, OneShot)                       |
| **Plans**           | `ParseTransaction()`, `ClassifyTransaction()`, `AnalyzeSpending()` |
| **Beliefs**         | `transactions.json`                                                |
| **Actions**         | Alerts, summaries, console dashboard                               |
| **Scenarios**       | Implemented with simulated sample messages                         |

***

# ✅ Challenges & Limitations

*   Real SMS access is restricted → requires simulation
*   Rule‑based parser may fail on unusual message formats
*   Privacy constraints limit real-world testing
*   Requires stable XMPP server for communication
*   No ML classifier (yet) due to limited real datasets

***

# ✅ Future Improvements

*   Integration with real Android notification listeners
*   Machine-learning classification for improved accuracy
*   Web dashboard (Streamlit/Flask)
*   Multi-agent expansion (fraud detection, budget advisor)

***

# ✅ Author

👤 **Essandoh Astrea Kwame Jnr**  
DCIT 403 – Intelligent Agent Systems

***

# ✅ License

This project is for academic use under the University of Ghana DCIT 403 course.

```

---
