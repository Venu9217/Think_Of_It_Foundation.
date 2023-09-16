import pandas as pd 
import time
import random
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
csv_file = "C:/Users/venuk/Downloads/influencers_data.csv.zip"
column_names = ["name", "headline", "location", "followers", "connections","about","time_spent","content_links","media_type","media_url","num_hashtags","hashtag_followers","hashtags","reactions","comments"]
df = pd.read_csv(csv_file, names=column_names, header=None)
print(df.head())
unique_names = pd.unique(df['name'])
unique_items_df = pd.DataFrame({'name': unique_names})
print(unique_items_df)
delay = random.uniform(2, 5)  # Random delay between 2 to 5 seconds
time.sleep(delay)
user_agent = UserAgent()
headers = {'User-Agent': user_agent.random}
total_creators = 100  
start_index = 1  
for i in range(start_index, total_creators + 1):
    creator_name = unique_items_df['name'] 
    print(f"Processing content creator: {creator_name}")
# Define a function to scrape LinkedIn profiles for recent posts
def scrape_linkedin_profile(profile_url):
    try:
        response = requests.get(profile_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            recent_posts = soup.find_all('div', class_='feed-shared-update-v2 feed-shared-update-v2--minimal-padding feed-shared-update-v2--e2')
            for post in recent_posts:
                post_content = post.find('span', {'class': 'break-words'}).text
                print("Recent Post:")
                print(post_content)
                
        else:
            print(f"Failed to fetch LinkedIn profile. Status code: {response.status_code}")
    except Exception as e: 
        print(f"Error: {e}")

total_creators = 100  
start_index = 1 
for index in range(start_index,total_creators+1):
    content_creator_name = unique_items_df['name']
    profile_url = df['content_links']  
    print(f"Scraping profile for {content_creator_name}")
    scrape_linkedin_profile(profile_url)
def extract_post_urls(profile_url):
    post_urls = []

    try:
        response = requests.get(profile_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            post_links = soup.find_all('a', {'data-control-name': 'view_recent_activity', 'href': True})
            for link in post_links:
                post_url = link['href']
                if '/posts/' in post_url:  
                    full_post_url = f"https://www.linkedin.com{post_url}"
                    post_urls.append(full_post_url)

        else:
            print(f"Failed to fetch LinkedIn profile. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

    return post_urls
for index in range(1,101):
    profile_url = df['content_links']  
    print(f"Scraping post URLs for profile: {profile_url}")
    post_urls = extract_post_urls(profile_url)

    for url in post_urls:
        print("Post URL:", url)
def simulate_like_post(profile_name, post_content):
  
    print(f"Liked the post by {profile_name} with content: {post_content}")


for index in range(1,101):
    profile_name = df['name']
    post_content = df['connections']
    simulate_like_post(profile_name, post_content)
    sleep_duration = random.uniform(5, 5)
    time.sleep(sleep_duration)
comments = [
    "Great post! I completely agree with your insights.",
    "This is very informative and well-written. Thanks for sharing!",
    "I love the way you presented your ideas in this post.",
    "Your content always inspires me. Keep up the good work!",
    "Your perspective on this topic is refreshing. Well done!",
    "I learned a lot from reading your post. Thank you for sharing your knowledge.",
]
def generate_comment():
    return random.choice(comments)
for index in range(1,100):
    content_creator_name = df['name']
    post_content = df['connections']  
    comment = generate_comment()
    print(f"Comment for {content_creator_name}'s post:")
    print(comment)
    print("Post Content:")
    print(post_content)
    print("-" * 50)




