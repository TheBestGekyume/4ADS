<?php
$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die(json_encode(["error" => "Conexão falhou: " . $conn->connect_error]));
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (!isset($data['nome'], $data['senha'], $data['email'], $data['tipo'])) {
        echo json_encode(["error" => "Campos obrigatórios ausentes."]);
        $conn->close();
        exit;
    }

    $nome = $conn->real_escape_string($data['nome']);
    $senha = $conn->real_escape_string($data['senha']);
    $email = $conn->real_escape_string($data['email']);
    $tipo = $conn->real_escape_string($data['tipo']);

    $stmt = $conn->prepare("INSERT INTO usuario (nome, senha, email, tipo) 
                            VALUES (?, ?, ?, ?)");
    $stmt->bind_param("sssi", $nome, $senha, $email, $tipo);

    if ($stmt->execute()) {
        echo json_encode(["success" => "Novo usuario inserida com sucesso!"]);
    } else {
        echo json_encode(["error" => "Erro ao inserir a usuario: " . $stmt->error]);
    }

    $stmt->close();
}

$conn->close();
?>
