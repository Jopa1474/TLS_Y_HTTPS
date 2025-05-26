import http.server
import ssl

# Definimos la dirección y el puerto del servidor HTTPS
server_address = ('localhost', 8443)

# Creamos un servidor HTTP en la dirección y puerto especificados
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Configuramos el contexto SSL para el servidor HTTPS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# Cargamos el certificado y la clave privada
context.load_cert_chain(certfile='HTTPS_App/certs/cert.pem', keyfile='HTTPS_App/certs/key.pem')
# Envolvemos el socket del servidor HTTP en el contexto TLS
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Servidor HTTPS corriendo en https://localhost:8443")
httpd.serve_forever()

