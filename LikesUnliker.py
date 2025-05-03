from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

def instagram_auto_unlike():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    loginSleep=35
    likesloadSleep=5
    likespageloadSleep=12
    
    
    try:
        # Step 1: Login to Instagram
        username = "brushmelodies"
        password = "LjjrN24%@532?/zrpLqstD*+"
        
        driver.get("https://www.instagram.com/")
        
        # Wait for login fields to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Enter login credentials
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Wait for login to complete
        print("Logging in...")
        time.sleep(loginSleep)
        
        # Step 2: Navigate to likes page
        print("Navigating to likes page...")
        driver.get("https://www.instagram.com/your_activity/interactions/likes")
        time.sleep(likesloadSleep)
        
        # Loop until no more posts to unlike
        
        TotalUnlikedcount=0
        while True:
            try:
                # Check if there are any posts to unlike
                posts_present = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1iyjqo2')]//img"))
                )
                
                # Step 3: Click on "Select" button - Updated selector based on the HTML structure
                print("Clicking on Select button...")
                
                # Try multiple selector strategies to find the Select button
                try:
                    # First approach: Using the class and text content
                    select_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'wbloks_1') and @role='button']//span[text()='Select']"))
                    )
                except:
                    try:
                        # Second approach: Using data-bloks-name attribute
                        select_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//div[@data-bloks-name='bk.components.Flexbox' and @role='button']"))
                        )
                    except:
                        try:
                            # Third approach: Find by span with the specific text color
                            select_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//span[@data-bloks-name='bk.components.Text' and contains(@style, 'color: rgb(0, 149, 246)') and text()='Select']//parent::div"))
                            )
                        except:
                            # Fourth approach: Try to find any element with "Select" text that appears to be a button
                            select_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//*[text()='Select' and (@role='button' or parent::*[@role='button'])]"))
                            )
                
                driver.execute_script("arguments[0].scrollIntoView(true);", select_button)
                time.sleep(0.2)
                driver.execute_script("arguments[0].click();", select_button)
                time.sleep(0.2)
                
                # Step 4: Select posts by clicking on the circle icons
                print("Selecting posts to unlike...")
                
                # Find the circular icons based on the mask-image URL
                circle_icons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-bloks-name='ig.components.Icon' and contains(@style, 'circle__outline')]"))
                )
                
                # If no circle icons found, try alternative selectors
                if not circle_icons:
                    try:
                        # Alternative approach: Find by class and style attributes
                        circle_icons = WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'wbloks_1') and contains(@style, 'mask-image') and contains(@style, 'circle')]"))
                        )
                    except:
                        try:
                            # Another approach: Find elements with specific dimensions that might be selection circles
                            circle_icons = WebDriverWait(driver, 10).until(
                                EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@style, 'height: 24px') and contains(@style, 'width: 24px') and contains(@style, 'mask-image')]"))
                            )
                        except:
                            print("Could not find the circle selection icons. Process failed.")
                            break
                
                # If still no posts found, break the loop
                if not circle_icons:
                    print("No more posts to unlike. Process complete.")
                    break
                
                # Select up to 25 posts
                posts_count = min(25, len(circle_icons))
                print(f"Found {posts_count} posts to select")
                
                for i in range(posts_count):
                    try:
                        # Try scrolling to ensure visibility
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", circle_icons[i])
                        time.sleep(0.06)
                        
                        # Try regular click first
                        circle_icons[i].click()
                        print(f"Clicked post {i+1}")
                    except Exception as click_error:
                        try:
                            # Fall back to JavaScript click if regular click fails
                            driver.execute_script("arguments[0].click();", circle_icons[i])
                            print(f"JS clicked post {i+1}")
                        except Exception as js_error:
                            print(f"Failed to click post {i+1}: {str(js_error)}")
                    
                    #time.sleep(0.06)  # Slightly longer delay between selections
                
                # Step 5: Click on "Unlike" button - Using the exact structure you provided
                print("Looking for Unlike button...")

                '''
                # Debug: Print page source to a file for inspection
                with open('page_source.html', 'w', encoding='utf-8') as f:
                    f.write(driver.page_source)
                print("Page source saved for debugging")
                '''
                # Try multiple approaches to find the Unlike button
                try:
                    # Target the specific div with pointer-events: auto that contains the red Unlike text
                    unlike_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Unlike' and contains(@style, 'pointer-events: auto')]"))
                    )
                    #print("Found Unlike button with pointer-events: auto")
                except:
                    try:
                        # Try finding by the specific button role and aria-label
                        unlike_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Unlike']"))
                        )
                        print("Found Unlike button by role and aria-label")
                    except:
                        try:
                            # Try to find the specific red Unlike text and navigate up to find a clickable parent
                            red_unlike_text = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, "//span[@data-bloks-name='bk.components.TextSpan' and contains(@style, 'color: rgb(237, 73, 86)') and text()='Unlike']"))
                            )
                            print("Found red Unlike text")
                            
                            # Use JavaScript to find a clickable parent
                            unlike_button = driver.execute_script("""
                                let element = arguments[0];
                                while (element && element.getAttribute) {
                                    if (element.getAttribute('role') === 'button') {
                                        return element;
                                    }
                                    element = element.parentElement;
                                }
                                return arguments[0];
                            """, red_unlike_text)
                            print("Found parent button using JavaScript")
                        except:
                            # Last resort: look for any red text
                            unlike_button = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, "//*[contains(@style, 'color: rgb(237, 73, 86)')]"))
                            )
                            print("Found element with red text (fallback)")
                
                #print("Unlike button found! Attempting to click...")
                
                # Store the button in case we need to try different approaches
                original_unlike_button = unlike_button
                
                # Try multiple click methods
                try:
                    # First try direct click
                    unlike_button.click()
                    print("Direct click on Unlike button succeeded")
                except Exception as e1:
                    print(f"Direct click failed: {str(e1)}")
                    try:
                        # Try JavaScript click
                        driver.execute_script("arguments[0].click();", unlike_button)
                        print("JavaScript click on Unlike button succeeded")
                    except Exception as e2:
                        print(f"JavaScript click failed: {str(e2)}")
                        try:
                            # Try to force pointer-events and click
                            driver.execute_script("""
                                let element = arguments[0];
                                element.style.pointerEvents = 'auto';
                                element.click();
                            """, unlike_button)
                            print("Click after modifying pointer-events succeeded")
                        except Exception as e3:
                            print(f"Modified pointer-events click failed: {str(e3)}")
                            try:
                                # Find all potential unlike buttons and try to click each one
                                potential_buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Unlike') or @aria-label='Unlike']")
                                print(f"Found {len(potential_buttons)} potential Unlike buttons. Trying each...")
                                
                                for i, btn in enumerate(potential_buttons):
                                    try:
                                        driver.execute_script("arguments[0].click();", btn)
                                        print(f"Successfully clicked potential button {i+1}")
                                        break
                                    except:
                                        print(f"Failed to click potential button {i+1}")
                            except Exception as e4:
                                print(f"All click attempts failed: {str(e4)}")
                
                time.sleep(0.7)
                
                # Step 6: Confirm unliking - Using the exact button structure
                print("Looking for confirmation Unlike button...")
                try:
                    # Using the exact HTML structure for the confirmation button
                    confirm_unlike_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_a9--') and @tabindex='0']//div[contains(text(), 'Unlike')]"))
                    )
                    #print("Found confirmation button by class and text")
                except:
                    try:
                        # Try with class selector only
                        confirm_unlike_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_a9--')]"))
                        )
                        print("Found confirmation button by class")
                    except:
                        try:
                            # Try with just button containing Unlike text
                            confirm_unlike_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Unlike')]]"))
                            )
                            print("Found confirmation button containing Unlike text")
                        except:
                            try:
                                # Try any button in a dialog
                                confirm_unlike_button = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.XPATH, "//div[contains(@role, 'dialog')]//button"))
                                )
                                print("Found button in dialog")
                            except:
                                # Last resort - any button element
                                print("Could not find specific confirmation button, trying any button")
                                try:
                                    confirm_unlike_button = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, "//button"))
                                    )
                                    print("Found generic button")
                                except:
                                    print("No confirmation button found. Continuing without confirmation.")
                                    time.sleep(30)  # Wait anyway
                                    continue
                
                #print("Confirmation button found! Attempting to click...")
                
                try:
                    # Normal click first
                    confirm_unlike_button.click()
                    print("Direct click on confirmation button succeeded")
                except:
                    try:
                        # JavaScript click as fallback
                        driver.execute_script("arguments[0].click();", confirm_unlike_button)
                        print("JavaScript click on confirmation button succeeded")
                    except Exception as e:
                        print(f"Could not click confirmation button: {str(e)}")
                
                # Step 7: Wait for posts to be unliked and new ones to load
                print(f"Waiting {likespageloadSleep} seconds for posts to be unliked and new ones to load...")
                time.sleep(likespageloadSleep)
                
                TotalUnlikedcount=TotalUnlikedcount+posts_count
                
                print(f"Successfully unliked approximately {posts_count} posts")
                
                print(f"Total count:{TotalUnlikedcount}")
                
            except Exception as e:
                print("Error in the unlike process:", str(e))
                # Take a screenshot to help with debugging
                try:
                    driver.save_screenshot(f"instagram_error_{time.time()}.png")
                    print("Screenshot saved for debugging")
                except:
                    pass
                    
                user_input = input("Would you like to retry, debug, or quit? (r/d/q): ")
                if user_input.lower() == 'd':
                    # Debug mode - dump page source and try to click elements manually defined
                    print("Debug mode activated")
                    with open('debug_page_source.html', 'w', encoding='utf-8') as f:
                        f.write(driver.page_source)
                    print("Page source saved to debug_page_source.html")
                    
                    # Try this very specific selector as a last resort
                    try:
                        print("Trying hardcoded selector...")
                        last_resort = driver.find_element(By.XPATH, "//div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Unlike']")
                        driver.execute_script("arguments[0].click();", last_resort)
                        print("Hardcoded selector clicked successfully")
                        time.sleep(2)
                        
                        # Try to click confirmation
                        try:
                            confirm = driver.find_element(By.XPATH, "//button[contains(@class, '_a9--')]")
                            confirm.click()
                            print("Clicked confirmation button")
                        except:
                            print("Could not find confirmation button in debug mode")
                        
                        time.sleep(30)
                    except Exception as debug_error:
                        print(f"Debug click failed: {str(debug_error)}")
                elif user_input.lower() != 'r':
                    break
        
        print("Auto-unlike process completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        try:
            driver.save_screenshot("final_error.png")
        except:
            pass
    
    finally:
        # Ask if user wants to close the browser
        close_browser = input("Do you want to close the browser? (y/n): ")
        if close_browser.lower() == 'y':
            driver.quit()
            print("Browser closed.")
        else:
            print("Browser kept open. Please close it manually when done.")

if __name__ == "__main__":
    instagram_auto_unlike()