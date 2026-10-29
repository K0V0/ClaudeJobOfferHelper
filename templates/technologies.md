# Technology catalog

Shared list of technologies with aliases, related technologies and calibration questions.
Every candidate gets the same questions for the same technology, so profiles are comparable.

## How to use

- Match names from the candidate or from an offer against **Name** and **Aliases** (case insensitive).
- **Related** technologies give partial credit when the exact one is missing in the profile
  (count as one level lower, max level 2).
- Calibration questions are yes/no. Each has a level tag. Candidate level for technology is
  the highest level where candidate answered *yes*, with at least one *yes* on every lower level.
- If a technology is not here, generate questions in the same style, ask them and append
  the new technology to the end of this file (section *Added by agent*).

## Level scale

| level | meaning |
| ----- | ------- |
| 0 | never used |
| 1 | tutorial, school or hobby project |
| 2 | used in real project, with help of others |
| 3 | independent in production |
| 4 | designs solutions, solves hard problems, mentors others |

## Common questions for every technology

- How many years have You used it, and when last time ?
- Where: production, side project, school / course ?
- Do You want to keep working with it ? (yes / neutral / no)

---

## Backend

### Java
- Category: language
- Aliases: Java SE, JDK, Java 17, Java 21
- Related: Kotlin, Scala
1. [L1] Did You write a Java application longer than a few classes ?
2. [L2] Did You use streams, Optional and records in production code ?
3. [L3] Did You work with concurrency - ExecutorService, CompletableFuture or virtual threads ?
4. [L3] Did You analyse a memory leak or a heap / thread dump ?
5. [L4] Did You tune GC or JVM flags based on measurements ?

### Kotlin
- Category: language
- Aliases: Kotlin JVM
- Related: Java
1. [L1] Did You write a Kotlin application or script ?
2. [L2] Did You use Kotlin in a production backend ?
3. [L3] Did You use coroutines in production ?
4. [L3] Did You mix Kotlin and Java in one codebase and deal with interop issues ?
5. [L4] Did You write a DSL or library in Kotlin used by other teams ?

### Spring Boot
- Category: framework
- Aliases: Spring, Spring Framework, Spring MVC
- Related: Quarkus, Micronaut, Jakarta EE
1. [L1] Did You create a Spring Boot application with REST endpoints ?
2. [L2] Did You use profiles, `@ConfigurationProperties` and externalized configuration ?
3. [L3] Did You configure Spring Security (JWT, OAuth2 or session based) ?
4. [L3] Did You write integration tests with `@SpringBootTest` or test slices ?
5. [L4] Did You implement Your own Spring Boot starter / auto-configuration module ?
6. [L4] Did You use Spring WebFlux / reactive stack in production ?

### Hibernate / JPA
- Category: persistence
- Aliases: JPA, Spring Data JPA, Hibernate ORM, Jakarta Persistence
- Related: jOOQ, MyBatis, JDBC
1. [L1] Did You map entities and relations with JPA annotations ?
2. [L2] Did You write custom queries (JPQL, Criteria or native) ?
3. [L3] Did You find and fix an N+1 problem or lazy loading exception ?
4. [L3] Did You manage transactions explicitly (propagation, isolation) ?
5. [L4] Did You use second level cache, batch processing or optimistic locking under load ?

### Quarkus
- Category: framework
- Aliases: Quarkus native
- Related: Spring Boot, Micronaut
1. [L1] Did You create a Quarkus application ?
2. [L2] Did You use Quarkus in a real project ?
3. [L3] Did You build a native image with GraalVM ?
4. [L4] Did You write a Quarkus extension ?

### Python
- Category: language
- Aliases: Python 3
- Related: -
1. [L1] Did You write Python scripts for automation ?
2. [L2] Did You build a service with Django, Flask or FastAPI ?
3. [L3] Did You manage dependencies and packaging (poetry, uv, pip-tools) for a production app ?
4. [L4] Did You profile and optimise Python code or use asyncio in production ?

