# AI-Powered News Newsletter Generator

## Overview
This project automates the process of collecting, summarizing, and distributing current news articles through an email newsletter. It retrieves the latest headlines on user-selected topics, summarizes them using an AI language model (OpenAI), and formats them into a clean, professional email ready for delivery.

The goal is to eliminate the time-consuming process of manually searching for, reading, and curating news content while still keeping users informed about relevant topics.

---

## Features
- **Automated News Retrieval:** Uses the NewsAPI service to fetch the latest articles from reliable sources based on chosen keywords or topics.
- **AI Summarization:** Integrates with the OpenAI API to generate concise, readable summaries suitable for an email format.
- **Email Delivery:** Sends formatted summaries directly to one or more recipients using SMTP (or a third-party service).
- **Customizable Schedule:** Can be automated using the Windows Task Scheduler or cron (macOS/Linux) to run daily or weekly without manual input.
- **Configurable Parameters:** Easily change topics of interest, the number of articles, and recipient details.

---

## Project Structure
ai_newsletter/
│
├── main.py # Main application entry point
├── config.py # Stores API keys and credentials (excluded from GitHub)
├── requirements.txt # Lists all required Python packages
├── .gitignore # Ensures sensitive data and unnecessary files are not tracked
└── README.md # Project documentation and setup instructions

## Setup Instructions

Follow these steps to properly set up and run the AI-Powered News Newsletter Generator on your local machine. This section covers cloning the repository, installing dependencies, configuring your API keys, verifying functionality, and optional automation.

### 1. Clone the Repository
Begin by cloning the repository from GitHub to your computer.  
Open a terminal or command prompt and run the following commands:
```bash
git clone https://github.com/<your-username>/ai-newsletter-generator.git
cd ai-newsletter-generator
```
This will create a local copy of the project on your machine and move you into the project directory.

### 2. Install Dependencies
Ensure that you have **Python 3.9 or higher** installed on your system.  
Next, install the required Python packages listed in `requirements.txt` by running:
```bash
pip install -r requirements.txt
```
This installs the libraries necessary for the project, including:
- `requests` – for fetching data from the News API
- `openai` – for generating article summaries
- `python-dotenv` – for managing environment variables if you choose to use them later

### 3. Configure API Keys and Email Credentials
Create a file named `config.py` in the main project directory if it does not already exist.  
This file will store your API keys and email credentials securely.  
Add the following example code to it:
```python
OPENAI_API_KEY = "your-openai-api-key"
NEWS_API_KEY = "your-news-api-key"
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"
```
**Important:**  
The `.gitignore` file already excludes `config.py`, so this file (and your keys) will never be uploaded to GitHub.

### 4. Run and Verify the Application
To confirm everything is set up correctly, run the main Python file:
```bash
python main.py
```
If setup is successful, a confirmation message will appear in the terminal (such as “AI-Powered News Newsletter Generator - Project initialized successfully”).  
Later in development, this script will:
1. Fetch the latest news articles from the NewsAPI.
2. Summarize them using OpenAI’s API.
3. Format and send them as a professional email newsletter.

### 5. (Optional) Automate Daily Execution
Once the project is working, you can automate the script to run at specific times:
- **Windows:** Use Task Scheduler to execute `python main.py` daily or weekly.
- **macOS/Linux:** Use a cron job to automate the same command.

### 6. Troubleshooting
If something doesn’t work as expected:
- Ensure all dependencies installed without errors.
- Check that your Python version is 3.9 or higher.
- Double-check your API keys in `config.py` for typos or invalid keys.
- Re-run the install command if needed:
```bash
pip install -r requirements.txt
```

### 7. Future Enhancements
Planned improvements and optional features include:
- Improved error handling for API and email issues.
- Support for multiple news topics in one email.
- Enhanced HTML/CSS formatting for cleaner newsletter design.
- Logging features to monitor automated runs.



