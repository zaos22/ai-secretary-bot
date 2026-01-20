# 🤖 AI Secretary: Gmail to Calendar & WhatsApp Notifier

An intelligent personal assistant that automates your scheduling. This bot scans unread emails, uses state-of-the-art AI (Gemini 2.5) to detect events, automatically schedules them in Google Calendar, and sends you a real-time notification via WhatsApp.



## 🌟 Key Features

- **Cutting-edge AI:** Powered by `gemini-2.5-flash` to understand natural language and context in emails.
- **Smart Filtering:** Ignores newsletters and receipts; focuses only on appointments, meetings, or events requiring attendance.
- **Custom Business Rules:** Automatically excludes events scheduled for "today" or the same date the email was sent to prevent last-minute conflicts.
- **WhatsApp Notifications:** Sends instant confirmations via Green-API (Group format ensures loud audio alerts).
- **Modular Architecture:** Clean separation between authentication, AI logic, notifications, and execution.

## 📁 Project Structure

```text
bot-calendar/
├── main.py            # Main engine and coordination
├── brain.py         # AI logic using Gemini 2.5
├── auth.py            # Google Token management (Gmail/Calendar)
├── message.py     # WhatsApp API integration
├── config.py          # Global settings and Scopes
├── .env               # Private environment variables
└── requirements.txt   # System dependencies