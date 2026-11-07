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
  the new technology to the end of this file (section *Added by agent*), including its **Tier**.

## Tier

Every technology has a **Tier** line. Fields are `backend`, `frontend` and `devops`.

| tier | meaning | calibration questions |
| ---- | ------- | --------------------- |
| core for <fields> | the job in that field is built on it - language, main framework, persistence, runtime platform (Java, Spring Boot, TypeScript, Angular, SQL, Docker, Kubernetes, ...) | 8-10, at least 2 per level L1-L4 |
| adjacent | commonly used, but only as a component or extension of the app (Kafka, Redis, Keycloak, SharePoint, Backstage, ...), also tools, domains and soft skills | 4-6 |

- A technology can be core for more fields (`core for frontend, backend`). Core for any field means
  the full 8-10 questions are asked, regardless of candidate target field or level.
- When unsure, choose `adjacent` - most technologies are.
- The Tier only decides how deep the interview goes. It does not change offer scoring.

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
- Tier: core for backend
- Aliases: Java SE, JDK, Java 17, Java 21
- Related: Kotlin, Scala
1. [L1] Did You write a Java application longer than a few classes ?
2. [L1] Did You use collections, generics and exception handling in Your own code ?
3. [L2] Did You use streams, Optional and records in production code ?
4. [L2] Did You debug a Java application with breakpoints and find the cause from a stack trace ?
5. [L2] Did You upgrade a project to a newer Java version (for example 8 -> 17 -> 21) ?
6. [L3] Did You work with concurrency - ExecutorService, CompletableFuture or virtual threads ?
7. [L3] Did You find and fix a race condition or deadlock ?
8. [L3] Did You analyse a memory leak or a heap / thread dump ?
9. [L4] Did You tune GC or JVM flags based on measurements ?
10. [L4] Did You write a library or shared module used by other teams and keep its API backward compatible ?

### Kotlin
- Category: language
- Tier: core for backend
- Aliases: Kotlin JVM
- Related: Java
1. [L1] Did You write a Kotlin application or script ?
2. [L1] Did You use data classes, null safety and extension functions ?
3. [L2] Did You use Kotlin in a production backend ?
4. [L2] Did You use collection functions (map, filter, groupBy) and scope functions (let, apply) deliberately ?
5. [L2] Did You model domain states with sealed classes and `when` expressions ?
6. [L3] Did You use coroutines in production ?
7. [L3] Did You mix Kotlin and Java in one codebase and deal with interop issues ?
8. [L4] Did You debug coroutine problems (structured concurrency, cancellation, blocked dispatcher) ?
9. [L4] Did You write a DSL or library in Kotlin used by other teams ?

### Spring Boot
- Category: framework
- Tier: core for backend
- Aliases: Spring, Spring Framework, Spring MVC
- Related: Quarkus, Micronaut, Jakarta EE
1. [L1] Did You create a Spring Boot application with REST endpoints ?
2. [L1] Did You use dependency injection with Spring beans and constructor injection ?
3. [L2] Did You use profiles, `@ConfigurationProperties` and externalized configuration ?
4. [L2] Did You handle errors globally with `@ControllerAdvice` and validate input with Bean Validation ?
5. [L3] Did You configure Spring Security (JWT, OAuth2 or session based) ?
6. [L3] Did You write integration tests with `@SpringBootTest` or test slices ?
7. [L3] Did You use Actuator health checks and metrics in production ?
8. [L3] Did You upgrade Spring Boot major version (2 -> 3, javax -> jakarta) ?
9. [L4] Did You implement Your own Spring Boot starter / auto-configuration module ?
10. [L4] Did You use Spring WebFlux / reactive stack in production ?

### Hibernate / JPA
- Category: persistence
- Tier: core for backend
- Aliases: JPA, Spring Data JPA, Hibernate ORM, Jakarta Persistence
- Related: jOOQ, MyBatis, JDBC
1. [L1] Did You map entities and relations with JPA annotations ?
2. [L1] Did You use Spring Data repositories with derived query methods ?
3. [L2] Did You write custom queries (JPQL, Criteria or native) ?
4. [L2] Did You change entities together with database migrations (Flyway, Liquibase) ?
5. [L2] Did You use DTO projections or pagination instead of loading whole entities ?
6. [L3] Did You find and fix an N+1 problem or lazy loading exception ?
7. [L3] Did You manage transactions explicitly (propagation, isolation) ?
8. [L3] Did You use SQL logging or Hibernate statistics to find slow or excessive queries ?
9. [L4] Did You use second level cache, batch processing or optimistic locking under load ?
10. [L4] Did You debug dirty checking, flush order or detached entity problems (unexpected updates) ?

### Quarkus
- Category: framework
- Tier: core for backend
- Aliases: Quarkus native
- Related: Spring Boot, Micronaut
1. [L1] Did You create a Quarkus application ?
2. [L1] Did You use Quarkus dev mode and Dev Services ?
3. [L2] Did You use Quarkus in a real project ?
4. [L2] Did You use RESTEasy Reactive, Panache or CDI beans in Quarkus ?
5. [L3] Did You configure Quarkus for Kubernetes (health, metrics, config, container image) ?
6. [L3] Did You build a native image with GraalVM ?
7. [L4] Did You solve native image problems (reflection config, build time initialization) ?
8. [L4] Did You write a Quarkus extension ?

### Python
- Category: language
- Tier: core for backend
- Aliases: Python 3
- Related: -
1. [L1] Did You write Python scripts for automation ?
2. [L1] Did You use virtual environments and install packages with pip ?
3. [L2] Did You build a service with Django, Flask or FastAPI ?
4. [L2] Did You write tests with pytest ?
5. [L2] Did You use type hints and run a type checker or linter (mypy, ruff) ?
6. [L3] Did You manage dependencies and packaging (poetry, uv, pip-tools) for a production app ?
7. [L3] Did You connect a Python service to a database with ORM and migrations (SQLAlchemy, Django ORM, Alembic) ?
8. [L4] Did You use asyncio in production ?
9. [L4] Did You profile and optimise Python code (cProfile, py-spy) ?

