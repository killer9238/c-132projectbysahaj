import csv
import plotly.express as px
data = []

with open('c-132 project\Data.csv','r') as f:
  csvReader = csv.reader(f)
  for row in csvReader:
    if row != []:
      data.append(row)

star = data[1:]
Name = []
Mass = []
Radius = []
Gravity = []

for i in star:
  Name.append(i[1])
  Mass.append(float(i[3])*1.989e+30)
  Radius.append(float(i[4])*6.957e+8) 
  Gravity.append(i[5])

fig1 = px.scatter(x = Mass,y = Radius, title = 'Mass VS Radius')
fig1.show()

fig2 = px.scatter(x = Mass,y = Gravity, title = 'Mass VS Gravity')
fig2.show()