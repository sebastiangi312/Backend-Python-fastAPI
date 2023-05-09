from mimesis import Person
import pandas as pd

nr_of_rows = 100000
nr_of_columns = 100

randomGenerator = Person()

data = [[randomGenerator.name() for i in range(nr_of_columns)] for j in range(nr_of_rows)]
df = pd.DataFrame(data)

df.to_csv("dummy.csv", index=False)