## Data

### SQL
- Category: database
- Aliases: relational databases, RDBMS
- Related: PostgreSQL, MySQL, Oracle, MSSQL
1. [L1] Did You write SELECT queries with JOIN and GROUP BY ?
2. [L2] Did You design a database schema with constraints and indexes ?
3. [L3] Did You read an execution plan and fix a slow query ?
4. [L3] Did You use window functions or CTEs ?
5. [L4] Did You design partitioning, replication or a zero downtime migration ?

### PostgreSQL
- Category: database
- Aliases: Postgres, PSQL
- Related: SQL, MySQL, Oracle
1. [L1] Did You use PostgreSQL as an application database ?
2. [L2] Did You write migrations (Flyway, Liquibase) for PostgreSQL ?
3. [L3] Did You use JSONB, full text search or PostgreSQL specific index types ?
4. [L4] Did You tune PostgreSQL configuration, vacuum or replication ?

### MongoDB
- Category: database
- Aliases: Mongo
- Related: other NoSQL document stores
1. [L1] Did You store and query documents in MongoDB ?
2. [L2] Did You design document structure for a real application ?
3. [L3] Did You write aggregation pipelines ?
4. [L4] Did You configure sharding or replica sets ?

### Redis
- Category: database
- Aliases: Valkey
- Related: Memcached, Hazelcast
1. [L1] Did You use Redis as a cache ?
2. [L2] Did You decide cache invalidation strategy and TTLs ?
3. [L3] Did You use Redis for locks, rate limiting or pub/sub ?
4. [L4] Did You run Redis cluster or sentinel in production ?

## Messaging

### Kafka
- Category: messaging
- Aliases: Apache Kafka, Confluent
- Related: RabbitMQ, Pulsar, Kinesis
1. [L1] Did You produce and consume Kafka messages ?
2. [L2] Did You configure consumer groups, partitions and offsets handling ?
3. [L3] Did You handle retries, dead letter topics and idempotency ?
4. [L3] Did You use schema registry (Avro, Protobuf) ?
5. [L4] Did You use Kafka Streams or design topic topology for multiple services ?

### RabbitMQ
- Category: messaging
- Aliases: AMQP
- Related: Kafka, ActiveMQ
1. [L1] Did You send and receive RabbitMQ messages ?
2. [L2] Did You configure exchanges, queues and bindings ?
3. [L3] Did You handle dead lettering, retries and acknowledgements ?
4. [L4] Did You run RabbitMQ cluster in production ?

## Frontend

### TypeScript
- Category: language
- Aliases: TS
- Related: JavaScript
1. [L1] Did You write TypeScript code ?
2. [L2] Did You use TypeScript in a production frontend or backend ?
3. [L3] Did You use generics, union types and type guards ?
4. [L4] Did You configure strict mode and type a shared library ?

### React
- Category: frontend framework
- Aliases: React.js, ReactJS, Next.js
- Related: Vue, Angular
1. [L1] Did You create React components with hooks ?
2. [L2] Did You build forms and fetch data from API in React app ?
3. [L3] Did You manage global state (Redux, Zustand, React Query) ?
4. [L4] Did You optimise rendering performance or do server side rendering ?

### Angular
- Category: frontend framework
- Aliases: Angular 2+
- Related: React, Vue
1. [L1] Did You create Angular components and services ?
2. [L2] Did You use reactive forms and routing ?
3. [L3] Did You use RxJS operators beyond basic subscribe ?
4. [L4] Did You use NgRx or design module structure of a large Angular app ?

## DevOps and cloud

### Docker
- Category: containers
- Aliases: containers, Podman
- Related: Kubernetes
1. [L1] Did You run applications with Docker ?
2. [L2] Did You write a Dockerfile and docker-compose file ?
3. [L3] Did You write multi-stage builds and optimise image size ?
4. [L4] Did You harden images (non-root, distroless, vulnerability scanning) ?

