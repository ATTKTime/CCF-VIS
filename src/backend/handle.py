import json

import pandas as pd

ccf_data = pd.read_csv("./paper_db/ccf_catalog.csv")
ccf_data.dropna(inplace=True)  # 删除空值
ccf_data['rank'] = ccf_data['rank'].str.strip()  # 去除rank两端空格


""" 知识图谱数据处理"""
# 读取知识图谱数据
with open("./data/KnowledgeGraph.json", "r", encoding="utf-8") as f:
    knowledge_graph = json.load(f)


def filter_nodes_by_domain(Domain):
    # 根据领域过滤节点
    nodes = [node for node in knowledge_graph['nodes'] if node['id'] == Domain or node['data']['cluster'] == Domain]
    edges = [edge for edge in knowledge_graph['edges'] if edge['source'] == Domain or edge['target'] == Domain]

    return {'nodes': nodes, 'edges': edges}

""" 知识图谱数据处理结束"""


""" 读取多级联选项数据"""

PaperInfoList = pd.read_json("data/PaperInfoList.json")  # 论文信息列表

# 读取论文总列表
with open('./data/PaperTotalList.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 展平嵌套结构并转换为 DataFrame
flattened_data = []

# 遍历每个文件夹（中文名称）
for folder_name, papers in data.items():
    # 遍历每个文件（即paperName和data）
    for paper in papers:
        paper_name = paper['paperName']
        paper_data = paper['data']

        # 如果需要更复杂的结构化，可以在这里修改，譬如提取某些字段
        for item in paper_data:
            # 将 paper_name 和对应的 JSON 数据合并到一起
            flattened_data.append({
                'folderName': folder_name,  # 文件夹的中文名称
                'paperName': paper_name,  # 文件名（paperName）
                'data': item  # JSON 数据的具体内容
            })

# 转换为 DataFrame
PaperTotalList = pd.DataFrame(flattened_data)  # 论文总列表

""" 读取多级联选项数据结束"""
