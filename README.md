# JogaYJoga
# Introdução ao Projeto

Este projeto utiliza uma arquitetura de microserviços, onde cada funcionalidade do sistema é desenvolvida e implantada como um serviço independente. Abaixo, descreveremos o padrão de projeto utilizado para o gateway com balanceamento de carga, seguido pela descrição dos microserviços e ferramentas de DevOps utilizadas no projeto.

## Padrão de Projeto: Gateway com Load Balance

O padrão de projeto de Gateway com Load Balance é utilizado para gerenciar o tráfego de rede de entrada e distribuir as solicitações para os diferentes microserviços disponíveis. Esse padrão melhora a escalabilidade, a disponibilidade e a confiabilidade do sistema. Aqui estão alguns componentes principais:

**Gateway:**

- O gateway serve como o ponto de entrada único para todas as solicitações externas ao sistema.
- Ele autentica e autoriza as solicitações, além de rotear para os microserviços apropriados.

**Load Balancer:**

- O balanceador de carga distribui as solicitações entre instâncias dos microserviços para garantir que nenhuma instância fique sobrecarregada.
- Pode ser implementado usando ferramentas como Nginx, HAProxy ou serviços em nuvem como o AWS Elastic Load Balancing.

## Estrutura do Projeto

### Microserviços

1. **Account:**
   - **Repositório:** `jogayjoga.account`
   - **Descrição:** Gerenciamento de contas de usuários.
   - **Swagger:** [Account API](http://localhost:8080/account/swagger-ui.html)

2. **Account Resource:**
   - **Repositório:** `jogayjoga.account-resource`
   - **Descrição:** Recursos e APIs relacionadas a contas de usuários.

3. **Auth:**
   - **Repositório:** `jogayjoga.auth`
   - **Descrição:** Serviço de autenticação e autorização.
   - **Swagger:** [Auth API](http://localhost:8080/auth/swagger-ui.html)

4. **Auth Resource:**
   - **Repositório:** `jogayjoga.auth-resource`
   - **Descrição:** Recursos e APIs relacionados à autenticação.

5. **Discovery:**
   - **Repositório:** `jogayjoga.discovery`
   - **Descrição:** Serviço de descoberta de microserviços, implementado com Eureka.

6. **Docker API:**
   - **Repositório:** `jogayjoga.docker.api`
   - **Descrição:** API para gerenciamento de contêineres Docker.

7. **Gateway:**
   - **Repositório:** `jogayjoga.gateway`
   - **Descrição:** Ponto de entrada único para o sistema, roteando solicitações para os microserviços.

8. **Ops:**
   - **Repositório:** `jogayjoga.ops`
   - **Descrição:** Operações e monitoramento do sistema.

9. **Court:**
   - **Repositório:** `jogayjoga.court`
   - **Descrição:** Gerenciamento de quadras esportivas.
   - **Swagger:** [Court API](http://localhost:8080/court/swagger-ui.html)

10. **Court Resource:**
    - **Repositório:** `jogayjoga.court-resource`
    - **Descrição:** Recursos e APIs relacionados a quadras esportivas.

11. **Sport:**
    - **Repositório:** `jogayjoga.sport`
    - **Descrição:** Gerenciamento de esportes e atividades.
    - **Swagger:** [Sport API](http://localhost:8080/sport/swagger-ui.html)

12. **Sport Resource:**
    - **Repositório:** `jogayjoga.sport-resource`
    - **Descrição:** Recursos e APIs relacionados a esportes.

13. **Group:**
    - **Repositório:** `jogayjoga.group`
    - **Descrição:** Gerenciamento de grupos e times.
    - **Swagger:** [Group API](http://localhost:8080/group/swagger-ui.html)

14. **Group Resource:**
    - **Repositório:** `jogayjoga.group-resource`
    - **Descrição:** Recursos e APIs relacionados a grupos.

15. **DB:**
    - **Repositório:** `jogayjoga.db`
    - **Descrição:** Gerenciamento de banco de dados.

16. **Front-end:**
    - **Repositório:** `jogayjoga.front-end`
    - **Descrição:** Interface do usuário do sistema.

### Ferramentas de DevOps

1. **Observabilidade:**
   - **Descrição:** Ferramentas e práticas para monitoramento e logging do sistema.
   - **Tecnologias:** Prometheus e Grafana.

2. **Jenkins:**
   - **Descrição:** Ferramenta de automação para integração contínua e entrega contínua (CI/CD).
   - **Configurações para pipelines de build e deploy.**

3. **Kubernetes:**
   - **Descrição:** Orquestrador de contêineres para implantação, escalonamento e gerenciamento dos aplicativos em contêineres.
   - **Configurações de deployment, services e ingress.**

### Cloud

1. **AWS:**
   - **Serviços utilizados:** EC2, S3, EKS.
   - **Configurações para deploy e infraestrutura na nuvem.**

### Redis para Cache

O Redis foi implementado para caching, ajudando a melhorar o desempenho do sistema ao reduzir a necessidade de consultas frequentes ao banco de dados. Isso é especialmente útil para dados que são lidos frequentemente.

### Kafka para Mensageria

O Apache Kafka foi implementado para gerenciar a mensageria assíncrona dentro dos microserviços.
