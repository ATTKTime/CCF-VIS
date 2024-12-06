<template>
  <div class="paper-list">
    <p class="title">论文查询</p>
    <el-divider style="width: 96%;margin: 1vh 2%;"/>
    <div class="list-title">
      <!--会议期刊选择-->
      <el-cascader v-model="PaperValue" :options="options" :props="props" @change="InitPaperList"
                   :show-all-levels="true" style="width: 30%;" popper-class="cascader-popper"/>
      <!--选择年份-->
      <el-select v-model="YearValue" placeholder="请选择年份年份" style="width: 30%; margin-left:1%"
                 @change="SelectYear" clearable @clear="ClearYear">
        <el-option v-for="item in PaperYearList" :key="item.value" :label="item.label" :value="item.value"/>
      </el-select>
      <!--搜索框-->
      <el-input v-model="SearchValue" style="width: 36.5%; margin-left:1%" placeholder="输入关键字搜索" clearable
                @keyup.enter="SearchPaper" @clear="SearchPaper"/>
    </div>
    <el-divider style="width: 96%;margin: 1vh 2%;"/>
    <div class="table">
      <!--  论文列表显示    -->
      <el-table v-loading="loading" :data="PaperNameList" height="23vh" style="width: 96%;margin: 1vh" lazy stripe>
        <!--        <el-table-column prop="Year" label="Year" width="100"/>-->
        <el-table-column prop="PaperName" label="PaperName"/>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import {usePaperListStore, useBaseSettingStore} from '../store/PaperList.js'
// 响应式数据
const props = {
  expandTrigger: 'hover',
}
const options = ref([])
const PaperValue = ref(['计算机体系结构/并行与分布计算/存储系统', 'ASAP'])
const YearValue = ref("")
const PaperNameList = ref([])
const tempPaperNameList = ref([]) //用于存档总体数据，防止多次请求
const PaperYearList = ref([])
const yearSet = ref(new Set())
const SearchValue = ref("")
let loading = ref(true)
// 引入 store
const paperListStore = usePaperListStore()
const BaseSettingStore = useBaseSettingStore()
// 初始化复选框数据
const InitCascaderData = () => {
  axios.get(BaseSettingStore.BaseURL + "/getPapersInfoList").then(res => {
    options.value = res.data.data
    InitPaperList()
  })
}
// 选择不同的会议时更新列表
const InitPaperList = () => {
  axios.post(BaseSettingStore.BaseURL + "/getPapersByCategory", {
    "paperName": PaperValue.value[1]
  }).then(res => {
    tempPaperNameList.value = res.data.data  // 存档总体数据
    PaperNameList.value = tempPaperNameList.value  // 总体数据初始化为存档数据
    PaperYearList.value.length = 0  // 清空年份列表
    paperListStore.setDomain(PaperValue.value[0])
    PaperNameList.value.forEach(item => {   //根据选择的论文加载年份列表
      if (!yearSet.value.has(item.Year)) {
        PaperYearList.value.push({value: item.Year, label: item.Year, Count: item.Count})
        yearSet.value.add(item.Year)
      }
    })
    YearValue.value = "" // 更换会议清空年份选择
    yearSet.value.clear() // 清空 Set
    paperListStore.setPaperYearList(PaperYearList.value.sort((a, b) => {
      return a.value - b.value
    })) // 把年份挂在到pinia中，同时进行排序
    SetWordCloudImgUrl() // 设置词云图图片地址
    setTimeout(() => {
      loading.value = false
    }, 1000)
  })
}

// 根据年份筛选
const SelectYear = () => {
  if (SearchValue.value !== "") {  // 当选择年份，且搜索搜索框有数据，则要根据搜索框筛选
    PaperNameList.value = tempPaperNameList.value.filter(item => item.Year === YearValue.value && item.PaperName.includes(SearchValue.value))
  } else {
    PaperNameList.value = tempPaperNameList.value.filter(item => item.Year === YearValue.value) // 否则加载对应年份数据
  }
}
//清楚年份
const ClearYear = () => {
  if (SearchValue.value !== "") { // 当清除年份，但是搜索搜索框有数据，则要根据搜索框筛选
    PaperNameList.value = tempPaperNameList.value.filter(item => item.PaperName.includes(SearchValue.value))
  } else {
    // 当清除年份，且搜索框没有数据，则恢复默认列表
    PaperNameList.value = tempPaperNameList.value
  }
}

// 搜索
const SearchPaper = () => {
  if (SearchValue.value === "") {  // 当清除搜索框时，恢复默认列表
    if (YearValue.value === "") {  // 当没有选择年份时，则加载全部数据
      InitPaperList()
    } else {
      SelectYear()  // 选择年份时，加载对应年份数据
    }
  } else { //有数据则进行过滤
    PaperNameList.value = PaperNameList.value.filter(item => item.PaperName.includes(SearchValue.value))
  }
}

// 设置词云图图片地址
const SetWordCloudImgUrl = () => {
  const UrlMap = {
    "计算机体系结构/并行与分布计算/存储系统": "计算机体系结构并行与分布计算存储系统",
    "软件工程/系统软件/程序设计语言": "软件工程系统软件程序设计语言",
    "数据库/数据挖掘/内容检索": "数据库数据挖掘内容检索",
    "交叉/综合/新兴": "交叉综合新兴",
  }
  // 设置词云图图片地址 因为文件名不能包含/ 所以进行字典映射
  paperListStore.setWordCloudUrl(UrlMap[PaperValue.value[0]] || PaperValue.value[0])
}

// 挂载时执行
onMounted(() => {
  InitCascaderData()
  SetWordCloudImgUrl()
})
</script>

<style scoped lang="scss">
.paper-list {
  width: 100%;
  height: 100%;

  .title {
    width: 100%;
    font-size: 14px;
    margin-top: 1vh;
    font-weight: bold;
    text-align: center;
  }

  .list-title {
    margin: 1vh;
  }

  .cascader-popper {
    background-color: black;
  }

  :deep(.el-cascader-panel) {
    max-width: 300px; /* 设置下拉框的最大宽度 */
  }
}
</style>