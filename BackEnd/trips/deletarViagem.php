<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204); 
    exit;
}

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Erro ao conectar ao banco de dados: " . $conn->connect_error);
}

function excluirViagem($idExcluir) {
    global $conn;

    $sql = "DELETE FROM viagem WHERE id_viagem = ?";

    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("i", $idExcluir);

        if ($stmt->execute()) {
            $stmt->close();
            return ["status" => "success", "message" => "Viagem excluída com sucesso!"];
        } else {
            $stmt->close();
            return ["status" => "error", "message" => "Erro ao excluir a viagem: " . $stmt->error];
        }
    } else {
        return ["status" => "error", "message" => "Erro ao preparar a consulta: " . $conn->error];
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'DELETE') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data["id_viagem"])) {
        $id_viagem = $data["id_viagem"];
        $response = excluirViagem($id_viagem);
    } else {
        $response = ["status" => "error", "message" => "ID da viagem não fornecido."];
    }

    header('Content-Type: application/json');
    echo json_encode($response);
}

$conn->close();
?>
