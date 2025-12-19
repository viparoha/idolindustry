#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server
import socketserver

class UTF8HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # HTML 파일에 대해 UTF-8 인코딩 명시
        if self.path.endswith('.html'):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

PORT = 8000
Handler = UTF8HTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"서버 시작: http://localhost:{PORT}")
    print("종료하려면 Ctrl+C를 누르세요")
    httpd.serve_forever()


