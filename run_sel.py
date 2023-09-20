from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

try:
    driver.get("https://www.cracked.io")

    # Find the div element with id "latestthreads_table"
    latest_threads_div = driver.find_element(By.CLASS_NAME, "latestthreads_table")

    # Find all the span elements with class "post_link" inside the div
    post_links = latest_threads_div.find_elements(By.CLASS_NAME, "post_link")

    with open("results.txt", "w", encoding="utf-8") as f:  # Specify UTF-8 encoding
        for post_link in post_links:
            # Find the corresponding anchor element inside the span
            post_link_a = post_link.find_element(By.TAG_NAME, "a")
            text = post_link_a.text  # Extract the text
            href = post_link_a.get_attribute(
                "href")  # Extract the href attribute
            print(f"Text: {text}, Href: {href}")
            f.write(f"Text: {text}, Href: {href}\n")

    # Click the "More" button repeatedly until it's not found
    while True:
        more_button = driver.find_element(By.CLASS_NAME, "forum-subforums")
        if more_button:
            more_button.click()
            time.sleep(2)  # Add a delay to allow new threads to load
            post_links = latest_threads_div.find_elements(
                By.CLASS_NAME, "post_link")
            with open("results.txt", "a", encoding="utf-8") as f:  # Append to the file
                for post_link in post_links:
                    post_link_a = post_link.find_element(By.TAG_NAME, "a")
                    text = post_link_a.text
                    href = post_link_a.get_attribute("href")
                    print(f"Text: {text}, Href: {href}")
                    f.write(f"Text: {text}, Href: {href}\n")
        else:
            break  # Exit the loop if "More" button is not found

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
