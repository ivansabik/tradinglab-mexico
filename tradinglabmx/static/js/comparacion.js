$(document).ready(function() {
    $('#grafica').highcharts('StockChart', {
        rangeSelector : {
            selected : 1,
            inputEnabled: $('#container').width() > 480
        },
        series : [{
            name : 'Cierre ajustado',
            data : data.rend_emisora_1,
            tooltip: {
                valueDecimals: 2
            }
        }]
    });
});
