import socket
import ssl #Librería para manejar TLS/SSL

# Configuración del servidor TLS

HOST = '127.0.0.1'  # Localhost
PORT = 8443  # Puerto para el servidor TLS

# Creamos un contexto TLS para actuar como servidor
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

#Cargamos el certificado y la clave privada
context.load_cert_chain(certfile='TLS_App/certs/cert.pem', keyfile='TLS_App/certs/key.pem')

# Creamos un socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    # Enlazamos el socket al host y puerto
    sock.bind((HOST, PORT))
    
    # Ponemos el socket en modo de escucha
    sock.listen(1)
    print(f"Servidor TLS escuchando en {HOST}:{PORT}")

    # Envolvemos el socket en un contexto TLS
    with context.wrap_socket(sock, server_side=True) as tls_conn:

        conn, addr = tls_conn.accept()

        print(f"Conexión TLS establecida con {addr}")

        # Recibimos y enviamos datos a través del socket TLS
        data = conn.recv(1024)
        print(f"Datos recibidos: {data.decode()}")

        # Enviamos una respuesta al cliente
        conn.send(b"Hola desde el servidor TLS!")