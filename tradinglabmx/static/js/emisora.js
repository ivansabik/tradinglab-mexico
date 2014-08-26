$(document).ready(function() {
    $('#precios').dataTable();
    $('#grafica').highcharts('StockChart', {
        rangeSelector : {
            selected : 1,
            inputEnabled: $('#container').width() > 480
        },
        series : [{
            name : 'Cierre ajustado',
            data : data,
            tooltip: {
                valueDecimals: 2
            }
        }]
    });
});