### C# / .NET
- Category: language
- Tier: core for backend
- Aliases: C#, .NET, .NET Core, ASP.NET Core, Entity Framework, EF Core
- Related: Java
1. [L1] Did You write a C# application longer than a few classes ?
2. [L1] Did You use LINQ, generics and async / await ?
3. [L2] Did You build ASP.NET Core Web API in a real project ?
4. [L2] Did You use Entity Framework Core with migrations ?
5. [L2] Did You use dependency injection and configuration in ASP.NET Core ?
6. [L3] Did You configure authentication (JWT, OAuth2, ASP.NET Identity) ?
7. [L3] Did You write integration tests (WebApplicationFactory, xUnit, NUnit) ?
8. [L4] Did You profile and fix performance or memory problems in .NET (dotnet-trace, dotnet-dump) ?
9. [L4] Did You migrate .NET Framework application to modern .NET ?

## Data

### SQL
- Category: database
- Tier: core for backend
- Aliases: relational databases, RDBMS
- Related: PostgreSQL, MySQL, Oracle, MSSQL
1. [L1] Did You write SELECT queries with JOIN and GROUP BY ?
2. [L1] Did You write INSERT, UPDATE and DELETE with conditions ?
3. [L2] Did You design a database schema with constraints and indexes ?
4. [L2] Did You use subqueries, outer joins and NULL handling correctly ?
5. [L2] Did You write schema migrations that also changed existing data ?
6. [L3] Did You read an execution plan and fix a slow query ?
7. [L3] Did You use window functions or CTEs ?
8. [L3] Did You solve locking, deadlock or transaction isolation problems ?
9. [L4] Did You design partitioning, replication or a zero downtime migration ?
10. [L4] Did You design data model for a large system (normalization trade-offs, archiving, multi-tenancy) ?

### PostgreSQL
- Category: database
- Tier: adjacent
- Aliases: Postgres, PSQL
- Related: SQL, MySQL, Oracle
1. [L1] Did You use PostgreSQL as an application database ?
2. [L2] Did You write migrations (Flyway, Liquibase) for PostgreSQL ?
3. [L3] Did You use JSONB, full text search or PostgreSQL specific index types ?
4. [L4] Did You tune PostgreSQL configuration, vacuum or replication ?

### MongoDB
- Category: database
- Tier: adjacent
- Aliases: Mongo
- Related: other NoSQL document stores
1. [L1] Did You store and query documents in MongoDB ?
2. [L2] Did You design document structure for a real application ?
3. [L3] Did You write aggregation pipelines ?
4. [L4] Did You configure sharding or replica sets ?

### Redis
- Category: database
- Tier: adjacent
- Aliases: Valkey
- Related: Memcached, Hazelcast
1. [L1] Did You use Redis as a cache ?
2. [L2] Did You decide cache invalidation strategy and TTLs ?
3. [L3] Did You use Redis for locks, rate limiting or pub/sub ?
4. [L4] Did You run Redis cluster or sentinel in production ?

## Messaging

### Kafka
- Category: messaging
- Tier: adjacent
- Aliases: Apache Kafka, Confluent
- Related: RabbitMQ, Pulsar, Kinesis
1. [L1] Did You produce and consume Kafka messages ?
2. [L2] Did You configure consumer groups, partitions and offsets handling ?
3. [L3] Did You handle retries, dead letter topics and idempotency ?
4. [L3] Did You use schema registry (Avro, Protobuf) ?
5. [L4] Did You use Kafka Streams or design topic topology for multiple services ?

### RabbitMQ
- Category: messaging
- Tier: adjacent
- Aliases: AMQP
- Related: Kafka, ActiveMQ
1. [L1] Did You send and receive RabbitMQ messages ?
2. [L2] Did You configure exchanges, queues and bindings ?
3. [L3] Did You handle dead lettering, retries and acknowledgements ?
4. [L4] Did You run RabbitMQ cluster in production ?

## Frontend

### TypeScript
- Category: language
- Tier: core for frontend, backend
- Aliases: TS
- Related: JavaScript
1. [L1] Did You write TypeScript code ?
2. [L1] Did You type function parameters, objects and API responses with interfaces or types ?
3. [L2] Did You use TypeScript in a production frontend or backend ?
4. [L2] Did You fix type errors without `any` or `@ts-ignore` ?
5. [L3] Did You use generics, union types and type guards ?
6. [L3] Did You use utility and mapped types (Partial, Pick, Record, keyof) ?
7. [L3] Did You configure tsconfig for a project (strict mode, paths, module resolution) ?
8. [L4] Did You type a shared library used by other projects (published types, declaration files) ?
9. [L4] Did You write conditional or template literal types ?

### React
- Category: frontend framework
- Tier: core for frontend
- Aliases: React.js, ReactJS, Next.js
- Related: Vue, Angular
1. [L1] Did You create React components with hooks ?
2. [L1] Did You pass props, lift state up and render lists with keys ?
3. [L2] Did You build forms and fetch data from API in React app ?
4. [L2] Did You use React Router or Next.js routing ?
5. [L2] Did You write tests with React Testing Library or similar ?
6. [L3] Did You manage global state (Redux, Zustand, React Query) ?
7. [L3] Did You write custom hooks and fix bugs caused by `useEffect` dependencies ?
8. [L4] Did You optimise rendering performance (memo, React profiler, virtualized lists) ?
9. [L4] Did You use server side rendering or React Server Components in production ?

### Angular
- Category: frontend framework
- Tier: core for frontend
- Aliases: Angular 2+
- Related: React, Vue
1. [L1] Did You create Angular components and services ?
2. [L1] Did You use data binding, directives and pipes ?
3. [L2] Did You use reactive forms and routing ?
4. [L2] Did You call APIs with HttpClient and use interceptors ?
5. [L2] Did You write tests with Jasmine, Jest or Angular testing utilities ?
6. [L3] Did You use RxJS operators beyond basic subscribe ?
7. [L3] Did You use lazy loaded routes, guards and resolvers ?
8. [L3] Did You upgrade Angular across major versions ?
9. [L4] Did You use NgRx or design module structure of a large Angular app ?
10. [L4] Did You optimise change detection (OnPush, signals, zoneless) ?

### Vue
- Category: frontend framework
- Tier: core for frontend
- Aliases: Vue.js, Vue 3, Nuxt
- Related: React, Angular
1. [L1] Did You create Vue components ?
2. [L1] Did You use template directives (v-if, v-for, v-model), props and events ?
3. [L2] Did You build forms and fetch data from API in a Vue app ?
4. [L2] Did You use Vue Router ?
5. [L3] Did You use Composition API and write own composables ?
6. [L3] Did You manage global state with Pinia or Vuex ?
7. [L4] Did You use Nuxt or server side rendering in production ?
8. [L4] Did You migrate Vue 2 to Vue 3 or design structure of a large Vue app ?

