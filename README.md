### Multi-Tool AI Agent Engine for Bangladesh

An intelligent, high-efficiency data retrieval and info-synthesis engine optimized for navigating regional public health metrics, commercial facilities, and educational infrastructures across Bangladesh. 

This engine implements an optimized **Dual-Layer Deterministic Router Architecture**. By combining light, native Python keyword interceptors with direct-execution database scripts and an LLM orchestration layer (`llama-3.1-8b-instant` via Groq), the system completely bypasses brittle, multi-turn AI agent reflection loops. Clean, statistical tallies process locally in milliseconds, while deep regional policy queries or unstructured contextual requests elegantly transition to an automated web synthesis engine.

---

#### 🏗️ Project Architecture & Directory Layout

To execute the engine successfully, verify that your workspace directory matches the following structural blueprint:

```text
Project
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

The Directorate General of Health Services (DGHS) is the primary executive agency of Bangladesh's Ministry of Health and Family Welfare, responsible for implementing national health policies, managing public healthcare delivery, and coordinating disease control programs across the country.

**Key Functions:**

1. **Health Policy Implementation**: DGHS plans and executes health initiatives, ensuring the effective implementation of national health policies.
2. **Technical Support**: The agency provides technical support to the Ministry of Health and Family Welfare, enabling informed decision-making.
3. **Health Information Management**: DGHS maintains the national health information portal, facilitating data aggregation and transparency.
4. **Healthcare Delivery**: The agency manages public healthcare delivery, ensuring access to quality healthcare services across the country.

**Structure and Operations:**

DGHS operates from its headquarters in Mohakhali, Dhaka, under the leadership of a Director General, supported by additional directors, line directors, and field officers. The agency's structure emphasizes administrative oversight of medical college hospitals and lower-tier health units, enabling policy execution through a hierarchical network.

**Contribution to Health Gains:**

DGHS has contributed to significant health gains in Bangladesh, including expansions in maternal care infrastructure and digital health strategies aimed at universal coverage. The agency has also played a crucial role in reducing mortality rates over the years.

**Challenges and Controversies:**

Despite its contributions, DGHS has been implicated in systemic health sector challenges, including corruption scandals, doctor absenteeism, and regulatory efficacy gaps. These issues highlight the need for continued reform and improvement in the health sector.

In summary, the Directorate General of Health Services (DGHS) plays a vital role in implementing national health policies, managing public healthcare delivery, and coordinating disease control programs in Bangladesh. While the agency has made significant contributions to health gains, it also faces challenges and controversies that require attention and reform.
```

3. Multi-Attribute Statistical Requests (High-Fidelity Web Synthesis)

```text
Ask: List Top 10 hospitals in Dhaka with bed capacity.

 Processing query via LangChain Routing Executor...

 Answer:
**Top 10 Hospitals in Dhaka, Bangladesh with Bed Capacity**

Based on the latest web search results, here's a comprehensive list of the top 10 hospitals in Dhaka, Bangladesh, along with their bed capacity:

1. **The Square Hospital** - 750 beds
Located in the heart of Dhaka, it's one of the biggest private hospitals in the city, providing world-class medical facilities and services.

2. **Evercare Hospital Dhaka** - 400 beds
A state-of-the-art hospital with a simple and patient-centric approach, offering a wide range of medical services and treatments.

3. **United Hospital Limited** - 650 beds
A leading private hospital in Dhaka, providing comprehensive medical care and services to patients from all over the country.

4. **Dhaka Medical College Hospital** - 2,500 beds
One of the oldest and largest hospitals in Bangladesh, offering a wide range of medical services, including emergency care, surgery, and specialized treatments.

5. **Kurmitola General Hospital** - 1,000 beds
A government-run hospital located in the Kurmitola area of Dhaka, providing medical services to patients from all walks of life.

6. **Apollo Hospital Dhaka** - 300 beds
A private hospital with a reputation for providing high-quality medical care and services to patients from Bangladesh and abroad.

7. **Ibn Sina Hospital** - 250 beds
A private hospital with a focus on providing comprehensive medical care and services to patients, including emergency care and specialized treatments.

8. **Green Life Hospital** - 200 beds
A private hospital with a reputation for providing high-quality medical care and services to patients from Bangladesh and abroad.

9. **Anwer Khan Modern Hospital** - 150 beds
A private hospital with a focus on providing comprehensive medical care and services to patients, including emergency care and specialized treatments.

10. **BDS General Hospital** - 100 beds
A government-run hospital located in the Dhaka city area, providing medical services to patients from all walks of life.

Please note that the bed capacity of these hospitals may be subject to change, and it's always best to verify the information with the hospital directly before visiting.
```

