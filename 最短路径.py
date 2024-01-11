import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# ... （之前的代码）

# 从Pandas数据创建图
dfAdj = pd.DataFrame([[0, 50, 0, 40, 25, 10],
                      [50, 0, 15, 20, 0, 25],
                      [0, 15, 0, 10, 20, 0],
                      [40, 20, 10, 0, 10, 25],
                      [25, 0, 20, 10, 0 ,55],
                      [10, 25, 0, 25, 55, 0]])

G1 = nx.from_pandas_adjacency(dfAdj)

# 计算最短路径
minPath03 = nx.shortest_path(G1, source=0, target=3)
lMinPath03 = nx.shortest_path_length(G1, source=0, target=3)
print("顶点 0 到 3 的最短路径为：{}，最短路径长度为：{}".format(minPath03, lMinPath03))

minWPath03 = nx.bellman_ford_path(G1, source=0, target=3)
lMinWPath03 = nx.bellman_ford_path_length(G1, source=0, target=3)
print("顶点 0 到 3 的最短加权路径为：{}，最短加权路径长度为：{}".format(minWPath03, lMinWPath03))

# 绘制图，并为每个节点添加标号
pos = nx.spring_layout(G1)
nx.draw(G1, pos, with_labels=True)

# 添加节点标签
labels = {i: i for i in range(len(G1.nodes))}
nx.draw_networkx_labels(G1, pos, labels=labels)

# 添加边的权重信息
edge_labels = {(i, j): w['weight'] for i, j, w in G1.edges(data=True)}
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels)

plt.show()
