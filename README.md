# Ponto a Ponto - Infraestrutura, Redes e Metodologias de TI

Plataforma web interativa de suporte ao estudo de redes de computadores, arquitetura de sistemas, metodologias de software e preparação para concursos públicos da área de Tecnologia da Informação.

---

## Objetivos do Projeto

1. **Infraestrutura e Redes**: Apresentação dos modelos OSI e TCP/IP, encapsulamento de quadros e pacotes, resolução de nomes DNS e tabela de portas de protocolos transportadores.
2. **Diagnóstico e Ferramentas**:
   - Mapeamento em tempo real do IP Público do cliente (provedor, geolocalização e latência de rede).
   - Calculadora de sub-redes IPv4 em notação CIDR com detalhamento bit a bit (bits de rede e host).
3. **Metodologias de TI para Concursos**:
   - Sínteses alinhadas às bancas Cebraspe, FGV, Vunesp e Cesgranrio.
   - Cobertura fundamentada do Modelo em Cascata, Scrum Guide (2020), Lean Software Development, TDD, Kanban e Extreme Programming (XP).
   - Banco de questões com gabarito e justificativa técnica.
4. **Laboratório Python**:
   - Terminal interativo executado no navegador via WebAssembly (Pyodide) para teste de scripts com as bibliotecas nativas `socket` e `ipaddress`.

---

## Modelagem UML e Arquitetura do Sistema

### 1. Diagrama de Casos de Uso

```mermaid
graph TD
    User[Usuario / Estudante]

    subgraph Ponto_a_Ponto [Plataforma Ponto a Ponto]
        UC1[Consultar IP Publico e Geolocalizacao]
        UC2[Calcular Sub-redes CIDR e Analisar Bits]
        UC3[Estudar Modelo OSI / TCP-IP]
        UC4[Simular Encapsulamento e Resolucao DNS]
        UC5[Estudar Metodologias de TI]
        UC6[Executar Scripts Python de Rede]
        UC7[Responder Simulado de Concursos]
        UC8[Enviar Dúvidas / Sugestões via Contato]
    end

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
    User --> UC8
    