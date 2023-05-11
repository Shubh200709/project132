import pandas as pd
import csv
import matplotlib.pyplot as plp
import seaborn as sns

data = pd.read_csv('project131output(2).csv')
mass = data['Mass']
gravity = data['Gravity(in m/s2)']
radius = data['Radius']

mass.sort_values()
radius.sort_values()
gravity.sort_values()

plp.figure(figsize=(15,7))
plp.scatter(x=mass, y=radius)
plp.xlabel('Mass Of Planet')
plp.ylabel('Radius Of Planet')
plp.show()

plp.figure(figsize=(15,7))
plp.scatter(x=mass, y=gravity)
plp.xlabel('Mass Of Planet')
plp.ylabel('Gravity Of Planet')
plp.show()
