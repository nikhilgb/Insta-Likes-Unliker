# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 00:10:58 2025

@author: user
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

def instagram_auto_unlike():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    loginSleep=35
    likesloadSleep=5
    likespageloadSleep=12
    
    
    try:
        username = "brushmelodies"
        password = "LjjrN24%@532?/zrpLqstD*+"
        
        driver.get("https://www.instagram.com/")
        

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        print("--------------------")
        print(f"Logging in. Waiting for {loginSleep}s ")
        
        countdownsleep=loginSleep
        print("Countdown:", end=" ")
        while countdownsleep>0:
            print(countdownsleep,end=" ")
            countdownsleep=countdownsleep-1
            time.sleep(1)
        
        
        print()
        print("Navigating to likes page...")
        print("--------------------")
        driver.get("https://www.instagram.com/your_activity/interactions/likes")
        time.sleep(likesloadSleep)
        

        
        TotalUnlikedcount=0
        while True:
            try:
                
                posts_present = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1iyjqo2')]//img"))
                )
                
                print("---Select button:", end=" ")
                
                
                
                try:
                    select_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'wbloks_1') and @role='button']//span[text()='Select']"))
                        )
                    print("found,", end=" ")                
                    driver.execute_script("arguments[0].scrollIntoView(true);", select_button)
                    time.sleep(0.2)                   
                    
                except:
                    print("Waiting 5 more seconds")
                    time.sleep(5)

                    try:
                        select_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'wbloks_1') and @role='button']//span[text()='Select']"))
                            )
                        print("found,", end=" ")                
                        driver.execute_script("arguments[0].scrollIntoView(true);", select_button)
                       
                    except:
                        print("Waiting 8 more seconds")
                        time.sleep(8)
                        try:
                            select_button = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'wbloks_1') and @role='button']//span[text()='Select']"))
                                )
                            print("found,", end=" ")                
                            driver.execute_script("arguments[0].scrollIntoView(true);", select_button)
                        except:
                            print("-------ERROR-------")
                            print("Unable to find Select button")
                            break
                
                driver.execute_script("arguments[0].click();", select_button)
                print("clicked")
                
                
                circle_icons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-bloks-name='ig.components.Icon' and contains(@style, 'circle__outline')]"))
                )
                
                if not circle_icons:
                    print("No more posts to unlike. Process complete.")
                    break
               
                '''
                posts_count = min(25, len(circle_icons))
                print(f"---Found {posts_count} posts to select")
                print("Selected post:")
               
                
                for i in range(posts_count):
                    
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", circle_icons[i])
                    time.sleep(0.06)
                    try:
                        circle_icons[i].click()
                        print(f"{i+1} ", end=" ")
                        if (i+1)%10==0:
                            print()
                    except:
                        pass
                    
                '''
                
                unlikeCount = min(25, len(circle_icons))
                selectedNumPost=0
                i=0
                
                print(f"---Found {unlikeCount} posts to select")
                print("Selected post:")
                
                while selectedNumPost<unlikeCount:
                    
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", circle_icons[i])
                    time.sleep(0.06)
                    try:
                        circle_icons[i].click()
                        print(f"{selectedNumPost+1} ", end=" ")
                        if (i+1)%10==0:
                            print()
                        selectedNumPost=selectedNumPost+1
                    except:
                        pass
                    i=i+1
                    
                     
                    
                    
                    
                print("")    
                print("---Unlike button:", end=" ")

                
                unlike_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Unlike' and contains(@style, 'pointer-events: auto')]"))
                    )
                
                
                original_unlike_button = unlike_button
                print("Found,", end=" ")
           
                
                unlike_button.click()
                print("Clicked")
                
                time.sleep(0.7)
                print("---Confirm Unlike button:", end=" ")
                                
                confirm_unlike_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_a9--') and @tabindex='0']//div[contains(text(), 'Unlike')]"))
                    )
                print("Found,", end=" ")
                    
                confirm_unlike_button.click()
                print("Clicked")
                
                
                
                print(f"{likespageloadSleep}s wait to unlike posts and load new ones")
                
                
                #time.sleep(likespageloadSleep)
                countdownsleeptoloadnew=likespageloadSleep
                print("Countdown:", end=" ")
                while countdownsleeptoloadnew>0:
                    print(countdownsleeptoloadnew,end=" ")
                    countdownsleeptoloadnew=countdownsleeptoloadnew-1
                    time.sleep(1)
                                
                print()
                
                TotalUnlikedcount=TotalUnlikedcount+selectedNumPost
                print("--------------------")
                print(f"Successfully unliked approximately {selectedNumPost} posts")
                
                print(f"TOTAL COUNT:{TotalUnlikedcount}")
                print("--------------------")
                print(" ")
            except Exception as e:
                print("Error in the unlike process:", str(e))
               
                try:
                    driver.save_screenshot(f"instagram_error_{time.time()}.png")
                    print("Screenshot saved for debugging")
                except:
                    pass
                    
                user_input = input("Would you like to retry, debug, or quit? (r/d/q): ")
                if user_input.lower() == 'd':
                    
                    print("Debug mode activated")
                    with open('debug_page_source.html', 'w', encoding='utf-8') as f:
                        f.write(driver.page_source)
                    print("Page source saved to debug_page_source.html")
                    
              
                    try:
                        print("Trying hardcoded selector...")
                        last_resort = driver.find_element(By.XPATH, "//div[@data-bloks-name='bk.components.Flexbox' and @role='button' and @aria-label='Unlike']")
                        driver.execute_script("arguments[0].click();", last_resort)
                        print("Hardcoded selector clicked successfully")
                        time.sleep(2)
                        
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



