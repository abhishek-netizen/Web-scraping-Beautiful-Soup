#step0 : Install the Requirements
# pip install requests
# pip install BeautifulSoup
# pip install html5lib
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
# Step 1 : Get the html
r = requests.get(url)
htmlContent = r.content
# Step2 : Parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup)
#print(soup.prettify)
# Step3 : HTML tree traversal
#commonly used types of objects are as below
#print(type(title)) # 1. Tag, and ouput is like : <class 'bs4.element.Tag'>
#print(type(title.string)) # 2. NavigableString, and output is like : <class 'bs4.element.NavigableString'>
#print(type(soup)) # 3. BeautifulSoup, and output is like : <class 'bs4.BeautifulSoup'>
#print(title)
#print(type(title)

# # 4. comment

#title = soup.title # get the title of the HTML page
#print(title)

#Get all the paragraph from the page
#paras = soup.find_all() # it will print all - to get the paragraph mention p inside find_all('p') function
#paras = soup.find_all('p')
#print(paras)
#Get all the anchor tags from the page
#anchors = soup.find_all('a')
#print(anchors)
#Get all the links on the page
#for link in anchors:
    #print(link.get('href'))
#print(soup.find('p'))    # # get first element in the HTML page
#print(soup.find('p')['class'])  # print classes of the first element in the HTML page  

# find all the element with the class lead
#print(soup.find_all("p", class_="lead"))    

#Get text from the tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())
    
#Get all the anchors tag from the page :
#anchors = soup.find_all('a')
#all_links = set()
#get all the links on this page
#for link in anchors:
    #if(link.get('href') != '#'):
       #linkText = "https://codewithharry.com" +link.get('href')
       #all_links.add(link)
       #print(linkText)       
       
# Comment
       
#markup = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(soup2.string)
#print(type(soup2.string))
#exit()


# -- content --#

navbarSupportedContent = soup.find(id = "navbarSupportedContent")
#print(navbarSupportedContent)
#print(navbarSupportedContent.contents)

#for elem in navbarSupportedContent.contents:
    #print(elem)
    
#for elem in navbarSupportedContent.children:
    #print(elem)
    
# Difference between contents and children is .....:
".contents = A tags children available as a list" "all elements are stores in memory"
".children = A tags children available as generator" "dont eat memory much"

#for item in navbarSupportedContent.strings: 
   # print(item) #prints all the strings

#for item in navbarSupportedContent.stripped_strings: #Gather all  strings once and print
    #print(item)

#print(navbarSupportedContent.parent) "its possible to print parents of whatever element
    
#print(navbarSupportedContent.parents) # 'parents' 'gives output as : <generator object PageElement.parents at 0x0000022299E3DCC8>


#for item in navbarSupportedContent.parents: #can be iterated
    #print(item.name)


#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

# CSS --------Selectors ------------#
    
#elem = soup.select('#loginModal') #ID
#print(elem)

#elem = soup.select('.loginModal') #class 
#print(elem)


elem = soup.select('.modal-footer') #class
print(elem)