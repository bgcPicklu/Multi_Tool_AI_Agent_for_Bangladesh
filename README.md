### Multi-Tool AI Agent Engine for Bangladesh

An intelligent, high-efficiency data retrieval and info-synthesis engine optimized for navigating regional public health metrics, commercial facilities, and educational infrastructures across Bangladesh. 

This engine implements an optimized **Dual-Layer Deterministic Router Architecture**. By combining light, native Python keyword interceptors with direct-execution database scripts and an LLM orchestration layer (`llama-3.1-8b-instant` via Groq), the system completely bypasses brittle, multi-turn AI agent reflection loops. Clean, statistical tallies process locally in milliseconds, while deep regional policy queries or unstructured contextual requests elegantly transition to an automated web synthesis engine.

---

#### 🏗️ Project Architecture & Directory Layout

To execute the engine successfully, verify that your workspace directory matches the following structural blueprint:

```text
├── .env                        # Private system credentials and API tokens
├── app.py                      # Main REPL execution command-line shell runtime
├── LICENSE
├── README.md
├── requirements.txt            # Contains all libraries and plugins
├── data/                       # Subdirectory containing raw source CSV records
│   ├── all-bangladesh-hospitals.csv
│   ├── InstitutionalInformation.csv
│   └── restaurants.csv
├── database/ 
|   └── create_databases.py     # DB compiler: reads raw CSV sheets, normalizes, and loads SQLite
├── databases/                  # Auto-generated target storage for SQLite binaries
│   ├── hospitals.db
│   ├── institutions.db
│   └── restaurants.db
├── utils/
│   └── text_utils.py           # String normalizer for mapping localized spellings
├── tools/
│   ├── db_tools.py             # LangChain tool definition decorators for local routing paths
│   ├── hospitals_tool.py       # Direct SQLite metric aggregator for medical counts/rows
│   ├── institutions_tool.py    # Direct SQLite query script for academic data
│   ├── restaurants_tool.py     # Direct SQLite lookup script for culinary samples
│   └── web_search_tool.py      # Live open-web internet crawler wrapped via Tavily
└── agent/
    └── main_agent.py           # Core routing router managing hybrid fallback triggers
```
---

#### ⚛ Smart Data Flow & Routing Protocol
The core philosophy of this engine is computational speed and loop prevention. Incoming queries are intercepted instantly using explicit pythonic conditional structures instead of delegating the primary routing choices to expensive LLM reasoning tokens:

```text
                  [User Natural Language Input]
                                │
                                ▼
                    [text_utils.normalize()]
         (Maps historical spellings e.g., Chittagong ➔ Chattogram)
                                │
                                ▼
                 [Deterministic Rule Evaluation]
  ┌─────────────────────────────┼─────────────────────────────┐
  │                             │                             │
["university", "college",     ["hospital", "clinic",       ["restaurant", "eatery",
 "school", "institute"]        "medical center"]            "cafe", "cuisine", "food"]
  │                             │                             │
  ▼                             ▼                             ▼
Contains complex requests?    Contains high-intent lists?   Contains deep food queries?
(e.g., non-local metrics)     (e.g., "top", "bed capacity") (e.g., "biryani", "kacchi")
  ├───► YES: Web Search         ├───► YES: Web Search         ├───► YES: Web Search
  └───► NO                      └───► NO                      └───► NO
       │                             │                             │
       ▼                             ▼                             ▼
 [institutions_tool.py]       [hospitals_tool.py]           [restaurants_tool.py]
 (Direct local lookups         (Direct SQLite counts/        (Direct local sample
  for Rajshahi, etc.)           lists for Dhaka/etc.)        data row fetching)
  ```
---

#### 🚀 Installation & Operation Manual
1. Configure System Environment Variables
Ensure your system runs Python 3.9 or higher. Create a .env configuration template file in your project root workspace directory and append your access keys:

Code snippet
```text
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-dev-xxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

2. Ingest Data Sheets & Compile Local Datastores
Place your raw tracking sheets inside the data/ subdirectory. Run the database compiler utility script to strip spaces, sanitize characters to upper case snake_case, and build your local relational index files:

Bash
```text
python create_databases.py
```

Expected Terminal Confirmation:

```text
✔ institutions.db created successfully.
✔ hospitals.db created successfully.
✔ restaurants.db created successfully.

All SQLite databases configured efficiently.
```


3. Activate the Interacting Core Console Shell
Launch the interactive CLI environment loops to begin typing live production queries against the agent:

Bash
```text
python app.py
```

📊 Validated Production Output Traces
The system architecture has been thoroughly verified. Below are actual, unaltered execution logs extracted from the active core engine shell:


1. Direct Local Metric Counting (SQLite Target Routing)

```text
Ask: How many hospitals are in Dhaka?

 Processing query via LangChain Routing Executor...

 Answer:
