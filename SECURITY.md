# Security Policy

## Supported Versions

Security fixes are currently provided for the latest version of the `main` branch.

| Version | Supported |
| ------- | --------- |
| `main`  | ✅         |

## Reporting a Vulnerability

Please **do not report security vulnerabilities through public GitHub issues**.

For security-related issues, contact the repository maintainer privately with:

* A clear description of the vulnerability.
* Steps to reproduce the issue.
* Potential security impact.
* Relevant logs, screenshots, or proof-of-concept details.
* Any suggested mitigation, if available.

Please allow reasonable time for the issue to be investigated before publicly disclosing the vulnerability.

## Security Considerations

This project is a reference implementation and should be reviewed and hardened before production deployment.

Production deployments should consider:

* Authentication and authorization.
* TLS/mTLS for network communication.
* Rate limiting and abuse protection.
* Secure secrets management.
* Audit logging and monitoring.
* Least-privilege IAM and access controls.
* Dependency vulnerability scanning.
* Container image scanning.
* Secure configuration management.
* Regular security updates.

## Responsible Disclosure

We appreciate responsible disclosure of security vulnerabilities.

Please avoid accessing, modifying, deleting, or exposing data that does not belong to you while investigating a potential vulnerability.

## Scope

Security concerns may include:

* Authentication or authorization bypasses.
* Sensitive information exposure.
* Injection vulnerabilities.
* Insecure API behavior.
* Dependency vulnerabilities affecting the project.
* Container or deployment security issues.
* Improper handling of secrets or credentials.

Thank you for helping keep the project secure.
