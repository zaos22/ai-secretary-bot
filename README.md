# 🤖 AI-Powered Gmail to Calendar Bot

Automate your scheduling. This bot scans unread emails, uses OpenAI to detect events requiring your presence, and ignores trivial dates (like "today" or "sent date").

## Setup
1. Place your `credentials.json` from Google Cloud in the root.
2. Create a `.env` file with your `OPENAI_API_KEY`.
3. Run `pip install -r requirements.txt`.
4. Run `python main.py` and authorize the app.

## Logic
- **Exclusion:** It strictly ignores events scheduled for the day the email was written or received.
- **Context:** Only schedules events that imply attendance (physical or virtual).