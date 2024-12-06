<template>
  <div class="word-cloud-container">
    <p class="title">所选领域词云图</p>
    <el-divider style="width: 96%;margin: 1vh 2%;"/>
    <el-image :src=wordCloudUrl fir="fill" class="word-cloud"></el-image>
  </div>

</template>
<script setup>
import {usePaperListStore} from "../store/PaperList.js";
import {watch, reactive, ref, onMounted} from "vue";

const paperListStore = usePaperListStore();
const wordCloudUrl = ref("");

// 监控词云图路径变化
watch(() => paperListStore.WordCloudUrl,
    () => {
      wordCloudUrl.value = "src/assets/WordCloud/" + paperListStore.WordCloudUrl + '.png';
    });
</script>
<style scoped lang="scss">
.word-cloud-container {
  width: 100%;
  height: 100%;

  .word-cloud {
    width: 96%;
    height: 86%;
    border-radius: 0.5vw;
    margin-left: 2%;
  }

  .title {
    width: 100%;
    font-size: 14px;
    margin-top: 1vh;
    font-weight: bold;
    text-align: center;
  }
}

</style>