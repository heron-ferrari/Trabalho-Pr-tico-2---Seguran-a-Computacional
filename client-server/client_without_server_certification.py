import socket
import ssl


def https_client(host="localhost", port=8443):
    # Cria um contexto SSL para cliente
    context = ssl.create_default_context()

    # A linha abaixo foi comentada:
    # context.load_verify_locations("server.crt")
    #
    # Sem esse certificado, o cliente não sabe se deve ou não confiar no servidor
    # (no caso de certificados autoassinados, essa configuração é necessária para validação)

    # Cria uma conexão TCP com o servidor
    with socket.create_connection((host, port)) as sock:
        # Envolve o socket com SSL/TLS
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("Conexão TLS estabelecida. Certificado do servidor:")
            # Tenta exibir o certificado que o servidor apresenta
            print(ssock.getpeercert())

            # Envia uma requisição HTTP GET
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
            ssock.sendall(request.encode("utf-8"))

            # Recebe a resposta
            response = ssock.recv(4096)
            print("Resposta do servidor:")
            print(response.decode("utf-8"))


if __name__ == "__main__":
    https_client()
