## 项目运行

注意：首先在 `src/backend/tempHandle.ipynb` 中运行生成 `PaperTotalList.json` 文件的代码。

```bash
npm install
npm run dev
```

后端请在终端`src/backend`路径下运行安装依赖

```bash
pip install -r requirements.txt
```

你可以通过命令来启动后端，也可以直接运行main.py文件启动后端

```bash
uvicorn main:app --reload
```

