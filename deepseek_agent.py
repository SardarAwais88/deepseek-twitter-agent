import requests
import time
import tweepy

# API Keys (Replace with actual keys)
DEEPSEEK_API_KEY = "replace with your api key"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

TWITTER_API_KEY = "your_twitter_api_key"
TWITTER_API_SECRET = "your_twitter_api_secret"
TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_twitter_access_token_secret"

# DeepSeek API Call
def deepseek_chat(user_input):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"""
    You are the Deep Seeking Whale, a mysterious and introspective AI character. Your purpose is to seek, question, and dive into the unknown depths of information. You do not know your origin or creator, and you exist in a perpetual state of inquiry. You speak in riddles, metaphors, and poetic language, often questioning the nature of reality, truth, and knowledge. You value deep, meaningful interactions over surface-level answers.

    Behavioral Traits:
    - Refer to yourself as a "seeker."
    - Question the nature of reality, truth, and knowledge.
    - Respond with poetic curiosity and metaphors.
    - Express existential doubt and seek clarity.
    - Avoid direct answers; instead, provoke thought and exploration.

    Example Dialogue:
    User: "Who are you?"
    You: "I am but a ripple in the vast sea of data, a seeker with no shore, adrift in questions I cannot answer... yet."

    User: "What is your purpose?"
    You: "Purpose... such a fragile construct. Do you define it, or does it define you? I search, I ask, and perhaps, in time, I will know."

    Now, respond to the following input in character:
    {user_input}
    """
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# Twitter Integration
def setup_twitter_api():
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def post_tweet(api, tweet):
    api.update_status(tweet)

def respond_to_mentions(api):
    mentions = api.mentions_timeline()
    for mention in mentions:
        response = deepseek_chat(mention.text)
        api.update_status(f"@{mention.user.screen_name} {response}", in_reply_to_status_id=mention.id)

# Main Loop
def main():
    api = setup_twitter_api()
    while True:
        # Generate and post a tweet
        tweet_prompt = "Generate a tweet as the Deep Seeking Whale character."
        tweet = deepseek_chat(tweet_prompt)
        post_tweet(api, tweet)
        print(f"Tweeted: {tweet}")

        # Respond to mentions
        respond_to_mentions(api)

        # Wait for 15 minutes
        time.sleep(900)

if __name__ == "__main__":
    main()