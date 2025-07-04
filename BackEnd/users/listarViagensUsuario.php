<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data['usuario_id'])) {
        $usuario_id = $data['usuario_id'];

        $sql_viagens = "
            SELECT v.id_viagem, v.origem, v.destino, v.horario_de_partida, v.data_de_partida, v.preco,
                   uv.usuario_viagem_id, uv.assentos
            FROM viagem v
            INNER JOIN usuario_viagem uv ON v.id_viagem = uv.viagem_id
            WHERE uv.usuario_id = ?";
        
        $stmt_viagens = $conn->prepare($sql_viagens);
        $stmt_viagens->bind_param("i", $usuario_id);
        $stmt_viagens->execute();
        $result_viagens = $stmt_viagens->get_result();

        $viagens = [];

        while ($row_viagem = $result_viagens->fetch_assoc()) {
            $assentos_comprados = json_decode($row_viagem['assentos'], true);

            $viagens[] = [
                'id_viagem' => $row_viagem['id_viagem'],
                'origem' => $row_viagem['origem'],
                'destino' => $row_viagem['destino'],
                'horario_de_partida' => $row_viagem['horario_de_partida'],
                'data_de_partida' => $row_viagem['data_de_partida'],
                'preco' => $row_viagem['preco'],
                'usuario_viagem_id' => $row_viagem['usuario_viagem_id'],
                'assentos' => $assentos_comprados
            ];
        }

        header('Content-Type: application/json');
        echo json_encode(['viagens' => $viagens]);

        $stmt_viagens->close();
    } else {
        http_response_code(400);
        echo json_encode([
            "status" => 400,
            "mensagem" => "ID do usuário não enviado"
        ]);
    }
}

$conn->close();
?>
