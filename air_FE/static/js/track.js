const app = new Vue({
    el: '#app2',
    data() {
      return {
        activities: [{
          content: '已收货（对应状态）',
          timestamp: '2018-04-12 20:46（对应发生时间' +
              '\n已收货，请耐心等待（对应描述）',
          size: 'large',
          type: 'primary',
          icon: 'el-icon-more'
        }, {
          content: '机场已收货',
          timestamp: '2018-04-03 20:46',
          color: '#0bbd87'
        }, {
          content: '货物异常',
          timestamp: '2018-04-03 20:46' +
              '\n货物异常：海关扣货',
          color: '#ee0951'
        }]
      };
    },

})