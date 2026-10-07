# PCI DSS Standard Reference

## Overview
Payment Card Industry Data Security Standard (PCI DSS) v4.0 requirements and compliance checklist.

## PCI DSS v4.0 Requirements Overview

### Requirement 1: Install and maintain network security controls

**1.1 - Network Security Policy**
- [ ] Network security policy established
- [ ] Policy reviewed annually and updated
- [ ] Policy communicated to all personnel

**1.2 - Network Security Configuration**
- [ ] Default passwords changed on all systems
- [ ] Default security parameters changed
- [ ] Unused services disabled
- [ ] Strong cryptography for passwords

**1.3 - Secure Network Connections**
- [ ] Network segmentation implemented
- [ ] Wireless networks secured
- [ ] VPN for remote access
- [ ] VPN authentication and encryption

**1.4 - Firewalls**
- [ ] Firewall configuration reviewed every 6 months
- [ ] Firewall rules documented
- [ ] Unnecessary services blocked
- [ ] Direct internet access prohibited for cardholder systems

**1.5 - Wireless Networks**
- [ ] Wireless networks scanned quarterly
- [ ] Wireless authentication required
- [ ] Wireless encryption (WPA2+)
- [ ] Wireless infrastructure outside cardholder data environment

**1.6 - Mobile Device Security**
- [ ] Mobile device security policy
- [ ] Mobile device inventory
- [ ] Mobile device management implemented
- [ ] Remote wipe capability

### Requirement 2: Apply secure configurations to all system components

**2.1 - Process and Procedures**
- [ ] Configuration standards documented
- [ ] Process for secure configuration
- [ ] Configuration verification
- [ ] Configuration management

**2.2 - Vendor Defaults**
- [ ] All vendor defaults changed
- [ ] Default accounts removed or disabled
- [ ] Default passwords removed
- [ ] Default security parameters modified

**2.3 - System Hardening**
- [ ] System hardening procedures
- [ ] Unnecessary services disabled
- [ ] System components hardened according to standards
- [ ] Secure protocols only (SSHv2, TLS 1.2+)

**2.4 - Shared Systems**
- [ ] Shared hosting risks assessed
- [ ] Shared hosting only if cardholder data environment isolated
- [ ] Separate cardholder data environment

**2.5 - Configuration Maintenance**
- [ ] Configuration changes documented
- [ ] Change control process
- [ ] Testing before deployment
- [ ] Impact analysis

### Requirement 3: Protect stored account data

**3.1 - Keep Cardholder Data to a Minimum**
- [ ] Data retention policy defined
- [ ] Data retention policy communicated
- [ ] Data disposal process
- [ ] Verification of data disposal
- [ ] Storage retention reviewed quarterly

**3.2 - Encryption of Stored Cardholder Data**
- [ ] Full track data not stored
- [ ] Card verification codes not stored
- [ ] Sensitive authentication data not stored after authorization
- [ ] PAN displayed masked (showing no more than first six/last four digits)
- [ ] PAN rendered unreadable (hashed, truncated, indexed)
- [ ] Cryptographic keys managed securely

**3.3 - Primary Account Number (PAN) Protection**
- [ ] Display of PAN restricted
- [ ] Unmasked PAN not displayed
- [ ] Access to unmasked PAN restricted
- [ ] Encryption keys stored securely
- [ ] Secure key storage devices

**3.4 - Encryption Key Management**
- [ ] Key generation process documented
- [ ] Secure key distribution
- [ ] Secure key storage
- [ ] Key rotation schedule
- [ ] Key decommissioning process
- [ ] Dual control for key management
- [ ] Split knowledge for key management
- [ ] Key backup procedures

**3.5 - Cryptographic Keys**
- [ ] Keys managed in compliance with standards
- [ ] Key management processes documented
- [ ] Key custodians identified
- [ ] Key access restrictions
- [ ] Key compromise procedures

### Requirement 4: Protect cardholder data in transit

**4.1 - Encryption of Cardholder Data in Transit**
- [ ] Strong cryptography and security protocols (TLS 1.2+)
- [ ] Only trusted certificates and keys
- [ ] Trusted keys/certificates maintained
- [ ] Protocol supported by system and client
- [ ] Secure connections only

