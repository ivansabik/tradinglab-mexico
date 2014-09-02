$(document).ready(function() {
    $('#precios').dataTable();
    $('#grafica').highcharts('StockChart', {
        rangeSelector : {
            selected : 1,
            inputEnabled: $('#container').width() > 480
        },
        yAxis: [
			{
				labels: {
					align: 'right',
					x: -3
				},
				title: {
					text: 'Precios'
				},
				height: '60%',
                lineWidth: 2
            },
            {
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
        series : [{
            name : 'Cierre ajustado',
            data : data.cierre_aj,
            tooltip: {
                valueDecimals: 2
            }
        },
        {
            name : 'Promedio móvil 5 días',
            data : data.mavg5,
            tooltip: {
                valueDecimals: 2
            }
        },
        {
            name : 'Promedio móvil 10 días',
            data : data.mavg10,
            tooltip: {
                valueDecimals: 2
            }
        },
        {
            name : 'Promedio móvil 15 días',
            data : data.mavg15,
            tooltip: {
                valueDecimals: 2
            }
        },
        {
            name : 'Promedio móvil 30 días',
            data : data.mavg30,
            tooltip: {
                valueDecimals: 2
            }
        },
        {
            type: 'column',
            name: 'Volumen',
            data: data.volumen,
            yAxis: 1
        }]
    });
});
