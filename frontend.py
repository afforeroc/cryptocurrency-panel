# Import everything from tkinter
from tkinter import *
import csv, random, time
import urllib.request, json
window = Tk()
window.geometry("680x200")

# HEADER labels
header1=Label(window, text="ACT")
header1.grid(row=0, column=0)

header2=Label(window, text="SYM")
header2.grid(row=0, column=1)

header3=Label(window, text="INPUT")
header3.grid(row=0, column=2)

header4=Label(window, text="BID")
header4.grid(row=0, column=3)

header5=Label(window, text="ASK")
header5.grid(row=0, column=4)

header6=Label(window, text="VOL")
header6.grid(row=0, column=5)

header7=Label(window, text="MODE")
header7.grid(row=0, column=6)

# ACT buttons
b1=Button(window, text='', width=12)
b1.grid(row=1, column=0)

b2=Button(window, text='', width=12)
b2.grid(row=2, column=0)

b3=Button(window, text='', width=12)
b3.grid(row=3, column=0)

b4=Button(window, text='', width=12)
b4.grid(row=4, column=0)

b5=Button(window, text='', width=12)
b5.grid(row=5, column=0)

# SYM entries
se1=Entry(window, text=StringVar(value='eth-btc'))
se1.grid(row=1, column=1)

se2=Entry(window, text=StringVar(value='ltc-btc'))
se2.grid(row=2, column=1)

se3=Entry(window, text=StringVar(value='xrp-btc'))
se3.grid(row=3, column=1)

se4=Entry(window, text=StringVar(value='ltc-btc'))
se4.grid(row=4, column=1)

se5=Entry(window, text=StringVar(value=''))
se5.grid(row=5, column=1)

# INPUT entries
X1=IntVar()
X1.set(0)
X2=IntVar()
X2.set(0)
X3=IntVar()
X4=IntVar()
X5=IntVar()

ie1=Entry(window, textvariable=X1)
ie1.grid(row=1, column=2)

ie2=Entry(window, textvariable=X2)
ie2.grid(row=2, column=2)

ie3=Entry(window, textvariable=X3)
ie3.grid(row=3, column=2)

ie4=Entry(window, textvariable=X4)
ie4.grid(row=4, column=2)

ie5=Entry(window, textvariable=X5)
ie5.grid(row=5, column=2)

# BID labels
bid1=Label(window, textvariable='')
bid1.grid(row=1, column=3)

bid2=Label(window, textvariable='')
bid2.grid(row=2, column=3)

bid3=Label(window, textvariable='')
bid3.grid(row=3, column=3)

bid4=Label(window, textvariable='')
bid4.grid(row=4, column=3)

bid5=Label(window, textvariable='')
bid5.grid(row=5, column=3)

# ASK labels
ask1=Label(window, textvariable='')
ask1.grid(row=1, column=4)

ask2=Label(window, textvariable='')
ask2.grid(row=2, column=4)

ask3=Label(window, textvariable='')
ask3.grid(row=3, column=4)

ask4=Label(window, textvariable='')
ask4.grid(row=4, column=4)

ask5=Label(window, textvariable='')
ask5.grid(row=5, column=4)

# VOL labels
vol1=Label(window, textvariable='')
vol1.grid(row=1, column=5)

vol2=Label(window, textvariable='')
vol2.grid(row=2, column=5)

vol3=Label(window, textvariable='')
vol3.grid(row=3, column=5)

vol4=Label(window, textvariable='')
vol4.grid(row=4, column=5)

vol5=Label(window, textvariable='')
vol5.grid(row=5, column=5)

# Radio Buttons
def sel():
   selection = "You selected the option " + str(rVal.get())
   label.config(text = selection)

rVal = IntVar()
R1 = Radiobutton(window, text="Random Gen", variable=rVal, value=1, command=sel)
R1.grid(row=1, column=6)

R2 = Radiobutton(window, text="Manual Input", variable=rVal, value=2, command=sel)
R2.grid(row=2, column=6)

def dictValuesToList(dictA):
    values = []
    for k in dictA:
        values.append(dictA[k])
    return values

def extractFromJSON(urlInput):
    with urllib.request.urlopen(urlInput) as url:
        data = json.loads(url.read().decode())
    return data

def updateFromTidex(b1, bid1, ask1, vol1, b2, bid2, ask2, vol2):
    # MODE Selector
    if rVal.get() == 1: # Random Gen
        exp1 = random.randint(5, 6)
        ie1.delete(0, END) # Delete the current value
        ie1.insert(0, exp1) # Insert new value
        exp2 = random.randint(2, 3)
        ie2.delete(0, END) # Delete the current value
        ie2.insert(0, exp2) # Insert new value
    else: # Manual Input
        try: 
            exp1 = int(X1.get())
            exp2 = int(X2.get())
        except:
            exp1 = 0
            exp2 = 0

    # Extract and process data
    data1 = extractFromJSON('https://api.tidex.com/api/3/ticker/eth_btc')
    data2 = extractFromJSON('https://api.tidex.com/api/3/ticker/ltc_btc')
    eData1 = data1['eth_btc']
    eData2 = data2['ltc_btc']
    bsvList1 = [eData1['buy'], eData1['sell'], eData1['vol'] ]
    bsvList2 = [eData2['buy'], eData2['sell'], eData2['vol'] ]
   
    # Update Row 1
    factor1 = pow(10, exp1)
    delta1 = (bsvList1[1] - bsvList1[0])*factor1
    if delta1 <= bsvList1[2]:
        b1.config(text='YES', bg="green")
        b1.update()
    else: 
        b1.config(text='NO', bg="red")
        b1.update()

    bid1.config(text=bsvList1[0])
    bid1.update()
    ask1.config(text=bsvList1[1])
    ask1.update()
    vol1.config(text=round(bsvList1[2], 5))
    vol1.update()

    # Row 2
    factor2 = pow(10, exp2)
    delta2 = (bsvList1[1] - bsvList1[0])*factor2
    if delta2 <= bsvList2[2]:
        b2.config(text='YES', bg="green")
        b2.update()
    else: 
        b2.config(text='NO', bg="red")
        b2.update()
    
    bid2.config(text=bsvList2[0])
    bid2.update()
    ask2.config(text=bsvList2[1])
    ask2.update()
    vol2.config(text=round(bsvList2[2], 6))
    vol2.update()

    # Update after 10ms
    window.after(10, lambda:updateFromTidex(b1, bid1, ask1, vol1, b2, bid2, ask2, vol2))

updateFromTidex(b1, bid1, ask1, vol1, b2, bid2, ask2, vol2)
label = Label(window)

window.mainloop()