### Kubernetes
- Category: containers
- Aliases: k8s, OpenShift, EKS, AKS, GKE
- Related: Docker, Nomad
1. [L1] Did You deploy an application to Kubernetes ?
2. [L2] Did You write Deployments, Services, ConfigMaps and Ingress manifests ?
3. [L3] Did You debug a crashing pod using logs, events and probes ?
4. [L3] Did You write or maintain Helm charts ?
5. [L4] Did You set up or operate a cluster (autoscaling, network policies, RBAC) ?

### CI/CD
- Category: delivery
- Aliases: GitHub Actions, GitLab CI, Jenkins, Azure DevOps pipelines
- Related: -
1. [L1] Did You work in a project with CI pipeline ?
2. [L2] Did You modify a pipeline (build, test, deploy steps) ?
3. [L3] Did You create a pipeline from scratch ?
4. [L4] Did You design release strategy (blue/green, canary, feature flags) ?

### AWS
- Category: cloud
- Aliases: Amazon Web Services
- Related: Azure, GCP
1. [L1] Did You deploy something to AWS ?
2. [L2] Did You use EC2, S3, RDS or Lambda in a real project ?
3. [L3] Did You configure IAM roles, VPC and security groups ?
4. [L4] Did You design multi-account or highly available architecture on AWS ?

### Azure
- Category: cloud
- Aliases: Microsoft Azure
- Related: AWS, GCP
1. [L1] Did You deploy something to Azure ?
2. [L2] Did You use App Service, Functions, Storage or Azure SQL in a real project ?
3. [L3] Did You configure networking, managed identities and Key Vault ?
4. [L4] Did You design architecture on Azure for a production system ?

### Terraform
- Category: infrastructure as code
- Aliases: OpenTofu, IaC
- Related: Pulumi, CloudFormation, Bicep
1. [L1] Did You run `terraform plan` and `apply` ?
2. [L2] Did You write Terraform resources for a real environment ?
3. [L3] Did You write reusable modules and manage remote state ?
4. [L4] Did You design IaC structure for multiple environments and teams ?

### Observability
- Category: operations
- Aliases: monitoring, logging, Prometheus, Grafana, ELK, OpenTelemetry, Datadog
- Related: -
1. [L1] Did You search application logs in a central tool ?
2. [L2] Did You create a dashboard or alert ?
3. [L3] Did You add custom metrics or tracing to an application ?
4. [L4] Did You define SLOs or set up monitoring stack for a system ?

## Practices

### Testing
- Category: practice
- Aliases: JUnit, Mockito, Testcontainers, TDD
- Related: -
1. [L1] Did You write unit tests ?
2. [L2] Did You write integration tests with real database or Testcontainers ?
3. [L3] Did You work with TDD or contract tests ?
4. [L4] Did You define test strategy for a project ?

### Microservices
- Category: architecture
- Aliases: distributed systems, service oriented architecture
- Related: -
1. [L1] Did You work on a project with multiple services ?
2. [L2] Did You implement communication between services (REST, messaging) ?
3. [L3] Did You handle resilience - timeouts, retries, circuit breakers ?
4. [L4] Did You split a monolith or design service boundaries ?

### REST API design
- Category: architecture
- Aliases: REST, OpenAPI, Swagger
- Related: GraphQL, gRPC
1. [L1] Did You implement REST endpoints ?
2. [L2] Did You write or generate an OpenAPI specification ?
3. [L3] Did You design API versioning, pagination and error format ?
4. [L4] Did You design public API used by external customers ?

---

## Added by agent

<!-- Agent appends new technologies here in the same format -->

