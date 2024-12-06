<script setup>
import { Graph, Tooltip } from "@antv/g6";
import { useBaseSettingStore, usePaperListStore } from "../store/PaperList.js";
import axios from "axios";
import { onMounted, watch } from "vue";
//  数据
const BaseSettingStore = useBaseSettingStore();
const PaperListStore = usePaperListStore();
let KnowledgeBox = null;

// 监听 Domain 变化
watch(
  () => PaperListStore.Domain,
  (newVal, oldVal) => {
    if (newVal !== oldVal) console.log(newVal, oldVal);
    initGraph(newVal);
  }
);
// 适当缩小节点大小
const scaleNodeSize = (count) => {
  // 设置节点大小的公式，调整范围为10到50
  const minSize = 20;
  const maxSize = 70;
  const minCount = 100; // count 的最小可能值
  const maxCount = 10000; // count 的最大可能值
  return (
    minSize + ((count - minCount) / (maxCount - minCount)) * (maxSize - minSize)
  );
};

// 生成知识图谱
const initGraph = (Domain) => {
  axios
    .post(BaseSettingStore.BaseURL + "/getKnowledgeGraph", { Domain: Domain })
    .then((res) => {
      const GraphData = res.data.data;
      console.log(GraphData);
      if (KnowledgeBox) {
        KnowledgeBox.destroy();
      }
      KnowledgeBox = new Graph({
        container: "KnowledgeBox",
        data: GraphData,
        node: {
          style: {
            labelText: (d) => d.id,
            size: (d) => scaleNodeSize(d.data.count), // 根据 count 调整节点大小
          },
          palette: {
            type: "group",
            field: "cluster",
          },
        },
        layout: {
          type: "force",
          linkDistance: 30,
          nodeClusterBy: "cluster",
          clusterNodeStrength: 30,
          preventOverlap: true, // 防止节点重叠
        },
        behaviors: ["zoom-canvas", "drag-canvas", "drag-node"],
        animation: false,
        plugins: [
          new Tooltip({
            offsetX: 10,
            offsetY: 10,
            itemTypes: ["node"],
            getContent: (e) => {
              const node = e.item.getModel();
              return `
              <div style="padding: 8px">
                <h4>${node.id}</h4>
                <p>数量: ${node.data.count}</p>
                <p>群组: ${node.cluster}</p>
              </div>
            `;
            },
          }),
        ],
      });
      KnowledgeBox.render();
    });
};

// 数据初始化
onMounted(() => {
  initGraph("计算机体系结构/并行与分布计算/存储系统");
});
</script>

<template>
  <div id="KnowledgeBox" class="KnowledgeBox"></div>
</template>

<style scoped lang="scss">
.KnowledgeBox {
  width: 100%;
  height: 100%;
}
</style>
