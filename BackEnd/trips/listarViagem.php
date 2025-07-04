<?php
header("Access-Control-Allow-Origin: *"); 
header("Access-Control-Allow-Methods: POST, OPTIONS, GET, PUT"); 
header("Access-Control-Allow-Headers: Content-Type, Authorization"); 

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Erro de conexão: " . $conn->connect_error);
}

$sql = "SELECT * FROM viagem ORDER BY id_viagem DESC";
$result = $conn->query($sql);

$viagens = [];

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $assentos = json_decode($row['assentos'], true); 
        
        $viagens[] = [
            'id_viagem' => $row['id_viagem'],
            'origem' => $row['origem'],
            'destino' => $row['destino'],
            'horario_de_partida' => $row['horario_de_partida'],
            'data_de_partida' => $row['data_de_partida'],
            'assentos' => $assentos,  
            'preco' => $row['preco'],
            'status' => $row['status'],
            'imgUrl' => isset($row['imgUrl']) ? $row['imgUrl'] : null 
        ];
    }
}

$conn->close();

header('Content-Type: application/json');

echo json_encode($viagens);
?>
