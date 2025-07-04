<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *"); // Permite todas as origens (substitua '*' pelo domínio específico se necessário)
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");


$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data['id_viagem'], $data['origem'], $data['destino'], 
              $data['horario_de_partida'], $data['data_de_partida'], 
              $data['preco'])) {

        $id_viagem = $data['id_viagem'];
        $origem = $data['origem'];
        $destino = $data['destino'];
        $horario_de_partida = $data['horario_de_partida'];
        $data_de_partida = $data['data_de_partida'];
        $preco = $data['preco'];


        $sql = "SELECT assentos FROM viagem WHERE id_viagem = $id_viagem";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();

            $sql_update = "UPDATE viagem 
                           SET origem = '$origem', 
                               destino = '$destino', 
                               horario_de_partida = '$horario_de_partida', 
                               data_de_partida = '$data_de_partida', 
                               preco = '$preco'
                           WHERE id_viagem = $id_viagem";

            if ($conn->query($sql_update) === TRUE) {
                echo json_encode(["success" => "Viagem atualizada com sucesso!"]);
            } else {
                echo json_encode(["error" => "Erro ao atualizar a viagem: " . $stmt->error]);
            }
        } else {
            echo "Viagem não encontrada!";
        }
    } else {
        echo "Dados incompletos. Certifique-se de enviar todos os dados necessários (origem, destino, horário, data, preço, status e assentos).";
    }
}

$conn->close();
?>
