console.log('Loading');
fetch(window.location.origin + '/total_points/')
    .then(function (response) {
        console.log('Response recieved');
        return response.json();
    })
    .then(render_simple_chart);


function render_simple_chart(response){
    console.log('Rendering');

    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["1E", "1W", "2E", "2W", "3E", "3W","4E", "4W",],
            datasets: [{
                label: 'Points',
                data: [response.FirstE, response.FirstW, response.SecondE, response.SecondW, response.ThirdE, response.ThirdW, response.FourthE, response.FourthW],
                backgroundColor: [
                    'rgba(255, 203, 63, 0.8)',
                    'rgba(255, 178, 72, 0.8)',
                    'rgba(191, 64, 45, 0.8)',
                    'rgba(255, 85, 60, 0.8)',
                    'rgba(42, 191, 39, 0.8)',
                    'rgba(28, 127, 26, 0.8)',
                    'rgba(38, 62, 191, 0.8)',
                    'rgba(50, 82, 255, 0.8)',
                ],
                borderColor: [
                    'rgba(255, 203, 63, 1)',
                    'rgba(255, 178, 72, 1)',
                    'rgba(191, 64, 45, 1)',
                    'rgba(255, 85, 60, 1)',
                    'rgba(42, 191, 39, 1)',
                    'rgba(28, 127, 26, 1)',
                    'rgba(38, 62, 191, 1)',
                    'rgba(50, 82, 255, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            legend: {
                display: true,
                position: 'bottom',
                labels: {
                    boxWidth: 0,
                },
            }
        }
    });
}