### HTML / CSS
- Category: frontend
- Tier: core for frontend
- Aliases: HTML5, CSS3, SCSS, Sass, Tailwind, responsive design, accessibility
- Related: React, Angular, Vue
1. [L1] Did You write HTML pages styled with CSS ?
2. [L1] Did You use flexbox or grid for layout ?
3. [L2] Did You build a responsive layout that works on mobile and desktop ?
4. [L2] Did You use SCSS, CSS modules or Tailwind in a real project ?
5. [L3] Did You make a page accessible (semantic HTML, ARIA, keyboard navigation, contrast) ?
6. [L3] Did You fix cross-browser or layout bugs reported by users ?
7. [L4] Did You build or maintain a design system or component library ?
8. [L4] Did You optimise page load and rendering (Core Web Vitals, critical CSS) ?

## DevOps and cloud

### Docker
- Category: containers
- Tier: core for devops
- Aliases: containers, Podman
- Related: Kubernetes
1. [L1] Did You run applications with Docker ?
2. [L1] Did You use volumes, ports and environment variables when running containers ?
3. [L2] Did You write a Dockerfile and docker-compose file ?
4. [L2] Did You debug a container that fails to start (logs, exec, inspect) ?
5. [L2] Did You push images to a registry and version them with tags ?
6. [L3] Did You write multi-stage builds and optimise image size ?
7. [L3] Did You set up container networking and health checks for several services ?
8. [L4] Did You harden images (non-root, distroless, vulnerability scanning) ?
9. [L4] Did You design image build and promotion process for multiple teams (base images, caching, registries) ?

### Kubernetes
- Category: containers
- Tier: core for devops
- Aliases: k8s, OpenShift, EKS, AKS, GKE
- Related: Docker, Nomad
1. [L1] Did You deploy an application to Kubernetes ?
2. [L1] Did You use kubectl to view pods, logs and describe resources ?
3. [L2] Did You write Deployments, Services, ConfigMaps and Ingress manifests ?
4. [L2] Did You set resource requests / limits and liveness / readiness probes ?
5. [L2] Did You use Secrets, namespaces and rolling updates ?
6. [L3] Did You debug a crashing pod using logs, events and probes ?
7. [L3] Did You write or maintain Helm charts ?
8. [L3] Did You configure autoscaling, PodDisruptionBudget or affinity rules ?
9. [L4] Did You set up or operate a cluster (autoscaling, network policies, RBAC) ?
10. [L4] Did You upgrade a cluster or write an operator / CRD ?

### CI/CD
- Category: delivery
- Tier: core for devops
- Aliases: GitHub Actions, GitLab CI, Jenkins, Azure DevOps pipelines
- Related: -
1. [L1] Did You work in a project with CI pipeline ?
2. [L1] Did You read pipeline logs to find why a build failed ?
3. [L2] Did You modify a pipeline (build, test, deploy steps) ?
4. [L2] Did You use pipeline secrets, caches and artifacts ?
5. [L3] Did You create a pipeline from scratch ?
6. [L3] Did You build or run staging / UAT / test environment used by QA team ?
7. [L3] Did You package software for on-premises deployment at customers (Helm chart, images, air-gapped delivery) ?
8. [L3] Did You add automated security checks to pipelines (image scanning, SAST, dependency scanning) ?
9. [L4] Did You design release strategy (blue/green, canary, feature flags) ?
10. [L4] Did You deploy or operate multi-tenant SaaS (one deployment, many customers) ?

### AWS
- Category: cloud
- Tier: core for devops
- Aliases: Amazon Web Services
- Related: Azure, GCP
1. [L1] Did You deploy something to AWS ?
2. [L1] Did You use AWS console and CLI with credentials / profiles ?
3. [L2] Did You use EC2, S3, RDS or Lambda in a real project ?
4. [L2] Did You read CloudWatch logs and metrics of a running service ?
5. [L3] Did You configure IAM roles, VPC and security groups ?
6. [L3] Did You deploy containers to ECS, EKS or Fargate ?
7. [L3] Did You manage AWS infrastructure as code (Terraform, CloudFormation, CDK) ?
8. [L4] Did You design multi-account or highly available architecture on AWS ?
9. [L4] Did You optimise AWS costs or plan disaster recovery ?

### Azure
- Category: cloud
- Tier: core for devops
- Aliases: Microsoft Azure
- Related: AWS, GCP
1. [L1] Did You deploy something to Azure ?
2. [L1] Did You use Azure portal and Azure CLI ?
3. [L2] Did You use App Service, Functions, Storage or Azure SQL in a real project ?
4. [L2] Did You read logs and metrics in Azure Monitor or Application Insights ?
5. [L3] Did You configure networking, managed identities and Key Vault ?
6. [L3] Did You deploy containers to AKS or Container Apps ?
7. [L3] Did You manage Azure resources as code (Bicep, ARM, Terraform) ?
8. [L4] Did You design architecture on Azure for a production system ?
9. [L4] Did You set up landing zone, subscriptions, policies or cost management for an organisation ?

### Terraform
- Category: infrastructure as code
- Tier: core for devops
- Aliases: OpenTofu, IaC
- Related: Pulumi, CloudFormation, Bicep
1. [L1] Did You run `terraform plan` and `apply` ?
2. [L1] Did You read a plan and understand what it will change ?
3. [L2] Did You write Terraform resources for a real environment ?
4. [L2] Did You use variables, outputs and data sources ?
5. [L3] Did You write reusable modules and manage remote state ?
6. [L3] Did You import existing resources or fix state drift (`import`, `state mv`) ?
7. [L3] Did You run Terraform in CI with plan review before apply ?
8. [L4] Did You design IaC structure for multiple environments and teams ?
9. [L4] Did You write policy checks or tests for Terraform (OPA, Sentinel, Terratest) ?

