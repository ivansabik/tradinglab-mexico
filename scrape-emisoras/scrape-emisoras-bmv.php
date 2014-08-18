#!/usr/bin/php -q
<?php
require 'vendor/autoload.php';
use Sunra\PhpSimple\HtmlDomParser;
use Ivansabik\DomHunter\DomHunter;
use Ivansabik\DomHunter\KeyValue;
use Camspiers\JsonPretty\JsonPretty;

# Opciones cURL
$curl = curl_init();
curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE);
# Para debug curl_setopt($curl, CURLOPT_VERBOSE, TRUE);
curl_setopt($curl, CURLOPT_HEADER, TRUE);
curl_setopt($curl, CURLOPT_POST, TRUE);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, Array('Cookie: JSESSIONID=70B54DD365D5C15F78D13171004F7C91.btmxbmv02'));
# Lista de emisoras
$emisoras = array();
$url_emisoras = 'http://www.bmv.com.mx/wb3/wb/BMV/BMV_empresa_emisoras/_rid/177/_mto/3/_url/BMVAPP/emisorasList.jsf?st=1';
$dom = HtmlDomParser::file_get_html($url_emisoras);
$html_emisoras = $dom->find('td.leftalignclass'); 
# Empieza en 5 para quitar ramo, subramo, bla bla
for($i = 5; $i < count($html_emisoras) - 1; $i += 2) {
    $clave = $html_emisoras[$i]->plaintext;
    print 'Obteniendo info inicial y logo de ' . $clave .PHP_EOL;
    $nombre = $html_emisoras[$i+1]->plaintext;
    $clave_interna = preg_match('/[0-9]{4}/', $html_emisoras[$i]->first_child()->onclick, $resregex);
    $clave_interna = $resregex[0];
    $emisoras[] = array('clave' => $clave, 'nombre' => $nombre, 'clave_interna' => $clave_interna, 'logo' => 'logos/' . $clave . '.gif');
    $url = 'http://www.bmv.com.mx/img-bmv/GRA/logosemis/' . $clave_interna . '.gif';
    $img = 'logos/' . $clave . '.gif';
    file_put_contents($img, file_get_contents($url));
}
# Información de cada emisora (historia, ramo, productos, etc.)
$url_emisora = 'http://www.bmv.com.mx/wb3/wb/BMV/BMV_empresa_emisoras/_rid/177/_mto/3/_url/BMVAPP/emisorasList.jsf';
foreach($emisoras as &$emisora) {
    print 'Obteniendo info extendida de ' . $emisora['clave'] .PHP_EOL;
    curl_setopt($curl, CURLOPT_URL, $url_emisora);
    $params_post = array(
        'emisoraLinkForm' => 'emisoraLinkForm',
	'cveEmisora' => $emisora['clave'],
	'idEmisora' => $emisora['clave_interna'],
	'emisoraLinkForm:_idcl' => 'emisoraLinkForm:table:1:_id100'
    );
    # Primero cURLeo, después con Dom Hunter busca info
    curl_setopt($curl, CURLOPT_POSTFIELDS, $params_post);
    $html = curl_exec($curl);
    $hunter = new DomHunter();
    $hunter->strHtmlObjetivo = $html;
    $presas = array();
    $presas[] = array('fecha_constitucion', new KeyValue('Fecha de constituci'));
    $presas[] = array('fecha_listado', new KeyValue('Fecha de listado'));
    $presas[] = array('sector', new KeyValue('Sector'));
    $presas[] = array('subsector', new KeyValue('Subsector'));
    $presas[] = array('ramo', new KeyValue('Ramo'));
    $presas[] = array('subramo', new KeyValue('Subramo'));
    $presas[] = array('actividad_economica', new KeyValue('Actividad econ'));
    $presas[] = array('productos_servicios', new KeyValue('Principales productos'));
    $presas[] = array('historia', new KeyValue('Historia de la empresa'));
    $hunter->arrPresas = $presas;
    $hunted = $hunter->hunt();
    $emisora = array_merge($emisora, $hunted);
}
# Escribe JSON con emisoras
$json_pretty = new JsonPretty();
$json_emisoras = $json_pretty->prettify(json_encode($emisoras));
file_put_contents('emisoras.json', $json_emisoras);
print 'Listo, exportada info a "emisoras.json" y al folder "logos"' . PHP_EOL;
