# networkX_E2.py
# Demo of shortest path with NetworkX
# Copyright 2021 YouCans, XUPT
# Crated：2021-05-18

import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
import networkx as nx  # 导入 NetworkX 工具包

# 问题 2：无向图的最短路问题（司守奎，数学建模算法与应用，P43，例4.3）
G2 = nx.Graph()  # 创建：空的 无向图
G2.add_weighted_edges_from([(1, 2, 2), (1, 3, 8), (1, 4, 1),
                            (2, 3, 6), (2, 5, 1),
                            (3, 4, 7), (3, 5, 5), (3, 6, 1), (3, 7, 2),
                            (4, 7, 9),
                            (5, 6, 3), (5, 8, 2), (5, 9, 9),
                            (6, 7, 4), (6, 9, 6),
                            (7, 9, 3), (7, 10, 1),
                            (8, 9, 7), (8, 11, 9),
                            (9, 10, 1), (9, 11, 2),
                            (10, 11, 4)])  # 向图中添加多条赋权边: (node1,node2,weight)
# 两个指定顶点之间的最短加权路径
minWPath_v1_v11 = nx.dijkstra_path(G2, source=1, target=11)  # 顶点 0 到 顶点 3 的最短加权路径
print("顶点 v1 到 顶点 v11 的最短加权路径: ", minWPath_v1_v11)
# 两个指定顶点之间的最短加权路径的长度
lMinWPath_v1_v11 = nx.dijkstra_path_length(G2, source=1, target=11)  # 最短加权路径长度
print("顶点 v1 到 顶点 v11 的最短加权路径长度: ", lMinWPath_v1_v11)
pos = nx.spring_layout(G2)  # 用 FR算法排列节点
nx.draw(G2, pos, with_labels=True, alpha=0.5)
labels = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
plt.show()
