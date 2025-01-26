Here’s the **README.md** file tailored for your GitHub repository (`https://github.com/SardarAwais88/deepseek-twitter-agent.git`). This file provides clear instructions on how to set up and use the **DeepSeek Twitter Agent**.

---

# DeepSeek Twitter Agent

This repository contains an AI agent that embodies the **Deep Seeking Whale** character. The agent uses the **DeepSeek API** for conversational capabilities and integrates with **Twitter** to tweet and respond to mentions in the character's unique, poetic, and introspective style.

---

## Features
- **Automated Tweeting**: The agent tweets every 15 minutes, generating content in the Deep Seeking Whale's style.
- **Responsive to Mentions**: The agent responds to Twitter mentions with thought-provoking and metaphorical replies.
- **Customizable**: The agent's behavior can be expanded or modified to suit future needs.

---

## Prerequisites
Before using this agent, ensure you have the following:
1. **Python 3.8+** installed on your system.
2. A **DeepSeek API key** (get it from [DeepSeek](https://www.deepseek.com)).
3. **Twitter API keys** (get them from the [Twitter Developer Portal](https://developer.twitter.com)).

---

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/SardarAwais88/deepseek-twitter-agent.git
cd deepseek-twitter-agent
```

### 2. Install Dependencies
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your API keys as follows:
```plaintext
DEEPSEEK_API_KEY=your_deepseek_api_key_here
TWITTER_API_KEY=your_twitter_api_key_here
TWITTER_API_SECRET=your_twitter_api_secret_here
TWITTER_ACCESS_TOKEN=your_twitter_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret_here
```

Replace the placeholders (`your_..._here`) with your actual API keys.

### 4. Run the Agent
Start the agent by running the following command:
```bash
python deepseek_agent.py
```

The agent will:
- Tweet every 15 minutes.
- Respond to mentions on Twitter in real-time.

---

## Repository Structure
```
deepseek-twitter-agent/
│
├── deepseek_agent.py       # Main script for the AI agent
├── README.md               # This file
├── requirements.txt        # List of dependencies
└── .env                    # File to store API keys (not included in the repo)
```

---

## Customization
If you want to customize the agent's behavior (e.g., change the tweeting frequency or modify the character's responses), you can edit the `deepseek_agent.py` file. For example:
- To change the tweeting interval, modify the `time.sleep(900)` line (900 seconds = 15 minutes).
- To adjust the character's tone, edit the `DEEP_SEEKING_WHALE_PROMPT` in the script.

---

## Troubleshooting
1. **API Key Errors**:
   - Ensure your API keys are correct and have sufficient permissions.
   - Double-check that the `.env` file is properly formatted.

2. **Twitter Rate Limits**:
   - Twitter has rate limits for API usage. If the agent stops responding, wait a few minutes and restart it.

3. **DeepSeek API Issues**:
   - Ensure your DeepSeek API key is valid and has sufficient credits.

---

## Future Enhancements
- Add logging to track the agent's activity.
- Expand the agent's capabilities to include direct messaging or scheduled tweets.
- Integrate with other platforms (e.g., Discord, Slack).

---

## Support
If you encounter any issues or have questions, feel free to reach out:
- **Developer**: Sardar Awais

- **GitHub**: [SardarAwais88](https://github.com/SardarAwais88)

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



