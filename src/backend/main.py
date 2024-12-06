import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import handle
#
app = FastAPI()
# 允许跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源访问，可以修改为特定域名 ['http://example.com']
    allow_credentials=True,  # 允许跨域发送cookies
    allow_methods=["*"],  # 允许所有的HTTP方法（GET, POST等）
    allow_headers=["*"],  # 允许所有的HTTP头部信息
)


# 读取全部数据
@app.get("/data")
async def data():
    return {"data": handle.ccf_data.to_dict(orient="records")}


# 根据category分组统计不同期刊数量
@app.post("/getGroupData")
async def getGroupData(request: Request):  # 可以是
    # 从前端接收一个item变量，该变量即为分组的依据
    requestData = await request.json()
    item = requestData.get("item")
    if item == "category":
        group_data = handle.ccf_data.groupby([item, 'type']).size().reset_index(name="count").to_dict(orient="records")
    else:
        group_data = handle.ccf_data.groupby([item, 'type','category']).size().reset_index(name="count").to_dict(orient="records")
    return {"data": group_data}



@app.get("/getPapersInfoList")
async def getPapersInfoList():
    return {"data": handle.PaperInfoList.to_dict(orient="records")}


@app.post("/getPapersByCategory")
async def GetPapersByCategory(request: Request):
    requestData = await request.json()
    paperName = requestData.get("paperName")
    papersList = []
    # 找到该论文在不同领域的论文列表，并将其转化为列表
    TempList = handle.PaperTotalList[handle.PaperTotalList['paperName'] == paperName]['data'].tolist()
    for item in TempList:  # 遍历不同领域的论文列表，变成前端需要的格式
        if len(item['venues']) > 0:  # 若该领域有论文，则将其添加到papersList中
            for paper in item['venues'][0]['papers']:  # 遍历该领域的论文列表
                papersList.append(
                    {"Year": item['year'], "PaperName": paper.get('PaperName'), "Count": item['venues'][0]['count']})
    return {"data": papersList}


@app.post("/getKnowledgeGraph")
async def getKnowledgeGraph(request: Request):
    requestData = await request.json()
    Domain = requestData.get("Domain")
    return {"data": handle.filter_nodes_by_domain(Domain)}


def run():
    uvicorn.run("main:app", host="localhost", port=1314, reload=True)


if __name__ == '__main__':
    run()
