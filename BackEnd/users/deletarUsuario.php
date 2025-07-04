<?php
$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Erro ao conectar ao banco de dados: " . $conn->connect_error);
}

function excluirUsuario($idUsuario) {
    global $conn;

    $sql = "DELETE FROM usuario WHERE id_usuario = ?";

    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("i", $idUsuario);

        if ($stmt->execute()) {
            $stmt->close();
            return ["status" => "success", "message" => "Usuário excluído com sucesso!"];
        } else {
            $stmt->close();
            return ["status" => "error", "message" => "Erro ao excluir o usuário: " . $stmt->error];
        }
    } else {
        return ["status" => "error", "message" => "Erro ao preparar a consulta: " . $conn->error];
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'DELETE') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data["id_usuario"])) {
        $idUsuario = $data["id_usuario"];
        $response = excluirUsuario($idUsuario);
    } else {
        $response = ["status" => "error", "message" => "ID do usuário não fornecido."];
    }

    header('Content-Type: application/json');
    echo json_encode($response);
}

$conn->close();
?>
