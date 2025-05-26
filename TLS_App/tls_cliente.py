import socket
import ssl

HOST = '127.0.0.1'  # Localhost
PORT = 8443  # Puerto para el cliente TLS

# Creamos un contexto TLS para actuar como cliente
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Como usamos un certificado autofirmado, debemos desactivar la verificación del certificado
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE 

# Nos conectamos al servidor TLS
with socket.create_connection((HOST, PORT)) as sock:

    # Aplicamos TLS sobre la conexion 
    with context.wrap_socket(sock, server_hostname=HOST) as tls_sock:
        print("Conexión TLS establecida")
        
        # Enviamos datos al servidor
        tls_sock.send(b"Hola desde el cliente TLS!")
        
        # Recibimos datos del servidor
        data = tls_sock.recv(1024)
        print(f"Datos recibidos del servidor: {data.decode()}")