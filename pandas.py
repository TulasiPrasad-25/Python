import numpy as np
import pandas as pd
data = {
    "name" : ["tulasi", "rohitha" , "JK", "kowshik"],
    "Age" : [20, 20, 22,23],
    "dept" : ["HR", "HR", "IT", "IT"],
    "place" : [ "ctr", "ctr","tpy", "ctr" ]
}
df = pd.DataFrame(data)
print(df)