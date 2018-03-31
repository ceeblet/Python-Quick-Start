import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the data into Python
sample_data = pd.read_csv('sample_data.csv')

### sample line graph for 1 account
# Pull all OURFAVORITEPARTNER stuff
plot_data = sample_data.query("account_name == 'OURFAVORITEPARTNER'")

# plot in rows
def facet_grid_rows(data, row, color):
  p = sns.FacetGrid(data, row = row, hue = color)
  p = p.map(plt.plot, 'day', 'value')
  plt.show()


# run the facet grid
print('Preparing graph 1...')
facet_grid_rows(plot_data, row = 'subcategory_1', color = 'subcategory_2')
print('Preparing graph 2...')
facet_grid_rows(plot_data, row = 'subcategory_2', color = 'subcategory_1')