### Observability
- Category: operations
- Tier: core for devops
- Aliases: monitoring, logging, Prometheus, Grafana, ELK, OpenTelemetry, Datadog
- Related: -
1. [L1] Did You search application logs in a central tool ?
2. [L1] Did You read metrics dashboards to check health of a service ?
3. [L2] Did You create a dashboard or alert ?
4. [L2] Did You use structured logging with correlation ids ?
5. [L3] Did You add custom metrics or tracing to an application ?
6. [L3] Did You find root cause of a production incident from logs, metrics and traces ?
7. [L3] Did You set up log collection or metrics scraping (Fluent Bit, Prometheus, OpenTelemetry Collector) ?
8. [L4] Did You define SLOs or set up monitoring stack for a system ?
9. [L4] Did You reduce alert noise or write on call runbooks for a team ?

## Practices

### Testing
- Category: practice
- Tier: core for backend, frontend
- Aliases: JUnit, Mockito, Testcontainers, TDD
- Related: -
1. [L1] Did You write unit tests ?
2. [L1] Did You use mocks or stubs (Mockito, Jest mocks) ?
3. [L2] Did You write integration tests with real database or Testcontainers ?
4. [L2] Did You fix flaky tests or tests broken by refactoring ?
5. [L2] Did You write end-to-end or UI tests (Selenium, Playwright, Cypress) ?
6. [L3] Did You work with TDD or contract tests ?
7. [L3] Did You use test coverage or mutation testing to find untested code ?
8. [L4] Did You define test strategy for a project ?
9. [L4] Did You set up test infrastructure for a team (test data, environments, parallel runs in CI) ?

### Microservices
- Category: architecture
- Tier: core for backend
- Aliases: distributed systems, service oriented architecture
- Related: -
1. [L1] Did You work on a project with multiple services ?
2. [L1] Did You run several services locally together (docker-compose, local profiles) ?
3. [L2] Did You implement communication between services (REST, messaging) ?
4. [L2] Did You use service discovery, API gateway or central configuration ?
5. [L3] Did You handle resilience - timeouts, retries, circuit breakers ?
6. [L3] Did You trace a request across services with correlation id or distributed tracing ?
7. [L3] Did You handle data consistency between services (saga, outbox, compensation) ?
8. [L4] Did You split a monolith or design service boundaries ?
9. [L4] Did You decide that something should not be a separate service and explain the trade-off ?

### REST API design
- Category: architecture
- Tier: core for backend
- Aliases: REST, OpenAPI, Swagger
- Related: GraphQL, gRPC
1. [L1] Did You implement REST endpoints ?
2. [L1] Did You use correct HTTP methods and status codes ?
3. [L2] Did You write or generate an OpenAPI specification ?
4. [L2] Did You generate clients or servers from OpenAPI (contract first) ?
5. [L3] Did You design API versioning, pagination and error format ?
6. [L3] Did You secure an API (OAuth2 scopes, API keys, rate limiting) ?
7. [L3] Did You design idempotent operations or optimistic concurrency (ETag, Idempotency-Key) ?
8. [L4] Did You design public API used by external customers ?
9. [L4] Did You deprecate an API version and migrate its consumers without breaking them ?

---

## Added by agent

<!-- Agent appends new technologies here in the same format, with Tier line -->

### Bash / Linux
- Category: operations
- Tier: core for devops
- Aliases: Bash, Shell, Linux, Unix, Ubuntu, RHEL
- Related: PowerShell
1. [L1] Did You use Linux command line daily (files, processes, permissions, ssh) ?
2. [L1] Did You use grep, find, pipes and redirection to process files and logs ?
3. [L2] Did You write Bash scripts with arguments, conditions and loops used by others ?
4. [L2] Did You manage packages, services and cron jobs on a Linux server ?
5. [L2] Did You configure ssh keys, users, groups and file permissions ?
6. [L3] Did You debug a production Linux server (disk, memory, network, systemd, journald) ?
7. [L3] Did You write Bash scripts for deployment or CI with proper error handling (`set -euo pipefail`, traps) ?
8. [L3] Did You use sed, awk or jq to transform data in scripts ?
9. [L4] Did You harden or tune Linux servers (kernel params, firewall, users, SELinux / AppArmor) ?
10. [L4] Did You analyse performance with strace, perf, iostat or similar tools ?

### ArgoCD
- Category: delivery
- Tier: adjacent
- Aliases: Argo CD, GitOps, Flux
- Related: Kubernetes, Helm, CI/CD
1. [L1] Did You deploy an application through ArgoCD ?
2. [L2] Did You write ArgoCD Application manifests and sync policies ?
3. [L3] Did You set up ArgoCD from scratch and structure a GitOps repository ?
4. [L3] Did You use ApplicationSets, app of apps or sync waves / hooks ?
5. [L4] Did You design GitOps promotion between multiple environments or clusters ?

### JavaScript
- Category: language
- Tier: core for frontend
- Aliases: JS, ECMAScript, ES6, vanilla JS
- Related: TypeScript, Node.js
1. [L1] Did You write JavaScript for a web page (DOM, events, fetch) ?
2. [L1] Did You use modern syntax (modules, arrow functions, destructuring, classes) ?
3. [L2] Did You use async / await and Promises in a real project ?
4. [L2] Did You debug JavaScript and network requests in browser dev tools ?
5. [L2] Did You configure a bundler or build tool (Vite, Webpack, esbuild) ?
6. [L3] Can You explain a bug caused by closures, `this` binding or the event loop, and did You fix one ?
7. [L3] Did You write a reusable JavaScript module or package used by others ?
8. [L4] Did You optimise bundle size or load performance (code splitting, lazy loading) ?
9. [L4] Did You migrate a JavaScript codebase to TypeScript or to a new framework ?

### Ruby on Rails
- Category: framework
- Tier: core for backend
- Aliases: Ruby, Rails, RoR
- Related: Django, Laravel
1. [L1] Did You create a Rails application with models, controllers and views ?
2. [L1] Did You use Rails generators, routes and the Rails console ?
3. [L2] Did You use ActiveRecord associations, migrations and validations in a real project ?
4. [L2] Did You write tests with RSpec or Minitest ?
5. [L3] Did You run a Rails application in production for real users ?
6. [L3] Did You write or fork a Ruby gem ?
7. [L3] Did You use background jobs (Sidekiq, ActiveJob) in production ?
8. [L4] Did You optimise Rails performance (N+1, caching, background jobs) ?
9. [L4] Did You upgrade a Rails application across major versions ?

