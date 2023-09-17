
import requests
from bs4 import BeautifulSoup
import os
from text_anonymizer import anonymize

# Define the base URL of the website
url = "https://www.cnn.com/"

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
num = 0
limit = 5

for link in soup.find_all('a'):
    href = link.get('href')
    if href is None:
        continue

    # Check if the href ends with 'index.html'
    if href.endswith('index.html'):
        urls.append(href)
        num += 1

    if num >= limit:
        break

# Now, urls contains only the links that end with 'index.html'
for url in urls:
    print(url)


story = 1
for url in urls:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and extract news headlines and descriptions
        headlines = soup.find_all("h1", class_="headline__text inline-placeholder")
        print(headlines)

        descriptions = soup.find_all("div", class_="article__content")
        # print(descriptions)

        # Create a directory to save the .txt files
        if not os.path.exists("../data"):
            os.mkdir("../data")

        # Loop through the headlines and descriptions
        for i, (headline, description) in enumerate(zip(headlines, descriptions), start=1):
            # Extract the text content
            headline_text = headline.get_text().strip()
            description_text = description.get_text().strip()

            # Create a .txt file for each news story
            file_name = f"../data/story_{story}.txt"
            story += 1
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"Headline: {anonymize(headline_text)}\n")
                file.write(f"Description: {anonymize(description_text)}\n")

            # print(f"Saved '{headline_text}' to {file_name}")
    else:
        print(f"Failed to retrieve the webpage (Status Code: {response.status_code})")
