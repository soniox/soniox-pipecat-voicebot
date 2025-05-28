# Simple Chatbot Server

A Pipecat bot.py file that is built to be deployed to Pipecat Cloud.

## Environment Variables

Copy `env.example` to `.env` and configure:

```ini
SONIOX_API_KEY=          # Your Soniox API key (required for Soniox STT)
OPENAI_API_KEY=          # Your OpenAI API key (required for OpenAI bot)
CARTESIA_API_KEY=        # Your Cartesia API key (for TTS)
DAILY_API_KEY=           # Your Daily API key (LOCAL DEV only)
```

## Running the server locally

Set up and activate your virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python server.py
```

Connect:

- Either connect directly using Daily's Prebuilt UI via http://localhost:7860
- Launch the client app
