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

// 初始化图表
const initYearList = () => {
  const data = paperListStore.PaperYearList // 获取 store 中的数据
  const chart = new Chart({
    container: 'box4',
    autoFit: true,
  })
  chart.data(data)
  chart
      .area()
      .encode('x', 'value')
      .encode('y', 'Count')
      .axis('x', {
        title: false,
      })
      .axis('y', {
        title: false,
      })
      .animate('enter', {type: 'pathIn', duration: 1000})
      .style('fill', 'linear-gradient(-90deg, white 0%, #2389ff 100%)')
      .encode("shape", 'smooth')
  chart
      .line()
      .encode('x', "value")
      .encode('y', 'Count')
      .style('stroke', 'darkblue')
      .style('lineWidth', 1.5)
      .style('shape','smooth')
  chart.title({
    title: '所选会议或期刊每年论文数量变化',
    align: 'center',
  })
  chart.render()
}

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