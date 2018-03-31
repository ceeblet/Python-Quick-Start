import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the data into Python
sample_data = pd.read_csv('sample_data.csv')

### sample line graph for 1 series
# Pull OURFAVORITEPARTNER, subcategory_1 and subcategory_2 of ALL
single_series = sample_data.query("account_name == 'OURFAVORITEPARTNER' & subcategory_1 == 'ALL' & event_name == 'ALL'")

# simple matplotlib plot
def simple_plot(data):
  plt.plot(data['day'], data['value'], '-')
  plt.show()


# run the simple plot
simple_plot(single_series)
