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
            labels: ["1st", "2nd", "3rd", "4th",],
            datasets: [{
                label: 'Points',
                data: [response.first, response.second, response.third, response.fourth],
                backgroundColor: [
                    'rgba(191, 63, 63, 0.8)',
                    'rgba(191, 127, 63, 0.8)',
                    'rgba(63, 63, 191, 0.8)',
                    'rgba(63, 191, 63, 0.8)',
                ],
                borderColor: [
                    'rgba(191, 63, 63, 1)',
                    'rgba(191, 127, 63, 1)',
                    'rgba(63, 63, 191, 1)',
                    'rgba(63, 191, 63, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}

