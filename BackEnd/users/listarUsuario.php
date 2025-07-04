<?php

$conn = new mysqli("localhost", "root", "", "viacaocalango");

if ($conn->connect_error) {
    die("Erro de conexão: " . $conn->connect_error);
}

$sql = "SELECT * FROM usuario";
$result = $conn->query($sql);

$usuarios = [];

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $usuarios[] = [
            'id_usuario' => $row['id_usuario'],
            'nome' => $row['nome'],
            'email' => $row['email'],
            'tipo' => $row['tipo']
        ];
    }
}

$conn->close();

header('Content-Type: application/json');

echo json_encode($usuarios);
?>
