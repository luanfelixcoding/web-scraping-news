# Web Scraping News
This Python project performs web scraping to collect the latest technology news headlines from different sources and saves them to a text file. It also includes a script for scheduling daily news scraping.

---

## Features
**Files**
- ***app.py***: Contains functions to fetch technology news from TechCrunch and The Verge.
- ***daily_news.py***: Uses schedule to automate the execution of news gathering functions at specific times.
---
**Functions**
- ***TechCrunch News Scraping***: Fetches the 10 latest tech headlines from TechCrunch.
- ***The Verge News Scraping***: Fetches the 10 latest tech headlines from The Verge.
- ***Save to File***: Saves the scraped headlines to tech_news.txt, adding a section for each source.
- ***Daily Schedule***: The **daily_news.py** script schedules the news scraping functions to run daily at 3:30 PM.

---

## Project Structure

```
web-scraping-news/
├── app.py           # Main module with web scraping functions.
├── daily_news.py    # Module for scheduling daily execution.
├── requirements.txt # List of Python libraries required for the project.
└── tech_news.txt    # File where the collected headlines are saved.

```

---

## Requirements
- **Python**: 3.9+
- Required Libraries: `requests`, `beautifulsoup4` and `schedule`

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/luanfelixcoding/web-scraping-news.git
    cd web-scraping-news
    
2. **Create a Virtual Environment (optional, but recommended)**:
    ```bash
    python -m venv .venv

3. **Activate the Virtual Environment (venv)**:
    - On Windows: `.venv/Scripts/activate`
    - On Linux/Mac: `source .venv/bin/activate`

4. **Install Dependencies (if any)**:
    ```bash
    pip install -r requirements.txt

5. **Run the Program**:
    ```bash
    python daily_news.py