### Camunda
- Category: workflow engine
- Tier: adjacent
- Aliases: Camunda BPM, Camunda 7, Camunda 8, Zeebe, BPMN
- Related: Flowable, Activiti, jBPM
1. [L1] Did You model or read BPMN processes ?
2. [L2] Did You implement service tasks / external task workers or Java delegates ?
3. [L3] Did You debug stuck process instances, incidents or failed jobs in production ?
4. [L3] Did You integrate Camunda into a Spring Boot application or extend the engine ?
5. [L4] Did You design a platform or reusable components on top of Camunda ?

### ActiveMQ / Artemis
- Category: messaging
- Tier: adjacent
- Aliases: ActiveMQ, Artemis, ArtemisMQ, JMS, IBM MQ
- Related: RabbitMQ, Kafka
1. [L1] Did You send and receive JMS messages ?
2. [L2] Did You configure queues, topics and listeners in a Spring application ?
3. [L3] Did You handle redelivery, dead letter queues and transactions ?
4. [L4] Did You configure or operate the broker (clustering, persistence, HA) ?

### HashiCorp Vault
- Category: security
- Tier: adjacent
- Aliases: Vault, secrets management, Infisical, AWS Secrets Manager
- Related: Kubernetes, Terraform
1. [L1] Did You read secrets from Vault in an application or pipeline ?
2. [L2] Did You configure secret engines, paths and policies ?
3. [L3] Did You integrate Vault with Kubernetes (injector, CSI, External Secrets) ?
4. [L4] Did You run Vault in production (unsealing, HA, dynamic secrets, PKI) ?

### Keycloak
- Category: security
- Tier: adjacent
- Aliases: Red Hat SSO, OIDC provider, IAM
- Related: Spring Security, OAuth2
1. [L1] Did You integrate an application with Keycloak login ?
2. [L2] Did You configure realms, clients, roles and mappers ?
3. [L3] Did You configure identity brokering, federation (LDAP / AD) or custom flows ?
4. [L4] Did You run Keycloak in production or write Keycloak extensions / themes ?

### Elasticsearch
- Category: database
- Tier: adjacent
- Aliases: Elastic, OpenSearch, ELK
- Related: Observability, MongoDB
1. [L1] Did You query Elasticsearch or search data in Kibana ?
2. [L2] Did You index documents and write search queries from an application ?
3. [L3] Did You design mappings, analyzers or aggregations ?
4. [L4] Did You operate a cluster (shards, replicas, index lifecycle) ?

### Maven / Gradle
- Category: build tool
- Tier: adjacent
- Aliases: Maven, Gradle
- Related: CI/CD
1. [L1] Did You build a project and add dependencies with Maven or Gradle ?
2. [L2] Did You work with a multi-module project ?
3. [L3] Did You configure plugins, profiles and dependency conflict resolution ?
4. [L4] Did You write own plugin or set up company parent POM / convention plugins ?

### Android
- Category: mobile
- Tier: adjacent
- Aliases: Android SDK, Jetpack, Jetpack Compose
- Related: Kotlin, Java
1. [L1] Did You create an Android application ?
2. [L2] Did You publish an app or have real users using it ?
3. [L3] Did You use background work, notifications or lifecycle-aware components ?
4. [L4] Did You design architecture of a larger Android app (MVVM, DI, modularization) ?

### SOAP
- Category: integration
- Tier: adjacent
- Aliases: SOAP, WSDL, XML web services, JAX-WS, NDC
- Related: REST API design
1. [L1] Did You call a SOAP service ?
2. [L2] Did You generate clients from WSDL / XSD and map XML messages ?
3. [L3] Did You implement integration against a complex external XML specification ?
4. [L4] Did You design a SOAP or XML based interface for external partners ?

### Event-driven architecture
- Category: architecture
- Tier: adjacent
- Aliases: EDA, event-driven, event sourcing, CQRS, asynchronous messaging
- Related: Kafka, RabbitMQ, ActiveMQ / Artemis, Microservices
1. [L1] Did You work on a system where services communicate through events or messages ?
2. [L2] Did You implement publishing and consuming of domain events between services ?
3. [L3] Did You handle eventual consistency, idempotent consumers or outbox pattern ?
4. [L4] Did You design event flows / event contracts for multiple services or use event sourcing / CQRS ?

### AI coding assistants
- Category: tooling
- Tier: adjacent
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
- Tier: adjacent
- Aliases: architectural thinking, solution design, system design, architecture design, ADR
- Related: Microservices, Event-driven architecture, REST API design
1. [L1] Did You follow an existing architecture (layers, modules) and can explain why it is structured that way ?
2. [L2] Did You propose structure for a new feature or module that was accepted by the team ?
3. [L3] Did You design a new service or application from scratch (structure, persistence, integrations) and run it in production ?
4. [L3] Did You write ADRs or lead technical discussions about trade-offs and maintainability ?
5. [L4] Did You set technical direction or a modernization plan for a whole system or several teams ?

### Regulated domain
- Category: domain
- Tier: adjacent
- Aliases: fintech, banking, payments, insurance, public sector, regulated environment, PSD2, PSD3
- Related: -
1. [L1] Did You work on a project where audits, compliance or strict release processes were required ?
2. [L2] Did You work in a regulated environment (public sector, insurance, healthcare, energy) ?
3. [L3] Did You work on a production project for a bank, payments or fintech company ?
4. [L4] Did You implement regulatory requirements yourself (PSD2 / PSD3, AML, KYC, strong customer authentication) ?

### Apache Camel
- Category: integration
- Tier: adjacent
- Aliases: Camel, Camel K, Camel Quarkus, Red Hat Fuse
- Related: Spring Integration, MuleSoft, ActiveMQ / Artemis
1. [L1] Did You write Camel routes in a tutorial, side project or small task ?
2. [L2] Did You use Camel routes in production with components (Kafka, HTTP, file, JMS) ?
3. [L3] Did You handle redelivery, dead letter channel or EIPs (split, aggregate, content-based router) in production ?
4. [L4] Did You design an integration platform on Camel or write own Camel components ?

### Design patterns / clean code
- Category: practice
- Tier: adjacent
- Aliases: design patterns, clean code, SOLID, GoF, refactoring
- Related: Software architecture
1. [L1] Can You explain common design patterns (strategy, factory, builder, adapter) and SOLID ?
2. [L2] Did You use design patterns deliberately in production code ?
3. [L3] Did You refactor legacy code to clean code / SOLID, with tests ?
4. [L3] Did You regularly point out design / clean code problems in code review ?
5. [L4] Did You define coding standards or architecture rules for the team ?

