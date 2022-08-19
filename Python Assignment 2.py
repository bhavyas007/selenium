#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# In[2]:


driver=webdriver.Chrome(r"Downloads\chromedriver.exe")


# In[3]:


# Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location
driver.get('https://www.naukri.com/')


# In[4]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Analyst")


# In[5]:


location= driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
location.send_keys("Banglore")


# In[6]:


search= driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[7]:


job_title=[]
job_location=[]
experience_required=[]
company_name=[]


# In[8]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags= driver.find_elements(By.XPATH,'//li [@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
experience_tags=driver.find_elements(By.XPATH,'//li  [@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[9]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'experience_required':experience_required,'company_name':company_name})
df


# In[10]:


driver.get("https://www.naukri.com/")


# In[11]:


# Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location
designation= driver.find_element(By.CLASS_NAME,'suggestor-input ')
designation.send_keys("Data Scientist")


# In[12]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input')
location.send_keys("Bangalore")


# In[14]:


search=driver.find_element(By.CLASS_NAME,'qsbSubmit')
search.click()


# In[15]:


job_title=[]
job_location=[]
comapany_name=[]


# In[16]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH,'//a [@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[17]:


len(job_title)


# In[18]:


len(job_location)


# In[19]:


len(company_name)


# In[20]:


df1=pd.DataFrame({"company_name":company_name})


# In[21]:


df2=df1.iloc[0:10]


# In[22]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location})


# In[23]:


frames=[df,df2]


# In[24]:


pd.concat(frames,axis=1,join='inner')


# In[25]:


# Q3: In this question you have to scrape data using the filters available on the webpage as shown below
driver.get("https://www.naukri.com/")


# In[26]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys("Data Scientist")

select= driver.find_element(By.CLASS_NAME,"qsbSubmit")
select.click()


# In[27]:


location_filter=driver.find_elements(By.XPATH,'//span [@class="ellipsis fleft"]')
location_filter[8].click()

salary_filter= driver.find_elements(By.XPATH,'//span [@class="ellipsis fleft"]')
salary_filter[11].click()


# In[28]:


job_title=[]
job_location=[]
company_name=[]
experienced_required=[]
salary_given=[]


# In[29]:


title_tags=driver.find_elements(By.XPATH,'//a [@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'// li [@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
name_tags=driver.find_elements(By.XPATH,'// a[@class="subTitle ellipsis fleft"]')
for i in name_tags[0:10]:
    name=i.text
    company_name.append(name)
    
experienced_tags= driver.find_elements(By.XPATH,'// li [@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experienced_tags[0:10]:
    experience=i.text
    experienced_required.append(experience)
    
salary_tags=driver.find_elements(By.XPATH,'// li [@class="fleft grey-text br2 placeHolderLi salary"]')
for i in salary_tags[0:10]:
    salary=i.text
    salary_given.append(i)
    


# In[30]:


len(job_title)


# In[31]:


len(job_location)


# In[32]:


len(company_name)


# In[33]:


len(experience_required)


# In[34]:


len(salary_given)


# In[35]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name,'experienced_required': experienced_required,'salary':salary_given})


# In[36]:


df


# In[37]:


# Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
driver.get("https://www.flipkart.com/")


# In[38]:


products=driver.find_element(By.CLASS_NAME,"_3704LK")
products.send_keys("sunglasses")

select= driver.find_element(By.CLASS_NAME,"L0Z3Pu")
select.click()


# In[39]:


Brand=[]
Product_description=[]
Price=[]
offer=[]


# In[40]:


start=0
end=3
for page in range (start,end):
    Brand_tags=driver.find_elements(By.XPATH,'// div [@class="_2WkVRV"]')
    for i in Brand_tags[0:100]:
        brand_value=i.text
        Brand.append(brand_value)
        
    product_tags= driver.find_elements(By.XPATH,'// a[@class="IRpwTa"]')
    for i in product_tags[0:100]:
        product=i.text
        Product_description.append(product)
        
    price_tags= driver.find_elements(By.XPATH,'// div [@class="_30jeq3"]')
    for i in price_tags[0:100]:
        price_value=i.text
        Price.append(price_value)
        
    offer_tags=driver.find_elements(By.XPATH,'// div [@class="_3Ay6Sb"]')
    for i in offer_tags[0:100]:
        offer_value= i.text
        offer.append(offer_value)   
        
    next_button =driver.find_element(By.XPATH,'//a [@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[41]:


len(Brand)


# In[42]:


len(Product_description)


# In[43]:


len(Price)


# In[44]:


len(offer)


# In[45]:


df=pd.DataFrame({"Brand":Brand,"Price":Price,"Offer":offer})


# In[46]:


df


# In[47]:


df.iloc[0:100]


# In[48]:


df1=pd.DataFrame({"Product_description":Product_description})


# In[49]:


df1.iloc[0:100]


# In[50]:


frames=[df,df1]


# In[51]:


pd.concat(frames,axis=1,join='inner')


# In[63]:


# Scrape 100 reviews data from flipkart.com for iphone11 phone.
driver.get("https://www.flipkart.com/apple-iphone-11-black-128-gb/p/itm8244e8d955aba?pid=MOBFWQ6BKRYBP5X8&lid=LSTMOBFWQ6BKRYBP5X8HS0EXP&marketplace=FLIPKART&q=iphon")


# In[53]:


products=driver.find_element(By.CLASS_NAME,'_3704LK')
products.send_keys('Apple iphone 11 (Black,128)')

search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[64]:


Rating=[]
Review_summary=[]
Full_review=[]


# In[65]:


start=0
end=7
for page in range(start,end):
    rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags[0:100]:
        rating=i.text
        Rating.append(rating)
        
    review_tags=driver.find_elements(By.XPATH,'//p [@class="_2-N8zT"]')
    for i in review_tags[0:100]:
        review=i.text
        Review_summary.append(review)
        
    full_tags=driver.find_elements(By.XPATH,'//div [@class="t-ZTKy"]')
    for i in full_tags[0:100]:
        full=i.text
        Full_review.append(full)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[66]:


len(Rating)


# In[59]:


len(Review_summary)


# In[60]:


len(Full_review)


# In[61]:


df=pd.DataFrame({'Rating': Rating,"Review_summay":Review_summary,"Full_review":Full_review})


# In[62]:


df


# In[67]:


#Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
driver.get("https://www.flipkart.com/")


# In[68]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
product.send_keys("sneakers")

search_button= driver.find_element(By.CLASS_NAME,'L0Z3Pu')
search_button.click()


# In[69]:


Brand=[]
Product_description=[]
Price=[]
Offer=[]


# In[70]:


start=0
end=3
for page in range(start,end):
    brand_tags = driver.find_elements(By.XPATH,'//div [@class="_2WkVRV"]')
    for i in brand_tags:
        brand_name=i.text
        Brand.append(brand_name)
        
    product_tags=driver.find_elements(By.XPATH,'// a[@class="IRpwTa"]')
    for i in product_tags:
        product= i.text
        Product_description.append(product)
        
    price_tags= driver.find_elements(By.XPATH,'// div [@class="_30jeq3"]')
    for i in price_tags:
        price_value=i.text
        Price.append(price_value)
        
    offer_tags=driver.find_elements(By.XPATH,'// div [@class="_3Ay6Sb"]')
    for i in offer_tags:
        offer_value=i.text
        Offer.append(offer_value)
    
    next_button=driver.find_element(By.XPATH,'//a [@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[71]:


len(Brand)


# In[72]:


len(Product_description)


# In[73]:


len(Price)


# In[74]:


len(Offer)


# In[75]:


df1= pd.DataFrame({"Product_description":Product_description})


# In[76]:


df2=df1.iloc[0:100]


# In[77]:


df3= pd.DataFrame({"Offer":Offer})


# In[78]:


df4=df3.iloc[0:100]


# In[79]:


df=pd.DataFrame({"Brand":Brand,"Price":Price})


# In[80]:


df5=df.iloc[0:100]


# In[81]:


frame=[df5,df4,df2]


# In[82]:


pd.concat(frame,axis=1, join='inner')


# Go to the link - https://www.myntra.com/shoes
# Set second Price filter and Color filter to “Black”, as shown in the below image.
# 

# In[83]:


driver.get("https://www.myntra.com/shoes")


# In[84]:


price= driver.find_elements(By.XPATH,'// label[@class="common-customCheckbox vertical-filters-label"]')
price[8].click()


# In[85]:


Color_filter=driver.find_elements(By.XPATH,'//label [@class="common-customCheckbox"]')
Color_filter[0].click()


# In[86]:


Brand=[]
shoe_description=[]
Price=[]


# In[91]:


start=0
end=6
for page in range(start,end):
    brand_tags= driver.find_elements(By.XPATH,'//h3 [@class="product-brand"]')
    for i in brand_tags:
        brand_value=i.text
        Brand.append(brand_value)
        
    shoe_tags= driver.find_elements(By.XPATH,'//h4 [@class="product-product"]')
    for i in shoe_tags:
        shoe=i.text
        shoe_description.append(shoe)
        
    price_tags= driver.find_elements(By.XPATH,'//div [@class="product-price"]')
    for i in price_tags:
        price= i.text
        Price.append(price)
    
    next_button= driver.find_element(By.XPATH,'// li [@class="pagination-next"]')
    next_button.click()


# In[92]:


len(Brand)


# In[93]:


len(shoe_description)


# In[94]:


len(Price)


# In[95]:


df=pd.DataFrame({'Brand':Brand})
df1=df.iloc[0:100]


# In[96]:


df2=pd.DataFrame({'shoe_description':shoe_description,'Price':Price})


# In[97]:


frames=[df1,df2]


# In[98]:


pd.concat(frames,axis=1, join='inner')


# In[99]:


# Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
driver.get(" https://www.amazon.in/")


# In[100]:


product= driver.find_element(By.XPATH,"//input[@class='nav-input nav-progressive-attribute'] ")
product.send_keys("laptop")

search_button= driver.find_element(By.XPATH,'// span [@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]')
search_button.click()


# In[101]:


cpu_filter= driver.find_elements(By.XPATH,'//span [@class="a-size-base a-color-base"]')
cpu_filter[46].click()


# In[102]:


Titles=[]
Ratings=[]
Price=[]


# In[107]:


title_tags=driver.find_elements(By.XPATH,'//h2 [@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title_tags[0:10]:
    title=i.text
    Titles.append(title)
    
rating_tags=driver.find_elements(By.XPATH,'//span [@class="a-icon-alt"]')
for i in rating_tags[0:10]:
    rate_value= i.text
    Ratings.append(rate_value)
    
price_tags= driver.find_elements(By.XPATH,'// span [@class="a-price-whole"]')
for i in price_tags[0:100]:
    price= i.text
    Price.append(price)
    


# In[108]:


len(Titles)


# In[109]:


len(Ratings)


# In[110]:


len(Price)


# In[111]:


df=pd.DataFrame({'Titles':Titles})
df2=df.iloc[0:10]


# In[112]:


df1= pd.DataFrame({'Rating':Ratings})
df3=df1.iloc[0:10]


# In[113]:


df4= pd.DataFrame({'Price':Price})
df5=df4.iloc[0:10]


# In[114]:


frames=[df2,df3,df5]


# In[115]:


pd.concat(frames,axis=1, join='inner')


# In[121]:


# Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noidalocation. You have to scrape company name, No. of days ago when job was posted, Rating of the company.
driver.get("https://www.ambitionbox.com/jobs")


# In[123]:


designation= driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input")
designation.send_keys("data scientist")

search_button=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/button/span")
search_button.click()


# In[124]:


location_filter= driver.find_elements(By.XPATH,'//div [@class="radio"]')
location_filter[12].click()


# In[125]:


title=[]
experience_req=[]
salary=[]


# In[126]:


title_tags=driver.find_elements(By.XPATH,'// div [@class="company-info"]')
for i in title_tags:
    title_value=i.text
    title.append(title_value)
    
experience_tags= driver.find_elements(By.XPATH,'//p[@class="body-small-l"]')
for i in experience_tags:
    experience=i.text
    experience_req.append(experience)
    
salary_tags= driver.find_elements(By.XPATH,'//p[@class="body-small-l]"')
for i in salary_tags:
    salary_value=i.text
    salary.append(salary)

    


# In[127]:


len(title)


# In[128]:


len(experience_req)


# In[129]:


df=pd.DataFrame({"title": title})


# In[130]:


df


# In[131]:


df1= pd.DataFrame({"description":experience_req})


# In[132]:


df1


# In[133]:


driver.get("https://www.ambitionbox.com/salaries")


# In[134]:


designation = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/span/input")
designation.send_keys("data scientist")

search= driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/button/span')
search.click()


# In[135]:


lead=driver.find_elements(By.XPATH,'// div[@class="gs-title"]')
lead[1].click()


# In[136]:


company=[]
average_salary=[]
min_salary=[]
max_salary=[]
experience_req=[]


# In[147]:


company_tags= driver.find_elements(By.XPATH,'//div [@class="name"]')
for i in company_tags:
    company_name= i.text
    company.append(company_name)
    
average_tags= driver.find_elements(By.XPATH,'// div [@class="average-indicator-wrapper"]')
for i in average_tags:
    average= i.text
    average_tags.append(average)
    
min_salary_tags= driver.find_elements(By.XPATH,'// div [@class="salary-range-wrapper"]')
for i in min_salary_tags:
    min_sal=i.text
    min_salary.append(min_salary)
    
max_salary_tags=driver.find_elements(By.XPATH,'// div [@class="value body-medium"]')
for i in max_salary_tags:
    max_sal= i.text
    max_salary.append(max_sal)
    
experience_tags= driver.find_elements(By.XPATH,'// div [@class="sbold-list-header"]')
for i in experience_tags:
    experience=i.text
    experience_req.append(experience)


# In[148]:


len(company)


# In[149]:


len(average_salary)


# In[150]:


len(min_salary)

