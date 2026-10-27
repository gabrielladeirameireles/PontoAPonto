# Ponto a Ponto — Portal de TI, Infraestrutura e Carreira

O **Ponto a Ponto** é um portal web interativo desenvolvido para organizar conceitos fundamentais da Tecnologia da Informação, servir como guia contínuo de aprendizado e expor um portfólio prático de projetos de software e infraestrutura.

A plataforma conta com uma estrutura de leitura fluida e um **painel administrativo dinâmico (CMS)** integrado a um banco de dados relacional (PostgreSQL via Supabase), permitindo a publicação e persistência de conteúdos em tempo real.

---

## Funcionalidades e Estrutura do Portal

1. **Notícias & Mercado**: Feed dinâmico de tendências tecnológicas, alimentado diretamente via banco de dados.
2. **Networking & Presença Profissional**: Orientações para otimização do perfil no LinkedIn e uso do GitHub como portfólio ativo.
3. **Trilha de Ingresso em TI**: Passos iniciais cobrindo lógica de programação, fundamentos de sistemas e inglês técnico.
4. **Guia de Cursos Superiores**: Comparativo prático entre ADS, Ciência da Computação, Engenharia de Software, Sistemas de Informação e Redes.
5. **Linguagens de Programação**: Aplicação de mercado de PHP, Python, JavaScript/TypeScript, Java e C# (.NET).
6. **Certificações da Indústria**: Visão geral de qualificações reconhecidas (AWS SysOps, Cisco CCNA, LPI Essentials).
7. **Infraestrutura & Diagnóstico**: Identificação automática de IP público, provedor e ferramenta de consulta de domínios.
8. **Guia Prático do Linux**: Instalação passo a passo, estrutura de diretórios (FHS) e tabela de permissões (`chmod` / `chown`).
9. **Ferramentas de Rede**: Calculadora interativa de sub-redes IPv4 e prefixo CIDR.
10. **Projetos no GitHub**: Vitrine de repositórios práticos integrados ao portal.
11. **Painel CMS (Administração)**: Área restrita para gerenciamento de conteúdo com autenticação segura e persistência de dados.

---

## Arquitetura & Tecnologias

* **Frontend**: HTML5 Semântico, Tailwind CSS (via CDN) e JavaScript Vanilla.
* **Backend & Banco de Dados**:
  * **Supabase Auth**: Autenticação segura do administrador via e-mail e senha.
  * **Supabase Database (PostgreSQL)**: Armazenamento persistente de notícias e postagens do portal.
  * **Row Level Security (RLS)**: Leitura pública de conteúdos com permissão de inserção/edição estritamente restrita ao administrador autenticado.
* **Hospedagem**: GitHub Pages.

---

## Repositórios Destacados

* [`sistema_ponto`](https://github.com/gabrielladeirameireles/sistema_ponto.git): Sistema de gestão de frequência e controle de ponto eletrônico.
* [`cog_ndvi_engine`](https://github.com/gabrielladeirameireles/cog_ndvi_engine.git): Motor de processamento espacial para cálculo de NDVI via Cloud Optimized GeoTIFF.
* [`shield-gateway`](https://github.com/gabrielladeirameireles/shield-gateway.git): Gateway de segurança e inspeção de tráfego de infraestrutura.

---

## Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/gabrielladeirameireles/PontoAPonto.git](https://github.com/gabrielladeirameireles/PontoAPonto.git)