**4.2 - Network Security Controls**
- [ ] Sensitive data transmitted only over secure channels
- [ ] Never sent over insecure protocols (HTTP, FTP, telnet)
- [ ] Network security controls prevent interception
- [ ] Wireless transmissions encrypted
- [ ] End-to-end encryption for wireless communications

**4.3 - Encryption Key Management**
- [ ] Cryptographic keys used for encryption in transit managed securely
- [ ] Key generation and distribution secure
- [ ] Key storage secure
- [ ] Key rotation per industry standards

### Requirement 5: Protect all systems and networks from malicious software

**5.1 - Anti-Virus Software**
- [ ] Anti-virus software deployed on all systems
- [ ] Anti-virus updated regularly
- [ ] Regular anti-virus scans
- [ ] Anti-virus software active at all times
- [ ] Anti-virus protection maintained

**5.2 - Malicious Software Protection**
- [ ] Systems protected against malicious software
- [ ] Protection mechanisms up-to-date
- [ ] Regular scans for malicious software
- [ ] Malicious software detection and prevention

**5.3 - Anti-Malware Processes**
- [ ] Anti-malware processes and procedures
- [ ] Malicious software response procedures
- [ ] Malware incident management
- [ ] Post-malware incident review

**5.4 - Malicious Software Awareness**
- [ ] User awareness training for malicious software
- [ ] Phishing awareness
- [ ] Social engineering awareness
- [ ] Security awareness training

### Requirement 6: Develop and maintain secure systems and applications

**6.1 - Security Development Lifecycle**
- [ ] Secure development lifecycle process
- [ ] Secure coding practices
- [ ] Application security training
- [ ] Security requirements included in development

**6.2 - Security Testing**
- [ ] Regular security testing of applications
- [ ] Vulnerability scanning
- [ ] Penetration testing
- [ ] Testing after significant changes

**6.3 - Secure Authentication**
- [ ] Multi-factor authentication implemented
- [ ] Strong authentication for remote access
- [ ] Encryption for authentication over open networks

**6.4 - Input Validation**
- [ ] Input validation on all data
- [ ] Output validation
- [ ] Data sanitization
- [ ] SQL injection prevention
- [ ] XSS prevention

**6.5 - Secure Coding Practices**
- [ ] Code reviews
- [ ] Secure coding standards
- [ ] Error handling without information disclosure
- [ ] Parameterized queries

**6.6 - Software Updates**
- [ ] Security patches applied promptly
- [ ] Software updates according to vendor schedule
- [ ] Critical security patches within 1 month
- [ ] Vulnerability monitoring

**6.7 - Development and Test Environments**
- [ ] Development/test environments separate from production
- [ ] Test data masked or obfuscated
- [ ] Production data not used for testing
- [ ] Access controls for development environments

### Requirement 7: Restrict access to system components and cardholder data

**7.1 - Access Control Policy**
- [ ] Access control policy established
- [ ] Policy reviewed annually
- [ ] Principle of least privilege
- [ ] Need-to-know basis

**7.2 - User Identification and Authentication**
- [ ] Unique user ID for each person
- [ ] Multi-factor authentication for remote access
- [ ] Strong password policies
- [ ] Password change at first login
- [ ] Temporary passwords changed at first use
- [ ] Lockout after failed attempts
- [ ] Session timeouts

**7.3 - Access Rights**
- [ ] Access granted based on business need
- [ ] Access rights documented
- [ ] Regular access reviews (quarterly)
- [ ] Access rights removed when no longer needed

**7.4 - System Administrators**
- [ ] Separate accounts for administrative duties
- [ ] Administrator authentication required
- [ ] Root/admin access controlled
- [ ] Use of personal accounts for administration prohibited

**7.5 - In-House and Third-Party Personnel**
- [ ] Background checks for personnel with cardholder data access
- [ ] Personnel screened before access granted
- [ ] Background check policy documented
- [ ] Contractual obligations for third parties

**7.6 - Personnel Termination**
- [ ] Access revoked immediately upon termination
- [ ] Personnel termination procedures
- [ ] Inventory of all access items returned
- [ ] Logical and physical access removed

**7.7 - Access Revocation**
- [ ] Access revoked when no longer needed
- [ ] Revocation process documented
- [ ] Regular access review
- [ ] Access log review

### Requirement 8: Identify users and authenticate access to system components

