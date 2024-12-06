<template>
  <div class="yearList" id="box4">
  </div>
</template>
<script setup>
import {onMounted, watch} from 'vue'
import {usePaperListStore} from '../store/PaperList.js' // 根据实际情况导入 store
import {Chart} from '@antv/g2' // 根据实际情况导入图表库

// 使用 store
const paperListStore = usePaperListStore()
const initYearList = () => {
  const data = paperListStore.PaperYearList; // 获取 store 中的数据
  const chart = new Chart({
    container: 'box4',
    autoFit: true,
  });
  chart.data(data);

  // 设置翻转轴：x轴和y轴字段互换
  chart
      .area()
      .encode('x', 'Count') // 翻转后，原来的y轴字段设置为x轴
      .encode('y', 'value') // 翻转后，原来的x轴字段设置为y轴
      .axis('x', {
        title: false,
      })
      .axis('y', {
        title: false,
      })
      .animate('enter', {type: 'pathIn', duration: 1000})
      .style('fill', 'linear-gradient(0deg, white 0%, #2389ff 100%)') // 线性渐变方向调整
      .encode('shape', 'smooth');

  chart
      .line()
      .encode('x', 'Count') // 翻转后，原来的y轴字段设置为x轴
      .encode('y', 'value') // 翻转后，原来的x轴字段设置为y轴
      .style('stroke', 'darkblue')
      .style('lineWidth', 1.5)
      .style('shape', 'smooth');

  chart.title({
    title: '所选会议或期刊每年论文数量变化',
    align: 'center',
  });

  chart.render();
};

// 初始化图表
// const initYearList = () => {
//   const data = paperListStore.PaperYearList // 获取 store 中的数据
//   const chart = new Chart({
//     container: 'box4',
//     autoFit: true,
//   })
//   chart.data(data)
//   chart
//       .area()
//       .encode('x', 'value')
//       .encode('y', 'Count')
//       .axis('x', {
//         title: false,
//       })
//       .axis('y', {
//         title: false,
//       })
//       .animate('enter', {type: 'pathIn', duration: 1000})
//       .style('fill', 'linear-gradient(-90deg, white 0%, #2389ff 100%)')
//       .encode("shape", 'smooth')
//   chart
//       .line()
//       .encode('x', "value")
//       .encode('y', 'Count')
//       .style('stroke', 'darkblue')
//       .style('lineWidth', 1.5)
//       .style('shape', 'smooth')
//   chart.title({
//     title: '所选会议或期刊每年论文数量变化',
//     align: 'center',
//   })
//   chart.render()
// }

// 监听 store 变化
watch(() => paperListStore.PaperYearList,
    () => {
      initYearList()
    },
    {deep: true}
)

// mounted 生命周期钩子
onMounted(() => {
  initYearList()
})
</script>

<style scoped lang="scss">
.yearList {
  height: 100%;
}
</style>