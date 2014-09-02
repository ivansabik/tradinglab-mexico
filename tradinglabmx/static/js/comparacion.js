$(document).ready(function() {
    $('#grafica').highcharts('StockChart', {
        rangeSelector : {
            selected : 1,
            inputEnabled: $('#container').width() > 480
        },
        series : [{
            name : emisora_1,
            data : data.rend_emisora_1,
            tooltip: {
                valueDecimals: 4
            }
        },
        {
            name : emisora_2,
            data : data.rend_emisora_2,
            tooltip: {
                valueDecimals: 4
            }
        }]
    });
    
    $('#grafica2').highcharts({
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: 'Rendimientos vs Riesgo'
        },
        xAxis: {
            title: {
                text: 'Rendimiento esperado'
            }
        },
        yAxis: {
            title: {
                text: 'Riesgo'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 100,
            y: 100,
            floating: true,
            borderWidth: 1
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 8
                },
                tooltip: {
                    valueDecimals: 4
                }
            }
        },
        series: [{
            name: emisora_1,
            data: [[data.media_emisora_1, data.std_emisora_1]]
        }, {
            name: emisora_2,
            data: [[data.media_emisora_2, data.std_emisora_2]]
        }]
    });
});
