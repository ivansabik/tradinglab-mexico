$(document).ready( function () {
    $('#resultados_simula').dataTable( {
        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/static/swf/copy_csv_xls_pdf.swf"
        }
    } );
} );
