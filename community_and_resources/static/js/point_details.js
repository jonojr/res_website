fetch(window.location.origin + '/point_results/')
    .then(function (response) {
        console.log('Response recieved');
        return response.json();
    })
    .then(render_full_chart);


function render_full_chart(response) {
    console.log('Rendering')
    var data = {
        labels: response.labels,
        datasets: [
            {
                label: "First Floor",
                backgroundColor: "rgba(41, 136, 93, 0.05)",
                borderColor: "rgb(41, 136, 93)",
                data: response.first
            },
            {
                label: 'Second Floor',
                backgroundColor: "rgba(44, 92, 126,0.05)",
                borderColor: "rgb(44, 92, 126)",
                data: response.second
            },
             {
                label: 'Second Floor',
                backgroundColor: "rgba(196, 137, 60, 0.05)",
                borderColor: "rgb(196, 137, 60)",
                data: response.third
            },
             {
                label: 'Second Floor',
                backgroundColor: "rgba(196, 97, 60,0.05)",
                borderColor: "rgb(196, 97, 60)",
                data: response.fourth
            }
        ]
    };
    var options = {scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }};
    var ctx = document.getElementById("point_detail").getContext('2d');
    var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
});
}
