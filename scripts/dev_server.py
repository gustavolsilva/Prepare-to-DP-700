#!/usr/bin/env python3
"""
Servidor HTTP Local com Desativação Estrita de Cache (No-Cache)
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Permite iterar sobre HTMLs, CSS e scripts sem bloqueios de cache do navegador.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def run(port=8000):
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(workspace_root)
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"🚀 Servidor DP-700 ativo em http://localhost:{port}/ (Raiz: {workspace_root})")
    print(f"👉 Pressione Ctrl+C para encerrar.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado com sucesso.")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run(port)

