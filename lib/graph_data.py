from process_data import dataset
import matplotlib

# Simple graph bar

# ds stands for 'dataset'

# Get the real community names

simple_graph_bar_ds = dataset[:10]

simple_bar_graph = simple_graph_bar_ds.plot.bar(x='originCommunity', y='bookCount', rot=0)
