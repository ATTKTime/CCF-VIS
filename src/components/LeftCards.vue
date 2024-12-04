<template>
  <div class="box" id="box1"></div>
  <div class="box" id="box2"></div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import {Chart} from '@antv/g2'
import axios from 'axios'
import {useBaseSettingStore} from '../store/PaperList.js'
// 响应式变量
const box1_data = ref([])
const BaseSettingStore = useBaseSettingStore()
// 初始化图表1
const initChartBox1 = () => {
  const item = 'category'
  // 获取数据
  axios.post(BaseSettingStore.BaseURL + '/getGroupData', {item}).then(res => {
    box1_data.value = res.data.data
    const chart = new Chart({
      container: 'box1',
      autoFit: true,
    })

    chart.coordinate({type: 'polar'})

    chart
        .data(box1_data.value)
        .scale('x', {padding: 0.5, align: 0})
        .scale('y', {tickCount: 4, domainMax: 60})
        .axis('x', {
          grid: true,
          gridLineWidth: 1,
          tick: false,
          gridLineDash: [0, 0],
        })
        .axis('y', {
          zIndex: 1,
          title: false,
          gridConnect: 'line',
          gridLineWidth: 1,
          gridLineDash: [0, 0],
        })
        .title({
          title: '不同领域的期刊和会议数量',
          align: 'center',
        })
    chart
        .area()
        .encode('x', 'category')
        .encode('y', 'count')
        .encode('color', 'type')
        .style('fillOpacity', 0.5)
    chart
        .line()
        .encode('x', 'category')
        .encode('y', 'count')
        .encode('color', 'type')
        .style('lineWidth', 2)
    chart
        .point()
        .encode('x', 'category')
        .encode('y', 'count')
        .encode('color', 'type')
        .encode('shape', 'point')
        .encode('size', 3)
        .tooltip(null)
    chart.interaction('tooltip', {crosshairsLineDash: [4, 4]})
    chart.render()
  })
}

// 初始化图表2
const initChartBox2 = () => {
  const item = 'rank'
  // 获取数据
  axios.post(BaseSettingStore.BaseURL + '/getGroupData', {item}).then(res => {
    const data = res.data.data
    const chart = new Chart({
      container: 'box2',
      autoFit: true,
      axis: {
        x: {
          title: "等级",
          titleSpacing: 0.5,
        },
        y: {
          title: "数量",
          titleSpacing: -10,

        }
      }
    })
    chart.title({
      title: '不同等级的期刊或会议数量',
      align: 'center',
    })
    chart.interval().data(data).encode('x', item).encode('y', 'count').encode('color', 'type').transform({type: 'dodgeX'})
    chart.render()
  })
}

// 在组件挂载后执行初始化函数
onMounted(() => {
  initChartBox1()
  initChartBox2()
})
</script>

<style scoped lang="scss">
.box {
  width: 95%;
  height: 48.3%;
  margin: 2.5%;
  border: 0.15vw solid gray;
  border-radius: 0.5vw;
}
</style>