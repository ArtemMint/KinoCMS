const app = new Vue({
    el: '#hall-type',
    data: {
        nameOfHallType: "",
        rows: [
            {
                number: 1, 
                seats_value: 0,
            }
        ],
        cinemaId: "",
    },
    methods: {
       addRow(){
           this.rows.push(
               {
                   number: this.rows.length + 1,
                   seats_value: 0
               }
           )
       },
    }
})