**8.1 - Authentication Mechanisms**
- [ ] Authentication mechanisms for all users
- [ ] Strong authentication (MFA for remote access)
- [ ] Password complexity requirements
- [ ] Password change frequency
- [ ] Password history requirements
- [ ] Password hashing/encryption

**8.2 - Multi-Factor Authentication**
- [ ] MFA implemented for all access to cardholder data
- [ ] MFA implemented for remote network access
- [ ] MFA for administrative access
- [ ] MFA factors independent (something you have, know, are)

**8.3 - Password Management**
- [ ] Passwords never shared
- [ ] Passwords never written down
- [ ] Passwords not in scripts or code
- [ ] Passwords rotated periodically
- [ ] Forced password changes
- [ ] Default passwords never used

**8.4 - Identification and Authentication**
- [ ] Users uniquely identified
- [ ] Identification and authentication mechanisms
- [ ] Authenticated sessions monitored
- [ ] Session timeout configured

**8.5 - Security Policy**
- [ ] Authentication security policy
- [ ] Policy communicated to all users
- [ ] Policy acceptance confirmation
- [ ] Regular security awareness training

### Requirement 9: Restrict physical access to cardholder data

**9.1 - Physical Access Control**
- [ ] Physical access control policy
- [ ] Physical access restricted to authorized personnel
- [ ] Access logs maintained
- [ ] Access badges/keys controlled
- [ ] Visitor management

**9.2 - Media Handling**
- [ ] Secure media storage
- [ ] Media transport secured
- [ ] Media destruction procedures
- [ ] Media inventory maintained
- [ ] Hard drive destruction/cryptographic erase

**9.3 - Physical Security**
- [ ] Physical barriers and fences
- [ ] Security cameras and monitoring
- [ ] Alarm systems
- [ ] Security guards (if applicable)
- [ ] Security lighting

**9.4 - Visitors**
- [ ] Visitor authorization process
- [ ] Visitor escorts
- [ ] Visitor badges/IDs
- [ ] Visitor log

**9.5 - Media Destruction**
- [ ] Secure media destruction
- [ ] Destruction process documented
- [ ] Destruction verified
- [ ] Certificates of destruction maintained

**9.6 - Equipment Maintenance**
- [ ] Equipment maintenance procedures
- [ ] Maintenance personnel authorization
- [ ] Supervision of maintenance
- [ ] Media removal before maintenance

### Requirement 10: Log and monitor access to system components and cardholder data

**10.1 - Audit Trails**
- [ ] Audit trail for all system components
- [ ] Audit logs capture user identification
- [ ] Audit logs capture event type
- [ ] Audit logs capture date and time
- [ ] Audit logs capture success/failure
- [ ] Audit logs capture source of event

**10.2 - Log Review**
- [ ] Regular review of logs
- [ ] Security event detection
- [ ] Daily review of critical systems
- [ ] Weekly review of other systems
- [ ] Retention of audit logs (at least 1 year, 3 months available)

**10.3 - Log Protection**
- [ ] Logs protected from tampering
- [ ] Log backup and storage
- [ ] Immediate review of log failures
- [ ] Log integrity verification

**10.4 - Synchronization**
- [ ] Time synchronization across systems
- [ ] NTP servers used
- [ ] Time drift monitoring

### Requirement 11: Test security systems and processes regularly

**11.1 - Wireless Network Testing**
- [ ] Quarterly wireless network scans
- [ ] Wireless access point testing
- [ ] Unauthorized wireless device detection
- [ ] Wireless security testing tools

**11.2 - Vulnerability Scanning**
- [ ] Quarterly external vulnerability scans
- [ ] Quarterly internal vulnerability scans
- [ ] Annual penetration testing by ASV
- [ ] Scanning after significant changes
- [ ] Remediation of vulnerabilities

**11.3 - Penetration Testing**
- [ ] Annual internal penetration testing
- [ ] Annual external penetration testing
- [ ] Testing by qualified internal resources or third party
- [ ] Network and application layer testing
- [ ] Testing of segmentation and scope
- [ ] Remediation of identified vulnerabilities

**11.4 - Intrusion Detection Systems**
- [ ] IDS/IPS monitoring
- [ ] Intrusion detection logs reviewed daily
- [ ] Security event alerts
- [ ] Incident response procedures

**11.5 - Incident Response Plan**
- [ ] Incident response plan documented
- [ ] Incident response team identified
- [ ] Response procedures defined
- [ ] Notification procedures
- [ ] Post-incident review

