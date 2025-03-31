#!/usr/bin/env python3
import argparse
import os
import json
import requests

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
    # Set file permissions to user-only (600) for security
    os.chmod(CONFIG_FILE, 0o600)

def query_ai(prompt, api_key):
    """Query the xAI API with the given prompt."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-2-latest",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to AI service - {str(e)}"

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Query an AI chatbot from the terminal.")
    parser.add_argument("--q", type=str, help="Question to ask the AI")
    parser.add_argument("--key", type=str, help="Set the xAI API key")
    args = parser.parse_args()

    # Handle API key setup
    if args.key:
        save_api_key(args.key)
        print(f"API key saved to {CONFIG_FILE}")
        return

    # Load the API key
    api_key = load_api_key()
    if not api_key:
        print("Error: No API key found. Set it with: how --key \"<your_api_key>\"")
        return

    # Handle query
    if not args.q:
        print("Error: No question provided. Use --q \"your question\"")
        return

    # Query the AI and print the response
    answer = query_ai(args.q, api_key)
    print(answer)

if __name__ == "__main__":
    main()