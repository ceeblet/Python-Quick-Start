import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the data into Python
sample_data = pd.read_csv('sample_data.csv')

### sample line graph for 1 account
# Pull all OURFAVORITEPARTNER stuff
plot_data = sample_data.query("account_name == 'OURFAVORITEPARTNER'")

# facet grid plot
def facet_grid(data):
  p = sns.FacetGrid(data, row = 'subcategory_1', col = 'subcategory_2')
  p = p.map(plt.plot, 'day', 'value')
  plt.show()


# run the facet grid
facet_grid(plot_data)