### Bash / Linux
- Category: operations
- Aliases: Bash, Shell, Linux, Unix, Ubuntu, RHEL
- Related: PowerShell
1. [L1] Did You use Linux command line daily (files, processes, permissions, ssh) ?
2. [L2] Did You write Bash scripts with arguments, conditions and loops used by others ?
3. [L3] Did You debug a production Linux server (disk, memory, network, systemd, journald) ?
4. [L3] Did You write Bash scripts for deployment or CI with proper error handling (`set -euo pipefail`, traps) ?
5. [L4] Did You harden or tune Linux servers (kernel params, firewall, users, SELinux / AppArmor) ?

### ArgoCD
- Category: delivery
- Aliases: Argo CD, GitOps, Flux
- Related: Kubernetes, Helm, CI/CD
1. [L1] Did You deploy an application through ArgoCD ?
2. [L2] Did You write ArgoCD Application manifests and sync policies ?
3. [L3] Did You set up ArgoCD from scratch and structure a GitOps repository ?
4. [L3] Did You use ApplicationSets, app of apps or sync waves / hooks ?
5. [L4] Did You design GitOps promotion between multiple environments or clusters ?

### JavaScript / Node.js
- Category: language
- Aliases: JavaScript, JS, ECMAScript, Node.js, NodeJS, Express
- Related: TypeScript
1. [L1] Did You write JavaScript for a web page (DOM, events, fetch) ?
2. [L2] Did You write or maintain a Node.js service in a real project ?
3. [L3] Did You use async / await, Promises and npm dependencies in production code ?
4. [L4] Did You profile or debug event loop, memory or performance problems in Node.js ?

### Ruby on Rails
- Category: framework
- Aliases: Ruby, Rails, RoR
- Related: Django, Laravel
1. [L1] Did You create a Rails application with models, controllers and views ?
2. [L2] Did You use ActiveRecord associations, migrations and validations in a real project ?
3. [L3] Did You run a Rails application in production for real users ?
4. [L3] Did You write or fork a Ruby gem ?
5. [L4] Did You optimise Rails performance (N+1, caching, background jobs) ?

### Camunda
- Category: workflow engine
- Aliases: Camunda BPM, Camunda 7, Camunda 8, Zeebe, BPMN
- Related: Flowable, Activiti, jBPM
1. [L1] Did You model or read BPMN processes ?
2. [L2] Did You implement service tasks / external task workers or Java delegates ?
3. [L3] Did You debug stuck process instances, incidents or failed jobs in production ?
4. [L3] Did You integrate Camunda into a Spring Boot application or extend the engine ?
5. [L4] Did You design a platform or reusable components on top of Camunda ?

### ActiveMQ / Artemis
- Category: messaging
- Aliases: ActiveMQ, Artemis, ArtemisMQ, JMS, IBM MQ
- Related: RabbitMQ, Kafka
1. [L1] Did You send and receive JMS messages ?
2. [L2] Did You configure queues, topics and listeners in a Spring application ?
3. [L3] Did You handle redelivery, dead letter queues and transactions ?
4. [L4] Did You configure or operate the broker (clustering, persistence, HA) ?

### HashiCorp Vault
- Category: security
- Aliases: Vault, secrets management, Infisical, AWS Secrets Manager
- Related: Kubernetes, Terraform
1. [L1] Did You read secrets from Vault in an application or pipeline ?
2. [L2] Did You configure secret engines, paths and policies ?
3. [L3] Did You integrate Vault with Kubernetes (injector, CSI, External Secrets) ?
4. [L4] Did You run Vault in production (unsealing, HA, dynamic secrets, PKI) ?

### Keycloak
- Category: security
- Aliases: Red Hat SSO, OIDC provider, IAM
- Related: Spring Security, OAuth2
1. [L1] Did You integrate an application with Keycloak login ?
2. [L2] Did You configure realms, clients, roles and mappers ?
3. [L3] Did You configure identity brokering, federation (LDAP / AD) or custom flows ?
4. [L4] Did You run Keycloak in production or write Keycloak extensions / themes ?

