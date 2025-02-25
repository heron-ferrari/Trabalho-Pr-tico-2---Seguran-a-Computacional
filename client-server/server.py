import http.server  # Módulo para criar um servidor HTTP simples em Python
import ssl  # Módulo que fornece recursos de SSL/TLS
from http.server import SimpleHTTPRequestHandler


def run_secure_server(host="localhost", port=8443):
    # Define o endereço do servidor (host e porta)
    server_address = (host, port)

    # Cria uma instância de servidor HTTP, associando o handler para requisições
    # SimpleHTTPRequestHandler serve arquivos do diretório atual como resposta HTTP
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Cria um contexto SSL para configurar o servidor com TLS
    # PROTOCOL_TLS_SERVER é usado para configurar o servidor de modo seguro
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    # Carrega o certificado e a chave privada do servidor
    # O certificado (server.crt) deve corresponder à chave (server.key)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    # Associa o socket do servidor ao contexto SSL, exigindo que as conexões sejam criptografadas
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor HTTPS iniciado em https://{host}:{port}")
    # Inicia o loop que mantém o servidor rodando para aceitar requisições
    httpd.serve_forever()


if __name__ == "__main__":
    run_secure_server()
