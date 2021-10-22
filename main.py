from typing import TypeVar
import pandas as cute_panda
import csv
import pyautogui
width, height= pyautogui.size()
import plotly.express as graphy
with open("data.csv",newline="") as f:
 reader=csv.reader(f)
 data=list(reader)
 d=data
 d.pop(0)
 sum=0
 count=0
 marks=[]
 for i in range(len(d)):
    #  
     count=count+1
     marks.append(d[i][1])
marks.sort()     
for i in range(len(marks)):
     sum=sum+float(d[i][1])
bar=graphy.scatter(data,x=0,y=marks,color=marks,title="Marks",color_discrete_sequence=["#7eff4f","#ff644f","#5b4fff","#f9ff4f","#bc4fff"],width=width,)
       
bar.update_layout({
"font": {'color': '#fff','family':'cursive'},
'plot_bgcolor': '#fff',
'paper_bgcolor': 'black',
})
bar.show()
print(sum/count)   
