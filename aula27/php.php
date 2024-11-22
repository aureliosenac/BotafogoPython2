exemplo de codigo php mysql pesquisando uma tabela com campo com caracter coreano sem utilizar objeto "->".
O ChatGPT disse:

Claro! Abaixo está um exemplo simples de código PHP utilizando MySQL para pesquisar uma tabela que contém caracteres coreanos, sem usar objetos (como ->), mas utilizando uma abordagem procedural:
Estrutura do Banco de Dados

Imaginando que você tenha uma tabela chamada pessoas com a seguinte estrutura:

CREATE TABLE pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

E que o campo nome pode conter caracteres coreanos.
Código PHP

<?php
// Configurações de conexão
$host = 'localhost';
$user = 'root'; // substitua pelo seu usuário MySQL
$senha = ''; // substitua pela sua senha
$banco = 'test'; // substitua pelo nome do seu banco de dados

// Conexão com o banco de dados MySQL usando a abordagem procedural
$conexao = mysqli_connect($host, $user, $senha, $banco);

// Verificar se a conexão foi bem-sucedida
if (!$conexao) {
    die("Falha na conexão: " . mysqli_connect_error());
}

// Definir o conjunto de caracteres para lidar com caracteres coreanos (UTF-8)
mysqli_set_charset($conexao, "utf8mb4");

// Consulta para buscar pessoas com um nome específico, incluindo caracteres coreanos
$nome_pesquisa = '김철수';  // Substitua pelo nome coreano que você deseja buscar
$sql = "SELECT id, nome FROM pessoas WHERE nome LIKE '%$nome_pesquisa%'";

// Executar a consulta
$resultado = mysqli_query($conexao, $sql);

// Verificar se a consulta retornou resultados
if (mysqli_num_rows($resultado) > 0) {
    // Exibir os resultados
    while ($linha = mysqli_fetch_assoc($resultado)) {
        echo "ID: " . $linha['id'] . " - Nome: " . $linha['nome'] . "<br>";
    }
} else {
    echo "Nenhum resultado encontrado.";
}

// Fechar a conexão
mysqli_close($conexao);
?>

Explicação:

    Conexão com o Banco de Dados: Usamos mysqli_connect() para estabelecer a conexão com o banco de dados de maneira procedural. Certifique-se de substituir as variáveis $host, $user, $senha, e $banco pelos valores corretos.

    Definindo o Charset: A função mysqli_set_charset() é utilizada para garantir que a conexão utilize o conjunto de caracteres utf8mb4, que suporta caracteres coreanos.

    Consulta SQL: A variável $nome_pesquisa contém o nome coreano que você deseja procurar. A consulta SQL utiliza a cláusula LIKE para realizar a pesquisa. A % antes e depois da variável de pesquisa permite que você encontre o nome, mesmo que ele seja parte de outro nome.

    Execução da Consulta: Utilizamos mysqli_query() para executar a consulta SQL e mysqli_fetch_assoc() para recuperar e exibir os resultados.

    Fechamento da Conexão: Após a execução da consulta, a conexão é fechada com mysqli_close().

Observações:

    O utf8mb4 é recomendado ao invés de utf8 pois ele garante a compatibilidade total com caracteres como os coreanos.
    Certifique-se de que a tabela e o banco de dados estão configurados para utilizar o charset utf8mb4.

Ao enviar mensagens para o ChatGPT, você aceita nossos Termos e declara ter lido nossa Política de Privacidade.
Não compartilhe informações confidenciais. Os chats podem ser revisados e usados para treinar nossos modelos. Saiba mais


