#!/usr/bin/env python3
import argparse
import os
import json
import requests
import re
import sys
import subprocess
import tempfile

# Config file location
CONFIG_FILE = os.path.expanduser("~/.how_config")
API_URL = "https://api.x.ai/v1/chat/completions"

def load_api_key():
    """Load the API key from the config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("api_key")
    return None

def save_api_key(api_key):
    """Save the API key to the config file."""
    config = {"api_key": api_key}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    os.chmod(CONFIG_FILE, 0o600)

def clean_output(text):
    """Clean the AI response for terminal display."""
    # Remove unwanted control characters (except newlines)
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', '', text)
    # Replace triple backticks with single quotes for readability
    text = text.replace('```', "'")
    return text

def query_ai(prompt, api_key):
    """Query the xAI API with the given prompt."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-2-latest",
        "messages": [{"role": "user", "content": prompt+" - Please give me a concise answer, max 500 characters."}],
        "max_tokens": 500,  # Increased to 1000 for longer responses
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        raw_text = result["choices"][0]["message"]["content"]
        # Debug: Save raw response to a file
        with open("/tmp/how_raw_response.txt", "w") as f:
            f.write(raw_text)
        return clean_output(raw_text)
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to AI service - {str(e)}"

def display_output(text):
    """Display the output in the terminal with alternative methods."""
    # Method 1: Use sys.stdout for raw output
    sys.stdout.write(text + "\n")
    sys.stdout.flush()

    # Method 2: Pipe to 'less' for scrollable output (uncomment to use)
    # with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    #     tmp.write(text)
    #     tmp_file = tmp.name
    # subprocess.run(['less', tmp_file])
    # os.unlink(tmp_file)

    # Method 3: Save to file and open with 'cat' (uncomment to use)
    # with open("/tmp/how_output.txt", "w") as f:
    #     f.write(text)
    # subprocess.run(['cat', '/tmp/how_output.txt'])

def main():
    parser = argparse.ArgumentParser(description="Query an AI chatbot from the terminal.")
    parser.add_argument("--q", type=str, help="Question to ask the AI")
    parser.add_argument("--key", type=str, help="Set the xAI API key")
    args = parser.parse_args()

    if args.key:
        save_api_key(args.key)
        print(f"API key saved to {CONFIG_FILE}")
        return

    api_key = load_api_key()
    if not api_key:
        print("Error: No API key found. Set it with: how --key \"<your_api_key>\"")
        return

    if not args.q:
        print("Error: No question provided. Use --q \"your question\"")
        return

    answer = query_ai(args.q, api_key)
    display_output(answer)

if __name__ == "__main__":
    main()