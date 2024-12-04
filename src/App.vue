<template>
  <div id="app">
    <el-container>
      <el-header height="5vh" style="padding: 0">
        <div class="header">针对CCF推荐会议与期刊的可视化系统</div>
      </el-header>
      <el-main style="padding: 0">
        <div class="main">
          <div class="warp1 content">
            <div class="PaperList">
              <PaperList/>
            </div>
            <div class="WordCloud">
              <WordCloud/>
            </div>
          </div>
          <div class="warp2 content">
            <div class="Knowledge">
              <Knowledge/>
            </div>
            <div class="PaperYearList">
              <YearList/>
            </div>
          </div>
          <div class="warp3 content">
            <LeftCards/>
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import PaperList from './components/PaperList.vue'
import LeftCards from './components/LeftCards.vue'
import YearList from './components/YearList.vue'
import WordCloud from './components/WordCloud.vue'
import Knowledge from './components/Knowledge.vue'
</script>
<style scoped lang="scss">
#app {
  width: 100vw;
  height: 100vh;
  overflow: hidden;

  .header {
    width: 100%;
    height: 100%;
    background: black;
    color: white;
    text-align: center;
    line-height: 5vh;
    font-size: 2.5vh;
  }

  .main {
    width: 100vw;
    height: 95vh;
    background: #e6e6e6;
    display: flex;

    .content {
      border: 0.15vw solid black;
      border-radius: 0.5vw;
      background: white;
    }

    .warp1 {
      width: 20vw;
      height: 93vh;
      margin: 1vh 0 1vh 1vh;

      .PaperList {
        width: 95%;
        height: 60%;
        margin: 2.5%;
        border: 0.15vw solid gray;
        border-radius: 0.5vw;
        overflow: hidden;
      }

      .WordCloud {
        width: 95%;
        height: 37%;
        margin: 2.5%;
        border: 0.15vw solid gray;
        border-radius: 0.5vw;
      }
    }

    .warp2 {
      width: 58vw;
      height: 93vh;
      margin: 1vh;

      .Knowledge {
        width: 98%;
        height: 60%;
        margin: 1vh 1%;
        border: 0.15vw solid gray;
        border-radius: 0.5vw;
      }

      .PaperYearList {
        width: 98%;
        height: 37%;
        margin: 1vh 1%;
        border: 0.15vw solid gray;
        border-radius: 0.5vw;
      }
    }

    .warp3 {
      width: 20vw;
      height: 93vh;
      margin: 1vh 1vh 1vh 0;
    }
  }
}
</style>
