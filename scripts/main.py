from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from colorama import Fore, Style  # Added colorama for terminal text color
import pyfiglet  # Added pyfiglet for ASCII art

# Initialize colorama
Fore.YELLOW
Fore.GREEN
Fore.LIGHTBLACK_EX
Style.RESET_ALL

output_path = os.path.join("data", "output")
output_file = "output.txt"
os.makedirs(output_path, exist_ok=True)

# Prompt the user for search type
print(f"{Fore.BLUE}Choose a search type:")
print(f"{Fore.BLUE}1. Press 's' to search for a specific keyword")
print(f"{Fore.BLUE}2. Press 'u' for a universal search")
search_type = input(f"{Fore.BLUE}Enter your choice (s/u): {Style.RESET_ALL}")

# Initialize the keyword variable
keyword = None

# If the user chose specific keyword search ('s')
if search_type.lower() == 's':
    keyword = input(
        f"{Fore.BLUE}Enter the keyword to search for: {Style.RESET_ALL}")

# driver = webdriver.Edge()
driver = webdriver.Chrome()

try:
    # Generate ASCII art for "SpyderSync" in blue
    ascii_art = pyfiglet.figlet_format("SpyderSync", font="slant")
    print(f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}")

    # Print a gray-colored note
    print(f"{Fore.LIGHTBLACK_EX}(Press Ctrl+C to stop the script){Style.RESET_ALL}")

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

                # Check if keyword is None (universal search) or keyword is in the title
                if keyword is None or keyword.lower() in text.lower():
                    print(
                        f"{Fore.YELLOW}Text: {text}, Href: {href}{Style.RESET_ALL}")
                    f.write(f"Text: {text}, Href: {href}\n")

        # Click the "More" button repeatedly until it's not found
        more_button = driver.find_element(By.CLASS_NAME, "forum-subforums")
        if more_button:
            more_button.click()
            time.sleep(2)  # Add a delay to allow new threads to load
        else:
            break  # Exit the loop if "More" button is not found

except KeyboardInterrupt:
    print(f"{Fore.LIGHTBLACK_EX}(Ctrl+C pressed. Stopping the script...){Style.RESET_ALL}")

except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

finally:
    driver.quit()
