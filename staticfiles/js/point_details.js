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
                label: "1st East",
                backgroundColor: 'rgba(255, 203, 63, 0.05)',
                borderColor: 'rgba(255, 203, 63, 1)',
                data: response.first_east
            },
            {
                label: '1st West',
                backgroundColor: 'rgba(255, 178, 72, 0.05)',
                borderColor: 'rgba(255, 178, 72, 1)',
                data: response.first_west
            },
             {
                label: '2nd East',
                backgroundColor: 'rgba(191, 64, 45, 0.05)',
                borderColor: 'rgba(191, 64, 45, 1)',
                data: response.second_east
            },
             {
                label: '2nd West',
                backgroundColor: 'rgba(255, 85, 60, 0.05)',
                borderColor: 'rgba(255, 85, 60, 1)',
                data: response.second_west
            },
            {
                label: '3rd East',
                backgroundColor: 'rgba(42, 191, 39, 0.05)',
                borderColor: 'rgba(42, 191, 39, 1)',
                data: response.third_east
            },
            {
                label: '3rd West',
                backgroundColor: 'rgba(28, 127, 26, 0.05)',
                borderColor: 'rgba(28, 127, 26, 1)',
                data: response.third_west
            },
            {
                label: '4th East',
                backgroundColor: 'rgba(38, 62, 191, 0.05)',
                borderColor: 'rgba(38, 62, 191, 1)',
                data: response.fourth_east
            },
            {
                label: '4th West',
                backgroundColor: 'rgba(50, 82, 255, 0.05)',
                borderColor: 'rgba(50, 82, 255, 1)',
                data: response.fourth_west
            },
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
