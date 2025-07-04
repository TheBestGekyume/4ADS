<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");
header("Content-Type: application/json; charset=UTF-8");

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die(json_encode(["error" => "Conexão falhou: " . $conn->connect_error]));
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (!isset($data['origem'], $data['destino'], $data['horario_de_partida'],
    $data['data_de_partida'], $data['preco'], $data['assentos'], $data['imgUrl'])) {
        echo json_encode(["error" => "Campos obrigatórios ausentes."]);
        $conn->close();
        exit;
    }

    $origem = $conn->real_escape_string($data['origem']);
    $destino = $conn->real_escape_string($data['destino']);
    $horario_de_partida = $conn->real_escape_string($data['horario_de_partida']);
    $data_de_partida = $conn->real_escape_string($data['data_de_partida']);
    $preco = $conn->real_escape_string($data['preco']);
    $imgUrl = $conn->real_escape_string($data['imgUrl']);
    $total_assentos = intval($data['assentos']); 

    $assentos = [];
    $metade = $total_assentos / 2;
    
    for ($i = 1; $i <= $total_assentos; $i++) {
        $letra = $i <= $metade ? "A" : "B";
        $numero = $i <= $metade ? $i : $i - $metade;
    
        $assento = new stdClass();
        $assento->nro_assento = $letra . $numero;
        $assento->disponivel = true;
    
        $assentos[] = $assento;
    }
    
    $assentos_json = json_encode($assentos);
    

    $stmt = $conn->prepare("INSERT INTO viagem (origem, destino, horario_de_partida, data_de_partida, preco, status, imgUrl, assentos) 
                            VALUES (?, ?, ?, ?, ?, 1, ?, ?)");
    $stmt->bind_param("ssssdss", $origem, $destino, $horario_de_partida, $data_de_partida, $preco, $imgUrl, $assentos_json);

    if ($stmt->execute()) {
        echo json_encode(["success" => "Nova viagem inserida com sucesso!"]);
    } else {
        echo json_encode(["error" => "Erro ao inserir a viagem: " . $stmt->error]);
    }

    $stmt->close();
}

$conn->close();
?>