**11.6 - Regular Testing**
- [ ] Regular testing of security systems
- [ ] Testing of security controls
- [ ] Testing of detection systems
- [ ] Testing of incident response

### Requirement 12: Support information security with organizational policies and programs

**12.1 - Security Policy**
- [ ] Information security policy established
- [ ] Policy reviewed annually
- [ ] Policy communicated to all personnel
- [ ] Security awareness training
- [ ] Policy acknowledgment by personnel

**12.2 - Risk Management**
- [ ] Risk assessment process
- [ ] Risk assessment performed annually
- [ ] Risk management program
- [ ] Risk remediation tracking

**12.3 - Security Incidents**
- [ ] Incident response procedures
- [ ] Incident escalation procedures
- [ ] Incident notification procedures
- [ ] Incident documentation
- [ ] Post-incident analysis

**12.4 - Security Awareness Training**
- [ ] Security awareness program
- [ ] Training upon hire
- [ ] Regular training updates
- [ ] Security incident reporting training

**12.5 - Third-Party Service Providers**
- [ ] Due diligence for third parties
- [ ] Contracts with security requirements
- [ ] Monitoring of third-party compliance
- [ ] Annual verification of third-party compliance

## Evidence Collection

### Required Evidence Types

**Policies and Procedures**
- [ ] Information security policy
- [ ] Network security policy
- [ ] Access control policy
- [ ] Incident response plan
- [ ] Change management process
- [ ] Risk assessment procedures

**Configuration Documentation**
- [ ] Firewall configurations
- [ ] Router configurations
- [ ] System configurations
- [ ] Security control configurations
- [ ] Encryption configurations

**Monitoring and Logging**
- [ ] Firewall logs
- [ ] System logs
- [ ] Application logs
- [ ] Access logs
- [ ] Monitoring reports

**Testing Evidence**
- [ ] Vulnerability scan reports
- [ ] Penetration test reports
- [ ] Wireless scan reports
- [ ] Security control test results
- [ ] Remediation verification

**Training Evidence**
- [ ] Training materials
- [ ] Training attendance records
- [ ] Training assessments
- [ ] Security awareness programs

## Audit Preparation

### Pre-Audit Checklist

**Documentation**
- [ ] All policies reviewed and updated
- [ ] All procedures documented
- [ ] Evidence collected and organized
- [ ] Gap analysis completed
- [ ] Remediation of gaps

**Internal Assessment**
- [ ] Internal audit conducted
- [ ] Self-Assessment Questionnaire (SAQ) completed
- [ ] Remediation of findings
- [ ] Re-assessment after remediation

**Staff Preparation**
- [ ] Staff trained on PCI DSS requirements
- [ ] Interview preparation conducted
- [ ] Point of contact identified
- [ ] Staff awareness of audit

**System Preparation**
- [ ] Evidence collection systems verified
- [ ] Monitoring systems verified
- [ ] Documentation repositories organized
- [ ] Access controls reviewed

## Scoping

### System Scope Identification

**In-Scope Systems**
- [ ] Systems that process cardholder data
- [ ] Systems that transmit cardholder data
- [ ] Systems that store cardholder data
- [ ] Systems that provide security for above

**Out-of-Scope Systems**
- [ ] Systems that do not process cardholder data
- [ ] Systems with network segmentation
- [ ] Systems with no access to cardholder data
- [ ] Systems that meet exclusion criteria

### Documentation Required

**Network Diagram**
- [ ] Current network diagram
- [ ] Data flow diagram
- [ ] System connections documented
- [ ] Out-of-scope systems identified

**Data Flow**
- [ ] Cardholder data entry points
- [ ] Cardholder data storage points
- [ ] Cardholder data transmission paths
- [ ] Cardholder data exit points

## References

- [PCI SSC Standards](https://www.pcisecuritystandards.org/)
- [PCI DSS v4.0](https://www.pcisecuritystandards.org/documents/PCI-DSS-v4_0.pdf)
- [PCI SAQ Instructions](https://www.pcisecuritystandards.org/documents/PCI-DSS-v4_0-SAQ-Instructions.pdf)
- [ASV Program Guide](https://www.pcisecuritystandards.org/documents/ASV-Program-Guide-v1.0.2.pdf)