### Jira / Confluence
- Category: tooling
- Tier: adjacent
- Aliases: Jira, Confluence, Atlassian, YouTrack
- Related: -
1. [L1] Did You work with tickets, boards and sprints in Jira ?
2. [L2] Did You write or maintain technical documentation in Confluence ?
3. [L3] Did You configure Jira workflows, boards or automation for the team ?

### Google Cloud
- Category: cloud
- Tier: core for devops
- Aliases: GCP, Google Cloud Platform, GKE, Cloud Run
- Related: AWS, Azure
1. [L1] Did You deploy something to GCP ?
2. [L1] Did You use Cloud Console and gcloud CLI ?
3. [L2] Did You use GCP managed services (Cloud Run, GKE, Cloud SQL, Pub/Sub) in a real project ?
4. [L2] Did You read logs and metrics in Cloud Logging / Cloud Monitoring ?
5. [L3] Did You set up IAM, networking or cost monitoring in GCP ?
6. [L3] Did You use service accounts and Workload Identity for applications ?
7. [L3] Did You manage GCP resources as code (Terraform) ?
8. [L4] Did You design multi-environment GCP infrastructure (projects, IaC, landing zone) ?
9. [L4] Did You plan disaster recovery or optimise costs on GCP ?

### Git
- Category: tooling
- Tier: adjacent
- Aliases: GitHub, GitLab, Bitbucket, version control
- Related: SVN
1. [L1] Did You commit, push and pull in Git daily ?
2. [L2] Did You resolve merge conflicts and work with feature branches and pull requests ?
3. [L3] Did You use rebase, cherry-pick, bisect or rewrite history safely ?
4. [L4] Did You define branching strategy or migrate repositories for the team ?

### Microsoft SQL Server
- Category: database
- Tier: adjacent
- Aliases: MSSQL, SQL Server, T-SQL, Azure SQL
- Related: SQL, PostgreSQL, Oracle
1. [L1] Did You use SQL Server as an application database ?
2. [L2] Did You write T-SQL queries, stored procedures or migrations for SQL Server ?
3. [L3] Did You analyse execution plans or indexes in SQL Server ?
4. [L4] Did You configure SQL Server high availability, replication or performance tuning ?

