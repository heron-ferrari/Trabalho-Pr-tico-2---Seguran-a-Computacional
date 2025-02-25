import socket  # Para criar conexões em baixo nível (TCP)
import ssl  # Para encapsular sockets com SSL/TLS


def https_client(host="localhost", port=8443):
    # Cria um contexto SSL com configurações padrão para cliente
    context = ssl.create_default_context()

    # Carrega o certificado do servidor, de modo que este cliente confie neste certificado específico
    context.load_verify_locations("server.crt")

    # Cria uma conexão TCP com o servidor no host e porta definidos
    with socket.create_connection((host, port)) as sock:
        # 'wrap_socket' envolve esse socket com a camada SSL/TLS
        # 'server_hostname' deve corresponder ao CN (Common Name) ou SubjectAltName do certificado do servidor
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("Conexão TLS estabelecida. Certificado do servidor:")
            # Exibe detalhes do certificado que o servidor apresentou
            print(ssock.getpeercert())

            # Monta uma requisição HTTP GET simples
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
            # Envia a requisição ao servidor
            ssock.sendall(request.encode("utf-8"))

            # Recebe a resposta
            response = ssock.recv(4096)
            print("Resposta do servidor:")
            print(response.decode("utf-8"))


if __name__ == "__main__":
    https_client()
