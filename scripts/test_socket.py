"""
Script de Exemplo: Teste de Conexao Socket TCP
Referencia para questoes sobre o modulo 'socket' nativo do Python.
"""
import socket

def testar_conexao(host="8.8.8.8", porta=53, timeout=3):
    print(f"Testando conexao TCP com {host}:{porta}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        resultado = sock.connect_ex((host, porta))
        sock.close()
        
        if resultado == 0:
            print(f"[SUCESSO] Porta {porta} em {host} esta ABERTA.")
        else:
            print(f"[FALHA] Porta {porta} em {host} esta FECHADA ou INACESSIVEL.")
    except Exception as e:
        print(f"[ERRO] Falha ao tentar conectar: {e}")

if __name__ == "__main__":
    testar_conexao("8.8.8.8", 53)   # DNS Google (TCP)
    testar_conexao("1.1.1.1", 80)   # Cloudflare HTTP