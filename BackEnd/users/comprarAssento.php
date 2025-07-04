<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");
header("Content-Type: application/json");

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
    $data = json_decode(file_get_contents("php://input"), true);

    if (isset($data['id_viagem'], $data['assentos_indisponiveis'], $data['usuario_id'])) {

        $id_viagem = $data['id_viagem'];
        $assentos_indisponiveis = $data['assentos_indisponiveis'];
        $usuario_id = $data['usuario_id'];

        $sql = "SELECT assentos FROM viagem WHERE id_viagem = $id_viagem";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $assentos = json_decode($row['assentos'], true);

            $assentos_comprados = [];

            foreach ($assentos_indisponiveis as $assento_indisponivel) {
                foreach ($assentos as &$assento) {
                    if ($assento['nro_assento'] === $assento_indisponivel['nro_assento'] && $assento['disponivel'] == true) {
                        $assento['disponivel'] = false;
                        $assentos_comprados[] = $assento['nro_assento']; 
                        break;
                    }
                }
            }

            $assentos_json = json_encode($assentos);

            $sql_update = "UPDATE viagem 
                           SET assentos = '$assentos_json' 
                           WHERE id_viagem = $id_viagem";

            if ($conn->query($sql_update) === TRUE) {
                $assentos_comprados_json = json_encode($assentos_comprados);

                $sql_insert = "INSERT INTO usuario_viagem (usuario_id, viagem_id, assentos) 
                               VALUES ($usuario_id, $id_viagem, '$assentos_comprados_json')";

                if ($conn->query($sql_insert) === TRUE) {
                    echo json_encode(["mensagem" => "Assentos comprados com sucesso e registrados!"]);
                } else {
                    echo json_encode(["erro" => "Erro ao associar usuário à viagem: " . $conn->error]);
                }
            } else {
                echo json_encode(["erro" => "Erro ao atualizar os assentos: " . $conn->error]);
            }
        } else {
            echo json_encode(["erro" => "Viagem não encontrada!"]);
        }
    } else {
        echo json_encode(["erro" => "Dados incompletos. Certifique-se de enviar 'id_viagem', 'assentos_indisponiveis' e 'usuario_id'."]);
    }
}

$conn->close();
?>
