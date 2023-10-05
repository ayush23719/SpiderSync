from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from colorama import Fore, Style  # Added colorama for terminal text color

# Initialize colorama
Fore.YELLOW
Fore.GREEN
Style.RESET_ALL

output_path = os.path.join("data", "output")
output_file = "output.txt"
os.makedirs(output_path, exist_ok=True)

# driver = webdriver.Edge()
driver = webdriver.Chrome()

try:
    driver.get("https://www.cracked.io")

    while True:
        # Find the div element with id "latestthreads_table"
        latest_threads_div = driver.find_element(
            By.CLASS_NAME, "latestthreads_table")

        # Find all the span elements with class "post_link" inside the div
        post_links = latest_threads_div.find_elements(
            By.CLASS_NAME, "post_link")

        with open(os.path.join(output_path, output_file), "a", encoding="utf-8") as f:
            for post_link in post_links:
                # Find the corresponding anchor element inside the span
                post_link_a = post_link.find_element(By.TAG_NAME, "a")
                text = post_link_a.text  # Extract the text
                href = post_link_a.get_attribute(
                    "href")  # Extract the href attribute
                print(f"{Fore.YELLOW}Text: {text}, Href: {href}{Style.RESET_ALL}")
                f.write(f"Text: {text}, Href: {href}\n")

        # Click the "More" button repeatedly until it's not found
        more_button = driver.find_element(By.CLASS_NAME, "forum-subforums")
        if more_button:
            more_button.click()
            time.sleep(2)  # Add a delay to allow new threads to load
        else:
            break  # Exit the loop if "More" button is not found

except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

finally:
    driver.quit()