### Elasticsearch
- Category: database
- Aliases: Elastic, OpenSearch, ELK
- Related: Observability, MongoDB
1. [L1] Did You query Elasticsearch or search data in Kibana ?
2. [L2] Did You index documents and write search queries from an application ?
3. [L3] Did You design mappings, analyzers or aggregations ?
4. [L4] Did You operate a cluster (shards, replicas, index lifecycle) ?

### Maven / Gradle
- Category: build tool
- Aliases: Maven, Gradle
- Related: CI/CD
1. [L1] Did You build a project and add dependencies with Maven or Gradle ?
2. [L2] Did You work with a multi-module project ?
3. [L3] Did You configure plugins, profiles and dependency conflict resolution ?
4. [L4] Did You write own plugin or set up company parent POM / convention plugins ?

### Android
- Category: mobile
- Aliases: Android SDK, Jetpack, Jetpack Compose
- Related: Kotlin, Java
1. [L1] Did You create an Android application ?
2. [L2] Did You publish an app or have real users using it ?
3. [L3] Did You use background work, notifications or lifecycle-aware components ?
4. [L4] Did You design architecture of a larger Android app (MVVM, DI, modularization) ?

### SOAP
- Category: integration
- Aliases: SOAP, WSDL, XML web services, JAX-WS, NDC
- Related: REST API design
1. [L1] Did You call a SOAP service ?
2. [L2] Did You generate clients from WSDL / XSD and map XML messages ?
3. [L3] Did You implement integration against a complex external XML specification ?
4. [L4] Did You design a SOAP or XML based interface for external partners ?

### Event-driven architecture
- Category: architecture
- Aliases: EDA, event-driven, event sourcing, CQRS, asynchronous messaging
- Related: Kafka, RabbitMQ, ActiveMQ / Artemis, Microservices
1. [L1] Did You work on a system where services communicate through events or messages ?
2. [L2] Did You implement publishing and consuming of domain events between services ?
3. [L3] Did You handle eventual consistency, idempotent consumers or outbox pattern ?
4. [L4] Did You design event flows / event contracts for multiple services or use event sourcing / CQRS ?

### AI coding assistants
- Category: tooling
- Aliases: Claude Code, ChatGPT, GitHub Copilot, Cursor, LLM
- Related: -
1. [L1] Did You use an AI chat for coding questions ?
2. [L2] Did You use an AI agent that edits code in Your repository in daily work ?
3. [L3] Did You write project instructions, custom commands or skills for an AI agent ?
4. [L4] Did You build tools or workflows on top of LLM APIs or agents ?
5. [L3] Do You write a specification or plan first and let the agent implement it ?
6. [L3] Do You review agent-written code and guard it with strict tests before merging ?

### Software architecture
- Category: architecture
- Aliases: architectural thinking, solution design, system design, architecture design, ADR
- Related: Microservices, Event-driven architecture, REST API design
1. [L1] Did You follow an existing architecture (layers, modules) and can explain why it is structured that way ?
2. [L2] Did You propose structure for a new feature or module that was accepted by the team ?
3. [L3] Did You design a new service or application from scratch (structure, persistence, integrations) and run it in production ?
4. [L3] Did You write ADRs or lead technical discussions about trade-offs and maintainability ?
5. [L4] Did You set technical direction or a modernization plan for a whole system or several teams ?

### Regulated domain
- Category: domain
- Aliases: fintech, banking, payments, insurance, public sector, regulated environment, PSD2, PSD3
- Related: -
1. [L1] Did You work on a project where audits, compliance or strict release processes were required ?
2. [L2] Did You work in a regulated environment (public sector, insurance, healthcare, energy) ?
3. [L3] Did You work on a production project for a bank, payments or fintech company ?
4. [L4] Did You implement regulatory requirements yourself (PSD2 / PSD3, AML, KYC, strong customer authentication) ?

