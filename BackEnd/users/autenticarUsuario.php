<?php
header("Access-Control-Allow-Origin: *"); 
header("Access-Control-Allow-Methods: POST, OPTIONS, GET, PUT"); 
header("Access-Control-Allow-Headers: Content-Type, Authorization"); 

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data['email'], $data['senha'])) {
        $email = $data['email'];
        $senha = $data['senha'];

        $stmt = $conn->prepare("SELECT id_usuario, nome, tipo FROM usuario WHERE email = ? AND senha = ?");
        $stmt->bind_param("ss", $email, $senha);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $stmt->bind_result($id_usuario, $nome, $tipo);
            $stmt->fetch();

            echo json_encode([
                "status" => 200,
                "mensagem" => "Autenticação bem-sucedida",
                "id_usuario" => $id_usuario, 
                "nome" => $nome,
                "tipo" => $tipo
            ]);
        } else {
            http_response_code(404);
            echo json_encode([
                "status" => 404,
                "mensagem" => "Usuário não encontrado ou senha incorreta"
            ]);
        }
        
        $stmt->close();
    } else {
        http_response_code(400);
        echo json_encode([
            "status" => 400,
            "mensagem" => "Dados de autenticação incompletos"
        ]);
    }
}

$conn->close();
?>
