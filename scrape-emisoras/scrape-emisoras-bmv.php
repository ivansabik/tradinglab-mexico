#!/usr/bin/php -q
<?php
require 'vendor/autoload.php';
use Sunra\PhpSimple\HtmlDomParser;

# cURL 
$curl = curl_init();
curl_setopt($curl, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($curl, CURLOPT_VERBOSE, TRUE);
curl_setopt($curl, CURLOPT_HEADER, TRUE);
curl_setopt($curl, CURLOPT_POST, TRUE);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, Array('Cookie: JSESSIONID=70B54DD365D5C15F78D13171004F7C91.btmxbmv02'));

# Lista de emisoras
$emisoras = array();
$url_emisoras = 'http://www.bmv.com.mx/wb3/wb/BMV/BMV_empresa_emisoras/_rid/177/_mto/3/_url/BMVAPP/emisorasList.jsf?st=1';
$dom = HtmlDomParser::file_get_html($url_emisoras);
$html_emisoras = $dom->find('td.leftalignclass'); 

for($i = 5; $i < count($html_emisoras) - 1; $i += 2) {
    $clave = $html_emisoras[$i]->plaintext;
    $nombre = $html_emisoras[$i+1]->plaintext;
    $clave_interna = preg_match('/[0-9]{4}/', $html_emisoras[$i]->first_child()->onclick, $resregex);
    $clave_interna = $resregex[0];
    $emisoras[] = array('clave' => $clave, 'nombre' => $nombre, 'clave_interna' => $clave_interna);
    
    $url = 'http://www.bmv.com.mx/img-bmv/GRA/logosemis/' . $clave_interna . '.gif';
    $img = 'logos/' . $clave . '.gif';
    file_put_contents($img, file_get_contents($url));
}

print_r($emisoras) . PHP_EOL;

/*
$url_emisora = 'http://www.bmv.com.mx/wb3/wb/BMV/BMV_empresa_emisoras/_rid/177/_mto/3/_url/BMVAPP/emisorasList.jsf';
curl_setopt($curl, CURLOPT_URL, $url_emisora);
$params_post = array(
    'emisoraLinkForm' => 'emisoraLinkForm',
    'cveEmisora' => 'ACCELSA',
    'idEmisora' => '5015',
    'emisoraLinkForm:_idcl' => 'emisoraLinkForm:table:1:_id100'
);

curl_setopt($curl, CURLOPT_POSTFIELDS, $params_post);

print curl_exec($curl);
print PHP_EOL;

# Logo
# http://www.bmv.com.mx/img-bmv/GRA/logosemis/5015.gif
*/