### Apache Camel
- Category: integration
- Aliases: Camel, Camel K, Camel Quarkus, Red Hat Fuse
- Related: Spring Integration, MuleSoft, ActiveMQ / Artemis
1. [L1] Did You write Camel routes in a tutorial, side project or small task ?
2. [L2] Did You use Camel routes in production with components (Kafka, HTTP, file, JMS) ?
3. [L3] Did You handle redelivery, dead letter channel or EIPs (split, aggregate, content-based router) in production ?
4. [L4] Did You design an integration platform on Camel or write own Camel components ?

### Design patterns / clean code
- Category: practice
- Aliases: design patterns, clean code, SOLID, GoF, refactoring
- Related: Software architecture
1. [L1] Can You explain common design patterns (strategy, factory, builder, adapter) and SOLID ?
2. [L2] Did You use design patterns deliberately in production code ?
3. [L3] Did You refactor legacy code to clean code / SOLID, with tests ?
4. [L3] Did You regularly point out design / clean code problems in code review ?
5. [L4] Did You define coding standards or architecture rules for the team ?

### Jira / Confluence
- Category: tooling
- Aliases: Jira, Confluence, Atlassian, YouTrack
- Related: -
1. [L1] Did You work with tickets, boards and sprints in Jira ?
2. [L2] Did You write or maintain technical documentation in Confluence ?
3. [L3] Did You configure Jira workflows, boards or automation for the team ?

### Google Cloud
- Category: cloud
- Aliases: GCP, Google Cloud Platform, GKE, Cloud Run
- Related: AWS, Azure
1. [L1] Did You deploy something to GCP ?
2. [L2] Did You use GCP managed services (Cloud Run, GKE, Cloud SQL, Pub/Sub) in a real project ?
3. [L3] Did You set up IAM, networking or cost monitoring in GCP ?
4. [L4] Did You design multi-environment GCP infrastructure (projects, IaC, landing zone) ?

### Git
- Category: tooling
- Aliases: GitHub, GitLab, Bitbucket, version control
- Related: SVN
1. [L1] Did You commit, push and pull in Git daily ?
2. [L2] Did You resolve merge conflicts and work with feature branches and pull requests ?
3. [L3] Did You use rebase, cherry-pick, bisect or rewrite history safely ?
4. [L4] Did You define branching strategy or migrate repositories for the team ?

### Microsoft SQL Server
- Category: database
- Aliases: MSSQL, SQL Server, T-SQL, Azure SQL
- Related: SQL, PostgreSQL, Oracle
1. [L1] Did You use SQL Server as an application database ?
2. [L2] Did You write T-SQL queries, stored procedures or migrations for SQL Server ?
3. [L3] Did You analyse execution plans or indexes in SQL Server ?
4. [L4] Did You configure SQL Server high availability, replication or performance tuning ?

### Networking
- Category: operations
- Aliases: network, TCP/IP, DNS, TLS, firewall, load balancer
- Related: Bash / Linux, Kubernetes
1. [L1] Do You understand IP, DNS, ports and HTTP / TLS and use curl, ping, nslookup ?
2. [L2] Did You debug firewall, DNS, proxy or certificate problems between services ?
3. [L3] Did You configure load balancers, ingress, VPN, network policies or subnets ?
4. [L4] Did You design network topology or segmentation for a system ?

### Application servers
- Category: operations
- Aliases: Tomcat, WebLogic, WildFly, JBoss, WebSphere, Apache httpd, Nginx, web server
- Related: Docker, Bash / Linux
1. [L1] Did You deploy an application to Tomcat or another application server ?
2. [L2] Did You configure Apache httpd or Nginx (virtual hosts, reverse proxy) ?
3. [L2] Did You deploy or administer applications on WebLogic, WildFly or WebSphere ?
4. [L3] Did You tune or troubleshoot an application server in production (threads, memory, connection pools) ?
