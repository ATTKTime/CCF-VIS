## 项目运行

注意：首先在 `src/backend/tempHandle.ipynb` 中运行生成 `PaperTotalList.json` 文件的代码。

```bash
npm install
npm run dev
```

后端请在终端`src/backend`路径下运行

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

