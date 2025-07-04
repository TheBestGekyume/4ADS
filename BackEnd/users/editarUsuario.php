<?php
$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die(json_encode(["error" => "Conexão falhou: " . $conn->connect_error]));
}

if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (!isset($data['id_usuario'], $data['nome'], $data['senha'], $data['email'], $data['tipo'])) {
        echo json_encode(["error" => "Campos obrigatórios ausentes. Certifique-se de enviar 'id_usuario', 'nome', 'senha', 'email', 'tipo'."]);
        $conn->close();
        exit;
    }

    $id_usuario = (int)$data['id_usuario'];
    $nome = $conn->real_escape_string($data['nome']);
    $senha = $conn->real_escape_string($data['senha']);
    $email = $conn->real_escape_string($data['email']);
    $tipo = (int)$data['tipo'];

    $stmt = $conn->prepare("UPDATE usuario 
                            SET nome = ?, senha = ?, email = ?, tipo = ? 
                            WHERE id_usuario = ?");
    $stmt->bind_param("sssii", $nome, $senha, $email, $tipo, $id_usuario);

    if ($stmt->execute()) {
        echo json_encode(["success" => "Usuário atualizado com sucesso!"]);
    } else {
        echo json_encode(["error" => "Erro ao atualizar o usuário: " . $stmt->error]);
    }

    $stmt->close();
}

$conn->close();
?>
