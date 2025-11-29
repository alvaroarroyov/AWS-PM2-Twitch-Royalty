# 🎰 Twitch Loyalty Engine (Cloud-Native)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![TwitchIO](https://img.shields.io/badge/TwitchIO-2.6.0-9146FF?logo=twitch&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazon-aws&logoColor=white)
![Database](https://img.shields.io/badge/Data-JSON-lightgrey)

### 🚧 Project Status: Live & Deployed

This is a server-side engagement system designed to increase viewer retention on Twitch. It runs on AWS EC2 and manages a persistent economy (points/currency) that survives server restarts, enabling real-time gamification (betting/minigames) via chat IRC.

---

## 🔗 VISUAL PORTFOLIO & BUSINESS CASE
**To see the Live Demo, Gambling Logic, and how I pitch this to clients, please visit my Notion Portfolio:**

### [👉 VIEW FULL PROJECT DOCS ON NOTION 👈](https://www.notion.so/Alvaro-Arroyo-Cloud-Solutions-2b853608ee2980c2a382d7ecc8cc57ed)

---

## ⚡ Key Features
* **Persistent Economy:** User points are stored in a structured JSON database, ensuring no data loss during maintenance.
* **Gamification Logic:** Includes RNG-based minigames (e.g., `!gamble`) to boost chat interaction metrics.
* **Event-Driven:** Reacts instantly to chat events using WebSockets.
* **Scalable:** Designed to run multiple instances on a single AWS micro-instance.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Library:** TwitchIO v2.6.0 (Stable)
* **Storage:** Local JSON Persistence (NoSQL-style structure)
* **Deployment:** AWS EC2 (Ubuntu 24.04 LTS) managed via PM2.

## 🚀 Installation (Local Dev)

1.  **Clone the repository**
    ```bash
    git clone [git remote add origin https://github.com/alvaroarroyov/AWS_PM2_Twitch_Royalty.git]
    cd Twitch-Loyalty-Engine
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Create a `.env` file in the root directory. You need a Twitch OAuth Token 
    ```env
    TMI_TOKEN=oauth:your_token_here
    PREFIX=!
    CHANNEL=target_channel_name
    ```

4.  **Run the Bot**
    ```bash
    python twitch_bot.py
    ```

---
*Built by Alvaro Arroyo - Cybersecurity Student & Cloud Builder.*
