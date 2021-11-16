from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path='chromedriver')
driver.get("https://www.lazada.sg/products/loreal-paris-uv-perfect-even-complexion-sunscreen-spf50pa-30ml-i214861100-s325723972.html?spm=a2o42.seller.list.1.758953196tH2Mn&mp=1")
review_csv=[]
product_csv = []
rating_csv =[]
date_review_csv = []
titles = driver.find_element_by_class_name('pdp-mod-product-badge-title').text
print(titles)
while True:
      #Get the review details here
      WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div.item")))
      product_reviews = driver.find_elements_by_css_selector("[class='item']")

      # Get product review
      for product in product_reviews:

          review = product.find_element_by_css_selector("[class='content']").text
          if (review != "" or review.strip()):
              print(review)
              review_csv.append(review)
          else:
              print(review)
              review_csv.append("No comments/review is an image")

          # Product Purchase
          # Check if the product purchase exists

          product_purchase = product.find_element_by_css_selector("[class='skuInfo']").text
          print(product_purchase)
          product_csv.append(product_purchase)

          # Star rating
          star_ratings = product.find_elements_by_css_selector("[class='star']")
          stars = "https://laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"

          star_rate = 0
          for rating in star_ratings:
              # print(rating.get_attribute('src'))
              if (rating.get_attribute('src') == stars):
                  star_rate = star_rate + 1
          rating_csv.append(star_rate)
          print(star_rate)

          # Date of Review
          date = product.find_element_by_css_selector("[class='title right']").text
          date_review_csv.append(date)
          print(date)

      #Check for button next-pagination-item have disable attribute then jump from loop else click on the next button
      if len(driver.find_elements_by_css_selector("button.next-pagination-item.next[disabled]"))>0:
          break;
      else:
          button_next=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.next-pagination-item.next")))
          driver.execute_script("arguments[0].click();", button_next)
          print("next page")
          time.sleep(2)
driver.close()
print(review_csv)
print(product_csv)
print(rating_csv)
print(date_review_csv)