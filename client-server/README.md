# 📌 Projeto Servidor & Cliente HTTPS

Este projeto explora a implementação de um servidor e cliente HTTPS em Python, abordando conceitos de segurança como SSL/TLS, criptografia, autenticação e integridade dos dados.

## 🔍 Para maior imersão
Recomenda-se acessar a pesquisa através do próprio servidor HTTPS que você irá executar. Isso permitirá uma experiência prática e interativa ao visualizar os conceitos diretamente via HTTPS.

## 📜 Como visualizar a pesquisa?
1. Inicie o servidor HTTPS (passo a passo abaixo).
2. Acesse pelo navegador:
   ```
   https://localhost:8443/
   ```
3. Navegue pelo site usando os links disponíveis para aprender sobre os protocolos e testar a segurança do HTTPS.

## 🚀 Configuração do Ambiente

### 🔧 Requisitos:
- Python 3.10+
- OpenSSL (para gerar certificados)
- Navegador atualizado (Chrome, Firefox, Edge, etc.)

### 📡 Executando o Servidor HTTPS
Para iniciar o servidor, execute:
```bash
python server.py
```
Após a execução, o servidor estará disponível em:
``` 
https://localhost:8443/
```

🔹 **Possível aviso no navegador:** Como o certificado é autoassinado, o navegador pode exibir um alerta de "Conexão não segura". Você pode avançar manualmente para visualizar o site.

### 💻 Executando os Clientes
Dois clientes foram desenvolvidos para testar a comunicação HTTPS:

#### ✅ Cliente 1: `client.py` (confia no servidor)
Este cliente carrega explicitamente o certificado do servidor (`server.crt`), garantindo que a conexão seja autenticada corretamente.

Para executá-lo, rode:
```bash
python client.py
```

#### ❌ Cliente 2: `client_without_server_certification.py` (não confia no servidor)
Esse cliente **NÃO** carrega o certificado do servidor, o que resultará em um erro de verificação de certificado.

Para testar:
```bash
python client_without_server_certification.py
```
Esse teste demonstrará como o cliente rejeita conexões não confiáveis, retornando um erro de verificação:
```less
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] self-signed certificate (_ssl.c:997)
```

### 📝 Estrutura do Projeto
```bash
.
├── server.py                        # Servidor HTTPS em Python
├── client.py                         # Cliente que confia no servidor
├── client_without_server_certification.py  # Cliente que NÃO confia no servidor
├── server.crt                        # Certificado do servidor (autoassinado)
├── server.key                        # Chave privada do servidor
├── index.html                        # Página inicial (recomenda-se acessar pelo servidor HTTPS)
├── ssl-tls-https.html                # Página sobre SSL/TLS/HTTPS
├── analise.html                      # Página de análise dos testes práticos
├── style.css                         # Estilos visuais do site
└── README.md                         # Este arquivo 📖
```

## 🔚 Conclusão
Este projeto demonstra:

- A importância do HTTPS na segurança da comunicação online.
- Como um cliente verifica a autenticidade de um servidor antes de se conectar.
- O impacto da falta de verificação de certificado (teste com `client_without_server_certification.py`).
- A diferença entre conexões seguras e não seguras, explorando os erros de verificação SSL/TLS.

💡 **Dica final:** Para realmente entender a teoria na prática, visualize os conteúdos do projeto através do próprio servidor HTTPS e veja os testes executando os clientes! 🚀