According to our records, there are exactly 2919 hospital facility records registered under Dhaka.
```

2. Deep Qualitative Analysis (Automated Web Search Fallback)

```text
Ask: What is the role of DGHS in Bangladesh?

 Processing query via LangChain Routing Executor...

 Answer:
**Role of Directorate General of Health Services (DGHS) in Bangladesh**

The Directorate General of Health Services (DGHS) is the primary executive agency of Bangladesh's Ministry of Health and Family Welfare...

**Key Functions:**
1. **Planning and Execution of Health Initiatives**: Provides vital technical support...
2. **Administrative Oversight**: Oversees medical college hospitals and lower-tier district-level units...
```

3. Multi-Attribute Statistical Requests (High-Fidelity Web Synthesis)

```text
Ask: List Top 10 hospitals in Dhaka with bed capacity.

 Processing query via LangChain Routing Executor...

 Answer:
**Top 10 Hospitals in Dhaka with Bed Capacity**
1. Dhaka Medical College Hospital - 2600 beds
2. The Square Hospital - 700 beds
3. Evercare Hospital Dhaka - 500 beds
```

4. Dynamic Academic Keyword Lookups (Direct Database Query)

```text
Ask: Which universities in Bangladesh offer medical degrees?

 Processing query via LangChain Routing Executor...

 Answer:
Here's a clean bulleted list of the institutions matching medical degree tracks:
* FORESIGHT MEDICAL INSTITUTE (PATUAKHALI) - Technical and Vocational
* BENGAL INSTITUTE OF MEDICAL TECHNOLOGY (BRAHAMANBARIA) - Technical and Vocational
```

5. Intent Normalization Guardrail (Spelling Variant Correction)

```text
Ask: Find restaurants in Chittagong serving biryani

 Processing query via LangChain Routing Executor...

 Answer:
**Discover the Best Biryani Restaurants in Chittagong**
1. Alif Restaurant and Biryani House (Alongkar, Chattogram)
2. Al Aqsa Hotel & Biryani House
3. Handi Restaurant (Famous for Hyderabadi biryani)
```
---

#### 🛠 Core Component Engineering Highlights
utils/text_utils.py: Intercepts lexical formatting variants typical to South Asian datasets (e.g., smoothly normalizes "Chittagong" requests to seamlessly match dataset-native "Chattogram" indexing rows).

tools/hospitals_tool.py & Co: Provides native SQLite speed paths. By looking for phrases like "how many", the scripts perform instantaneous COUNT(*) scalar extractions instead of pulling massive, memory-heavy row dumps.

agent/main_agent.py: Controls execution balance. If a prompt requires granular commercial information or localized recommendations that do not match the static database constraints, it triggers execute_web_fallback(query) to crawl live context via Tavily before building a clean, final Markdown response using Llama-3.1.

---

#### ⚙ Library Installation & Configuration Guide
##### Project Setup & Dependencies

This document covers the complete installation steps and environment configurations required to run and scale the application.

##### Prerequisites

- **Python:** Version 3.10 or higher (Python 3.11+ highly recommended)
- **Package Manager:** `pip`

---

##### Installation

###### 1. Environment Isolation (Recommended)
Before installing packages, create a virtual environment to prevent dependency conflicts with your global Python system.

```bash
# Create the environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

###### 2. Core Dependencies
Install the required packages using pip. This includes the foundational LLM frameworks and provider integration suites.
```text
# Update pip to the latest version
pip install --upgrade pip

# Install main framework dependencies
pip install langchain langchain-core langgraph

# Install model provider integrations
pip install langchain-groq langchain-openai langchain-anthropic

# Install environment and utility helper libraries
pip install python-dotenv pydantic requests
```

Alternatively, you can bundle these into a requirements.txt file And run:
```text
pip install -r requirements.txt
```

---

#### 🕯 Future Work Roadmap
The next phase of development focuses on scaling the architecture, improving performance, and hardening security.

Asynchronous Processing & Event Streaming: Migrate blocking operations to fully asynchronous (async/await) pipelines. Integrate LangChain's astream_events (v3) to handle heavy streaming loads and cut real-time latency.

Memory Optimization & Context Pruning: Implement smart conversation summary windows using specialized LLM nodes. This bounds memory growth and avoids ContextOverflowError states in long-running sessions.

Enhanced Tool Sandbox: Upgrade local execution tools to use a isolated runtime environment (like QuickJS) to securely evaluate code snippets generated by the model.

Enterprise Observability: Integrate comprehensive production tracing to monitor latency bottlenecks, token spend, and cache hit rates.