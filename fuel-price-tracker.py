# # import module 
# import requests 
# import pandas as pd 
# from bs4 import BeautifulSoup 

# # link for extract html data 


# def getdata(url): 
# 	r = requests.get(url) 
# 	return r.text 


# htmldata = getdata("https://www.goodreturns.in/petrol-price.html") 
# soup = BeautifulSoup(htmldata, 'html.parser') 

# # Declare string var 
# # Declare list 
# mydatastr = '' 
# result = [] 

# # searching all tr in the html data 
# # storing as a string 
# for table in soup.find_all('tr'): 
# 	mydatastr += table.get_text() 

# # set accourding to your required 
# mydatastr = mydatastr[1:] 
# itemlist = mydatastr.split("\n\n") 

# for item in itemlist[:-5]: 
# 	result.append(item.split("\n")) 

# # Calling DataFrame constructor on list 
# df = pd.DataFrame(result[:-8]) 
# df 


# import module 
import requests 
import pandas as pd 
from bs4 import BeautifulSoup 
  
# link for extract html data 
  
  
def getdata(url): 
    r = requests.get(url) 
    return r.text
  
  
htmldata = getdata("https://www.goodreturns.in/petrol-price.html") 
soup = BeautifulSoup(htmldata, 'html.parser') 
  
# Declare string var 
# Declare list 
mydatastr = '' 
result = [] 
  
# searching all tr in the html data 
# storing as a string 
for table in soup.find_all('tr'): 
    mydatastr += table.get_text() 
  
# set accourding to your required 
mydatastr = mydatastr[1:] 
itemlist = mydatastr.split("\n\n") 
  
for item in itemlist[:-5]: 
    result.append(item.split("\n")) 
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(result[:-8]) 
print(df)