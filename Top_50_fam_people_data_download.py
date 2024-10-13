#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import lxml
import re


# In[2]:


url ="https://www.thefamouspeople.com/famous-people-by-country.php"
r = requests.get(url)
print(r)
    
soup = BeautifulSoup(r.text, "lxml")
# print(soup)
box = soup.find("div", class_ = "pod colorbar editorial")
# print(box)


# In[7]:


import requests

# Function to download an image from a given URL
def download_image(url, save_path):
    try:
        # Send a GET request to the URL with a timeout
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Open a file in binary write mode and save the content of the response
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded: {save_path}")
        else:
            print(f"Failed to retrieve image. HTTP Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


# In[6]:


Country_url = []
cont = box.find_all("div", class_="col-md-2 contentdata")

# Loop through each div element found
for i in cont:
    # Find the <a> tag within the div (if it exists)
    a_tag = i.find("a")
    # If the anchor tag exists and has an 'href' attribute, append it to the list
    if a_tag and a_tag.get("href"):
        Country_url.append("https:"+a_tag["href"])

print(Country_url)


# In[5]:


Celb_title = []
Celb_img=[]
for name in Country_url:
    r = requests.get(name)
    print(r)

    s = BeautifulSoup(r.text, "lxml")
    
    celb_img_url = s.find_all("img", class_="combi-profile-img")
    
    for img in celb_img_url:
        # Check if 'data-src' exists, if yes, use it; otherwise, use 'src'
        url = img.get('data-src') if img.get('data-src') else img.get('src')
        title = img.get('title')  # Extract the title attribute
        url = "https:"+url
    
        if url:  # Only append if the URL exists
            Celb_img.append(url)
    
        if title:  # Only append if the title exists
            Celb_title.append(title)
        
        image_url = "https://example.com/path-to-image.jpg"
        save_path = "Pictures_People/"+title+".jpg"
        download_image(url,save_path)

