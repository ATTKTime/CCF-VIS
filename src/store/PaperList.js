import {defineStore} from 'pinia'

export const usePaperListStore = defineStore('paperList', {
    state: () => {
        return {
            PaperYearList: [], //共享论文数据
            WordCloudUrl: '' ,//词云图url
            Domain: '计算机体系结构/并行与分布计算/存储系统' //当前领域
        }
    },
    // persist: true,
    actions: {
        setPaperYearList(list) {
            this.PaperYearList = list //更新共享每年论文数据
        },
        setWordCloudUrl(url) {
            this.WordCloudUrl = url //更新词云图url
        },
        setDomain(domain) {
            this.Domain = domain //更新当前领域
        }
    },
})

export const useBaseSettingStore = defineStore('baseSetting', {
    state: () => {
        return {
            BaseURL: 'http://localhost:8000' //后端接口地址
        }
    },
})