# Threat Model - Secure Movie Service

## Overview

This document identifies potential security threats to the Secure Movie Service microservice and outlines mitigation strategies. The goal is to anticipate attack vectors, understand risks, and design controls to minimize impact.

---

## 1. Assets

- Movie data fetched and stored/processed by the service
- API endpoints and underlying infrastructure
- User data (if any authentication is implemented)
- Deployment environment and container images
- Source code repository and CI/CD pipeline

---

## 2. Entry Points

- HTTP API endpoints exposed by FastAPI
- GitHub repository (code, workflow files)
- Docker container registry (for images)
- Deployment and hosting environment (e.g., cloud provider)

---

## 3. Threat Actors

- External attackers aiming to exploit vulnerabilities or disrupt service
- Malicious insiders with access to code or deployment environments
- Automated bots attempting abuse (scraping, brute force)
- Supply chain attackers targeting dependencies or CI/CD pipelines

---

## 4. Threats and Risks

| Threat                                    | Description                                                       | Impact                           | Likelihood | Mitigation                                                      |
|-------------------------------------------|-------------------------------------------------------------------|---------------------------------|------------|----------------------------------------------------------------|
| Injection Attacks                         | SQL/command injection via unvalidated inputs                      | Data theft, corruption          | Medium     | Input validation, use ORM, static code analysis (CodeQL)       |
| Unauthorized Access                       | Accessing APIs or resources without proper authentication         | Data leak, privilege escalation | Medium     | Use authentication/authorization, secure secrets management    |
| Dependency Vulnerabilities                | Malicious or vulnerable third-party libraries                     | Remote code execution, breaches | Medium     | Regular dependency scanning (Bandit, Trivy), pinned versions   |
| Container/Image Vulnerabilities           | Vulnerabilities in base images or container misconfigurations     | Container escape, data leaks    | Low        | Use minimal base images, scan images, run non-root             |
| CI/CD Pipeline Compromise                 | Unauthorized code injection or malicious workflow modifications    | Supply chain attacks            | Low        | Protect branches, code reviews, secure secrets in workflows    |
| Denial of Service (DoS)                    | Excessive requests exhausting resources                           | Service unavailability          | Medium     | Rate limiting (future enhancement), resource limits            |
| Information Disclosure                     | Logging sensitive data or verbose error messages                  | Leak of credentials or data     | Low        | Sanitized logging, error handling best practices                |
| Man-in-the-Middle (MitM) Attack            | Intercepting data in transit                                      | Data tampering, leakage         | Medium     | Use HTTPS / TLS in deployment environment                       |

---

## 5. Attack Surface Summary

- Public HTTP API endpoints
- Docker image build and deployment process
- Source code repository with workflow files
- External dependencies and package managers

---

## 6. Security Controls Mapping

| Threat                             | Controls Implemented                                           |
|-----------------------------------|---------------------------------------------------------------|
| Injection Attacks                 | Input validation, static analysis (CodeQL), safe coding       |
| Unauthorized Access               | Secrets management, authentication (planned), non-root users  |
| Dependency Vulnerabilities        | Bandit and Trivy scanning, pinned dependencies                |
| Container/Image Vulnerabilities   | Multi-stage Docker build, image scanning, minimal base images |
| CI/CD Pipeline Compromise         | Branch protections, code review, GitHub Actions security      |
| DoS                              | Planned rate limiting, container resource limits              |
| Information Disclosure             | Sanitized logging, error handling                              |
| MitM                             | Use of HTTPS / TLS in deployment                               |

---

## 7. Summary

The Secure Movie Service has a focused threat model that addresses the typical risks for a microservice with publicly exposed API endpoints and CI/CD pipelines. Ongoing improvements such as authentication, rate limiting, and encrypted transport will further enhance security posture.

---

*Document last updated:* 2025-06-19