### Networking
- Category: operations
- Tier: core for devops
- Aliases: network, TCP/IP, DNS, TLS, firewall, load balancer
- Related: Bash / Linux, Kubernetes
1. [L1] Do You understand IP, DNS, ports and HTTP / TLS and use curl, ping, nslookup ?
2. [L1] Did You read HTTP requests and responses (headers, status codes) in browser tools or curl ?
3. [L2] Did You debug firewall, DNS, proxy or certificate problems between services ?
4. [L2] Did You diagnose PKI / TLS problems (expired or untrusted certificate, wrong chain, truststore) ?
5. [L2] Did You inspect connections with tcpdump, Wireshark, netstat or ss ?
6. [L3] Did You configure load balancers, ingress, VPN, network policies or subnets ?
7. [L3] Did You set up TLS certificates with automatic renewal (cert-manager, Let's Encrypt) ?
8. [L4] Did You design network topology or segmentation for a system ?
9. [L4] Did You design zero trust access, mTLS or service mesh networking ?

### Application servers
- Category: operations
- Tier: adjacent
- Aliases: Tomcat, WebLogic, WildFly, JBoss, WebSphere, Apache httpd, Nginx, web server
- Related: Docker, Bash / Linux
1. [L1] Did You deploy an application to Tomcat or another application server ?
2. [L2] Did You configure Apache httpd or Nginx (virtual hosts, reverse proxy) ?
3. [L2] Did You deploy or administer applications on WebLogic, WildFly or WebSphere ?
4. [L3] Did You tune or troubleshoot an application server in production (threads, memory, connection pools) ?

### Windows Server / Active Directory
- Category: operations
- Tier: adjacent
- Aliases: Windows Server, AD, Active Directory, GPO, Entra ID
- Related: Microsoft 365
1. [L1] Did You create users, groups, reset passwords or manage permissions in Active Directory ?
2. [L2] Did You install or maintain Windows Server, its roles and updates ?
3. [L3] Did You configure group policies, domain join or DNS / DHCP on Windows ?
4. [L4] Did You design AD structure or hybrid identity (AD + Entra ID) for a company ?

### Microsoft 365 / IT support
- Category: operations
- Tier: adjacent
- Aliases: M365, Office 365, Exchange Online, Teams admin, helpdesk, user support
- Related: Windows Server / Active Directory
1. [L1] Did You solve PC, printer, phone or access problems for colleagues ?
2. [L2] Did You manage M365 users, licenses, mailboxes or Teams ?
3. [L3] Did You set up device management (Intune) or conditional access ?

### PowerShell
- Category: language
- Tier: adjacent
- Aliases: PowerShell, pwsh
- Related: Bash / Linux
1. [L1] Did You run or modify PowerShell scripts ?
2. [L2] Did You write PowerShell scripts for admin tasks used by others ?
3. [L3] Did You write PowerShell modules or automate AD / M365 with PowerShell ?

### Security / compliance
- Category: security
- Tier: adjacent
- Aliases: NIS2, ISO 27001, GDPR, endpoint protection, EDR, Bitdefender, firewall, patch management
- Related: Networking, Bash / Linux
1. [L1] Did You patch servers or manage access rights ?
2. [L2] Did You manage antivirus / EDR or firewall rules ?
3. [L3] Did You take part in a security audit or compliance project (ISO 27001, NIS2, GDPR) ?
4. [L4] Did You lead security compliance or define security policies for a company ?

### ML / LLM fundamentals
- Category: AI
- Tier: adjacent
- Aliases: machine learning, LLM, RAG, embeddings, AI evaluation, MLOps
- Related: AI coding assistants, Python
1. [L1] Can You explain LLM basics: tokens, context window, embeddings, temperature, hallucinations ?
2. [L1] Do You understand ML basics: training vs inference, overfitting, train / test split ?
3. [L2] Did You call an LLM API from code or build RAG / an agent (hobby counts) ?
4. [L3] Did You evaluate AI outputs against a test set or criteria and iterate on prompts or models ?
5. [L4] Did You train, fine-tune or deploy an ML model to production ?

### Stakeholder communication
- Category: soft skill
- Tier: adjacent
- Aliases: client communication, requirements clarification, working with business users
- Related: -
1. [L1] Did You take part in meetings or calls with clients or business users ?
2. [L2] Did You clarify requirements directly with clients or business users ?
3. [L3] Did You regularly present results or explain technical decisions to non-developers ?

### Oracle DB
- Category: database
- Tier: adjacent
- Aliases: Oracle, Oracle Database, PL/SQL
- Related: SQL, PostgreSQL, Microsoft SQL Server
1. [L1] Did You query an Oracle database ?
2. [L2] Did You use Oracle as an application database in a real project ?
3. [L3] Did You write PL/SQL procedures or analyse execution plans in Oracle ?
4. [L4] Did You tune Oracle performance, partitioning or RAC / Data Guard ?

### Load testing
- Category: practice
- Tier: adjacent
- Aliases: Gatling, k6, JMeter, Locust, performance testing
- Related: Testing
1. [L1] Did You run an existing load test ?
2. [L2] Did You write load tests with Gatling, k6, JMeter or similar ?
3. [L3] Did You find and fix a performance bottleneck based on load test results ?
4. [L4] Did You define performance requirements and a load testing strategy for a system ?

### Java EE / J2EE
- Category: framework
- Tier: core for backend
- Aliases: J2EE, Java EE, Jakarta EE, Servlets, JSP, Struts, JSF, EJB
- Related: Spring Boot, Application servers
1. [L1] Did You write Servlets or JSP pages ?
2. [L1] Did You read and change web.xml or other deployment descriptors ?
3. [L2] Did You maintain a Java EE web application in production (Servlets / JSP, Struts or JSF) ?
4. [L2] Did You fix bugs in a legacy Struts, JSF or JSP application ?
5. [L3] Did You work with EJB, JPA, JMS or CDI on an application server (WebLogic, WildFly, WebSphere) ?
6. [L3] Did You configure datasources, JNDI or security realms on an application server ?
7. [L4] Did You migrate a Java EE / Struts application to Spring Boot or newer Jakarta EE ?
8. [L4] Did You design module structure (EAR, WAR, shared libraries) of a large Java EE application ?

### XML / XSLT
- Category: data format
- Tier: adjacent
- Aliases: XML, XSLT, XSD, XPath, JAXB
- Related: SOAP
1. [L1] Did You parse or generate XML in an application ?
2. [L2] Did You write XSD schemas or XSLT transformations ?
3. [L3] Did You maintain complex XSLT / XML processing in production ?

### Google Workspace
- Category: tooling
- Tier: adjacent
- Aliases: G Suite, Google Admin, Google Drive, Gmail admin
- Related: Microsoft 365 / IT support
1. [L1] Did You manage sharing and permissions in Google Drive for a team ?
2. [L2] Did You administer Google Workspace users, groups and settings ?
3. [L3] Did You set up Google Workspace for an organization (domain, security policies, migration) ?

### No-code automation
- Category: integration
- Tier: adjacent
- Aliases: Make, Integromat, Zapier, n8n, Power Automate
- Related: REST API design
1. [L1] Did You build a simple automation in Make, Zapier or n8n ?
2. [L2] Did You run automations used by others in an organization ?
3. [L3] Did You integrate several apps with error handling and monitoring of the scenarios ?

### UX research
- Category: design
- Tier: adjacent
- Aliases: UX, usability testing, user research, information architecture
- Related: -
1. [L1] Did You collect feedback from users of an application ?
2. [L2] Did You do user research or usability testing and change the product based on it ?
3. [L3] Did You design information structure or user flows for a product ?

### API testing tools
- Category: tooling
- Tier: adjacent
- Aliases: Postman, SoapUI, Bruno, Insomnia, REST Client
- Related: REST API design, SOAP
1. [L1] Did You send requests to an API with Postman, SoapUI, Bruno or similar ?
2. [L2] Did You build shared collections with environments, variables or auth flows ?
3. [L3] Did You automate API tests (Newman, SoapUI test suites) in CI ?

### UML
- Category: architecture
- Tier: adjacent
- Aliases: UML, sequence diagram, Enterprise Architect, PlantUML
- Related: Software architecture
1. [L1] Did You read UML or sequence diagrams in specifications ?
2. [L2] Did You draw sequence or component diagrams for a design ?
3. [L3] Did You maintain a model in Enterprise Architect or similar for a team ?

### Salesforce
- Category: platform
- Tier: adjacent
- Aliases: Salesforce, SFDC, Apex, SOQL, Lightning
- Related: REST API design
1. [L1] Did You configure objects, fields or flows in a Salesforce org ?
2. [L2] Did You call Salesforce REST, Bulk or Metadata API from an application ?
3. [L3] Did You write Apex code or SOQL queries in production ?
4. [L4] Did You build a product or managed package on top of Salesforce ?

### DLT / blockchain
- Category: domain
- Tier: adjacent
- Aliases: distributed ledger, Hyperledger Besu, Ethereum, smart contracts
- Related: -
1. [L1] Do You understand DLT principles (ledger, nodes, consensus, smart contracts) ?
2. [L2] Did You run or deploy a blockchain node (Hyperledger Besu, Ethereum client) ?
3. [L3] Did You write or deploy smart contracts ?
4. [L4] Did You design a private DLT network (permissioning, consensus choice, node topology) ?

### SonarQube
- Category: code quality
- Tier: adjacent
- Aliases: SonarCloud, SonarLint, static code analysis
- Related: -
1. [L1] Did You work in a project where SonarQube analysed the code ?
2. [L2] Did You fix issues reported by SonarQube ?
3. [L3] Did You set up SonarQube in CI (quality gates, rules) ?
4. [L4] Did You define code quality rules or gates for a team or organisation ?

### IntelliJ IDEA
- Category: tooling
- Tier: adjacent
- Aliases: IntelliJ, IDEA, JetBrains IDE
- Related: Eclipse, VS Code
1. [L1] Do You use IntelliJ IDEA for editing and running code ?
2. [L2] Do You use its debugger and built-in refactorings ?
3. [L3] Do You work efficiently with shortcuts, plugins, run configurations, database / HTTP tools ?
4. [L4] Did You write IntelliJ plugins or set up shared IDE configuration for a team ?

### Mobile Device Management
- Category: operations
- Tier: adjacent
- Aliases: MDM, SOTI MobiControl, Microsoft Intune, Android Enterprise, Workspace ONE, Jamf
- Related: Microsoft 365 / IT support
1. [L1] Did You work in an MDM console (device lookup, remote commands, logs) ?
2. [L2] Did You configure policies, profiles or enrollment for managed devices ?
3. [L3] Did You troubleshoot device fleet problems (failed enrollment, app deployment, rugged devices) ?
4. [L4] Did You design MDM architecture or integrate MDM with other systems (APIs, reporting) ?

### GraphQL
- Category: API
- Tier: adjacent
- Aliases: Apollo, graphql-java, DGS
- Related: REST API design
1. [L1] Did You call a GraphQL API as a client ?
2. [L2] Did You build a GraphQL API (schema, resolvers) ?
3. [L3] Did You solve N+1 / batching (DataLoader) or pagination in GraphQL ?
4. [L4] Did You design a GraphQL schema for multiple clients or federation ?

### BigQuery
- Category: database
- Tier: adjacent
- Aliases: Google BigQuery, GCP data warehouse
- Related: SQL, Google Cloud
1. [L1] Did You run queries in BigQuery ?
2. [L2] Did You load or stream data into BigQuery from an application ?
3. [L3] Did You optimise cost / partitioning of BigQuery tables ?

### Ansible
- Category: infrastructure as code
- Tier: core for devops
- Aliases: Ansible playbooks, AWX, Ansible Tower
- Related: Terraform, Bash / Linux
1. [L1] Did You run Ansible playbooks in a project ?
2. [L1] Did You use inventories and ad hoc commands ?
3. [L2] Did You write or maintain playbooks / roles for deployments ?
4. [L2] Did You use Jinja2 templates, handlers and variables ?
5. [L3] Did You structure inventories, roles and vaults for multiple environments ?
6. [L3] Did You make playbooks idempotent and test them (check mode, Molecule) ?
7. [L4] Did You design configuration management for a whole organisation ?
8. [L4] Did You write own Ansible modules or collections ?

### ETL / data modeling
- Category: data
- Tier: adjacent
- Aliases: data pipelines, ETL, ELT, data modelling, Airflow, Spark
- Related: SQL, Kafka
1. [L1] Did You design DB schemas / data models ?
2. [L2] Did You build ETL / data pipelines between systems ?
3. [L3] Did You handle incremental loads, data quality checks or reprocessing ?
4. [L4] Did You design data platform or warehouse model (star schema, data vault) ?

### SAST
- Category: security
- Tier: adjacent
- Aliases: Fortify, Checkmarx, Snyk Code, Semgrep, static application security testing
- Related: SonarQube, Security / compliance
1. [L1] Did You fix issues reported by Fortify, Checkmarx or similar ?
2. [L2] Did You add a SAST scan to a CI pipeline ?
3. [L3] Did You tune rules, triage false positives or define security gates ?

### Node.js
- Category: runtime
- Tier: core for backend
- Aliases: Node, NodeJS, Express, NestJS, Fastify
- Related: JavaScript, TypeScript
1. [L1] Did You write a Node.js script or small service ?
2. [L1] Did You manage dependencies with npm, yarn or pnpm ?
3. [L2] Did You build Node.js backend in production ?
4. [L2] Did You use async / await and Promises with proper error handling in a service ?
5. [L3] Did You use a large framework (Express, NestJS) with auth, validation and tests ?
6. [L3] Did You connect Node.js to a database with ORM or query builder (Prisma, TypeORM, Knex) ?
7. [L3] Did You run Node.js in production with logging, graceful shutdown and process management ?
8. [L4] Did You debug Node.js performance (event loop, memory) in production ?
9. [L4] Did You use worker threads, streams or clustering for heavy load ?

### Go
- Category: language
- Tier: core for backend
- Aliases: Golang
- Related: Java, C
1. [L1] Did You write a Go program or small service ?
2. [L1] Did You use Go modules, structs, interfaces and explicit error handling ?
3. [L2] Did You build Go backend or CLI in production ?
4. [L2] Did You write table driven tests in Go ?
5. [L2] Did You build an HTTP service with net/http or a framework (Gin, Echo, chi) ?
6. [L3] Did You use goroutines and channels for concurrent processing in production ?
7. [L3] Did You use context for cancellation and timeouts across a service ?
8. [L4] Did You profile and tune Go services (pprof, GC, memory) ?
9. [L4] Did You write a Kubernetes operator, controller or larger Go library ?

### Consul
- Category: service discovery
- Tier: adjacent
- Aliases: HashiCorp Consul, service discovery, service mesh
- Related: Kubernetes, HashiCorp Vault
1. [L1] Did You register services or read config / service discovery from Consul ?
2. [L2] Did You use Consul KV or health checks in an application (Spring Cloud Consul) ?
3. [L3] Did You set up Consul agents / cluster or Consul Connect service mesh ?
4. [L4] Did You operate Consul in production (ACLs, multi datacenter, upgrades) ?

### HAProxy
- Category: load balancer
- Tier: adjacent
- Aliases: load balancer, reverse proxy
- Related: Application servers (Nginx), Networking
1. [L1] Did You work with a system behind HAProxy and read its logs / stats ?
2. [L2] Did You write HAProxy configuration (frontends, backends, health checks, TLS) ?
3. [L3] Did You troubleshoot HAProxy in production (timeouts, sticky sessions, failover) ?
4. [L4] Did You design HA load balancing (keepalived / VRRP, zero downtime reloads) ?

### SharePoint
- Category: platform
- Tier: adjacent
- Aliases: SharePoint Online, SPFx, SharePoint Framework, OneDrive
- Related: Microsoft 365 / IT support
1. [L1] Did You work with SharePoint sites, lists and document libraries ?
2. [L2] Did You configure sites, permissions or Power Automate flows on SharePoint ?
3. [L3] Did You integrate an application with SharePoint (Graph API, REST) or build SPFx web parts ?
4. [L4] Did You design information architecture or migrate content for a whole organisation ?

### Backstage
- Category: developer portal
- Tier: adjacent
- Aliases: Spotify Backstage, developer portal, internal developer platform, IDP
- Related: CI/CD, Kubernetes
1. [L1] Did You use Backstage to find services, docs or owners ?
2. [L2] Did You register components with catalog-info.yaml or write TechDocs ?
3. [L3] Did You write software templates (scaffolder) or configure plugins ?
4. [L4] Did You run Backstage for an organisation or write own plugins ?
