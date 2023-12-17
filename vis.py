# pls never fsck with pandas near windows, as they will jump through (run this in collab you nerd)
import pandas as pd
from pyvis.network import Network

deffs = pd.read_csv("deffs.csv")
treefs = pd.read_csv("treefs.csv")


# Create a network object
net = Network(notebook=True, cdn_resources="in_line")

net.repulsion()

# Add nodes to the network
for row in deffs.itertuples():
  net.add_node(row[1], label=row[2], size=row[3] / 2)

# Add edges to the network
for row in treefs.itertuples():
  net.add_edge(row[1], row[2])

# Show the network
# net.save_graph("graphfs.html")
net.show("graphfs.html")