4. Dynamic Academic Keyword Lookups (Direct Database Query)

```text
Ask: Which universities in Bangladesh offer medical degrees?

 Processing query via LangChain Routing Executor...

 Answer:
Here's a clean bulleted list of the institutions matching medical degree tracks:

* FORESIGHT MEDICAL INSTITUTE (PATUAKHALI) - Technical and Vocational
* BENGAL INSTITUTE OF MEDICAL TECHNOLOGY (BRAHAMANBARIA) - Technical and Vocational
* HAJIGONJ MEDICAL INSTITUTE,HAJIGONJ (CHANDPUR) - Technical and Vocational
* CONTINENTAL INSTITUTE OF MEDICAL TECHNOLOGY (CHITTAGONG) - Technical and Vocational
* AVOY ASHRAM INSTITUTE OF MEDICAL TECHNOLOGY (COMILLA) - Technical and Vocational
* KOTBARI SHAHID SMIRITY PARAMEDICAL INSTITUTE (COMILLA) - Technical and Vocational
* LANDMARK PARA-MEDICAL INSTITUTE (COMILLA) - Technical and Vocational
* SOFT-TECH INSTITUTE OF MEDICAL TECHNOLOGY (COMILLA) - Technical and Vocational
* SHYAMOLI IDEAL MEDICAL INSTITUTE (LAKSHMIPUR) - Technical and Vocational
* ASIAN INSTITUTE OF MEDICAL SCIENCE (DHAKA) - Technical and Vocational
```

5. Intent Normalization Guardrail (Spelling Variant Correction)

```text
Ask: Find restaurants in Chittagong serving biryani

 Processing query via LangChain Routing Executor...

 Answer:
**Discover the Best Biryani Restaurants in Chittagong**

If you're craving delicious biryani in Chittagong, we've got you covered. Based on online reviews and ratings, here are some top recommendations:

1. **Al Aqsa Hotel & Biryani House**: This restaurant has a 3.8-star rating on Foodpanda, with reviewers praising its flavorful biryani dishes. You can find it on Foodpanda's website or mobile app.
2. **Handi Restaurant**: This popular eatery has been praised by TripAdvisor users for its mouth-watering Hyderabadi biryani. Its modern location in a busy road adds to its appeal.
3. **Kutumboobadi Restaurant**: Steemit users have raved about this restaurant's special mutton biryani with leg of goat, which they consider the best of 2019. The restaurant offers excellent service, quality food, and a special taste that's worth trying.

**Honorable Mention:**

* **Hotel ABP Biryani House & Restaurant**: Although it's currently closed until Saturday, this restaurant has a good reputation for its biryani dishes.
* **Asian Kabab & Biryani House - GEC**: This restaurant is a great option for those looking for a variety of biryani options.

**Tips:**

* Check the current ratings and reviews on Foodpanda or TripAdvisor before visiting any of these restaurants.
* Be sure to try the special mutton biryani with leg of goat at Kutumboobadi Restaurant, as it's been highly recommended by users.
* Don't hesitate to explore other options in Chittagong, as there are many more restaurants serving delicious biryani dishes.

Enjoy your culinary adventure in Chittagong!
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
Install the required packages using pip. You can bundle these into a requirements.txt file And run:
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