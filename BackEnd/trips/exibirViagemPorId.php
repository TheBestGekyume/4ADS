<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *"); 
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    http_response_code(500);
    echo json_encode(["error" => "Falha na conexão com o banco de dados: " . $conn->connect_error]);
    exit;
}

if (!isset($_GET['id_viagem']) || empty($_GET['id_viagem'])) {
    http_response_code(400);
    echo json_encode(["error" => "Parâmetro 'id_viagem' é obrigatório."]);
    exit;
}

$id_viagem = intval($_GET['id_viagem']);

$sql = "SELECT * FROM viagem WHERE id_viagem = $id_viagem";
$result = $conn->query($sql);

if ($result && $result->num_rows > 0) {
    $viagem = $result->fetch_assoc();
    echo json_encode($viagem);
} else {
    http_response_code(404);
    echo json_encode(["error" => "Viagem não encontrada."]);
}

$conn->close();
?>
