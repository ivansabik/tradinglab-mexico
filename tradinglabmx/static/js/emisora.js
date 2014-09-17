$(document).ready(function() {
    $('#precios').dataTable( {
        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/static/swf/copy_csv_xls_pdf.swf"
        }
    } );
    $('#grafica').highcharts('StockChart', {
        rangeSelector: {
            selected: 1,
            inputEnabled: $('#container').width() > 480
        },
        yAxis: [{
            labels: {
                align: 'right',
                x: -3
            },
            title: {
                text: 'Precios'
            },
            height: '60%',
            lineWidth: 2
        }, {
            labels: {
                align: 'right',
                x: -3
            },
            title: {
                text: 'Volumen'
            },
            top: '65%',
            height: '35%',
            offset: 0,
            lineWidth: 2
        }],
        series: [{
            name: 'Cierre ajustado',
            data: data.cierre_aj,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            name: 'Promedio móvil 5 días',
            data: data.mavg5,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            name: 'Promedio móvil 10 días',
            data: data.mavg10,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            name: 'Promedio móvil 20 días',
            data: data.mavg20,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            name: 'Promedio móvil 50 días',
            data: data.mavg50,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            name: 'Promedio móvil 200 días',
            data: data.mavg200,
            tooltip: {
                valueDecimals: 2
            }
        }, {
            type: 'column',
            name: 'Volumen',
            data: data.volumen,
            yAxis: 1
        }]
    });
});
