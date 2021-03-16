


#SPACE:)


import tkinter 
from bs4 import BeautifulSoup
import requests
import re
from tkinter import messagebox
res = []


#Functions
def search():
    global mobiles
    try:
        minimum = int(entry_start.get())
        maximum = int(entry_end.get())
    except:
        messagebox.showinfo(title="WARNING",message="Please insert all data(must be integer)")
	
    
    for i in range(len(list_price)):
	    if minimum<=list_price[i]<=maximum:
		    res.append(list_mobile[i])
    messagebox.showinfo(title="Your Results",message=f'{res}')
    res.clear()		
                    
   

            



    



# data dictionary
mobiles = {
    "iPhone SE 2020" : 399,
    "iPhone Xr " : 499,
    "iPhone 11" : 599,
    "iPhone 12 mini" : 699,
    "iPhone 12" : 799,
    "iPhone 12 Pro" : 899,
    "iPhone 12 Pro Max" : 999,
    "iPhone 11 Pro " : 699,
    "iPhone 11 Pro Max" : 799
}

#Counter
counter = -1
    
    
webpage = requests.get('https://www.mobile57.com/us/phones/samsung/')
print("connected to the website!")

soup = BeautifulSoup(webpage.text,"html.parser")
#Name
Name = soup.find_all(attrs={"class":"product-link"})
result_name = re.findall(r'(Samsung .*?)<',str(Name))

#Price
price = soup.find_all(attrs={"class":"price-num1"})
result_price = re.findall(r'\$(\s.+?)<',str(price))



#Adding datas to dictionary
for i in range(59):
    counter += 1
    mobiles[result_name[counter]] = int(result_price[counter].replace(",",""))

list_mobile = list(mobiles.keys())
print(list_mobile)

list_price = list(mobiles.values())
print(list_price) 



root = tkinter.Tk()
root.title("Your phones price")


#GUI


label_start = tkinter.Label(root,width =5,text = "Min")
label_start.grid(row=0,column=0)

label_end = tkinter.Label(root,width=5,text="Max")
label_end.grid(row=1,column=0)

label_result = tkinter.Label(root,width=50)
label_result.grid(row=2,column=1)



entry_start = tkinter.Entry(root,width = 50)
entry_start.grid(row =0,column=1)

entry_end = tkinter.Entry(root,width = 50)
entry_end.grid(row=1,column=1)



button_search = tkinter.Button(root,text = "Search",bg="green",width = 50,command=search)
button_search.grid(row=2,column=0)












root.mainloop()

