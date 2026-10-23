"""
Script de Exemplo: Calculo de Sub-rede IPv4 com a biblioteca nativa 'ipaddress'
Referencia para provas de concursos publicos de TI.
"""
import ipaddress

def analisar_subrede(cidr_str):
    try:
        rede = ipaddress.ip_network(cidr_str, strict=False)
        print(f"=== Analise da Sub-rede {cidr_str} ===")
        print(f"Endereco de Rede:     {rede.network_address}")
        print(f"Mascara de Sub-rede:   {rede.netmask}")
        print(f"Endereco de Broadcast: {rede.broadcast_address}")
        print(f"Total de IPs (bruto):  {rede.num_addresses}")
        print(f"Hosts Uteis:          {max(0, rede.num_addresses - 2)}")
        
        hosts = list(rede.hosts())
        if hosts:
            print(f"Primeiro Host Util:   {hosts[0]}")
            print(f"Ultimo Host Util:     {hosts[-1]}")
    except ValueError as e:
        print(f"[ERRO] CIDR invalido: {e}")

if __name__ == "__main__":
    analisar_subrede("192.168.1.0/26")