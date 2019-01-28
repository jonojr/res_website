fetch(window.location.origin + '/point_results/')
    .then(function (response) {
        console.log('Response recieved');
        return response.json();
    })
    .then(render_full_chart);


function render_full_chart(response) {

    var ctx = document.getElementById("point_detail").getContext('2d');
    var myLineChart = new Chart(ctx).Line(data);
    var data = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                data: [65, 59, 80, 81, 56, 55, 40]
            },
            {
                fillColor: "rgba(151,187,205,0.2)",
                strokeColor: "rgba(151,187,205,1)",
                data: [28, 48, 40, 19, 86, 27, 90]
            }
        ]
    };
}
