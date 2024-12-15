# Authentification

## ...
- Open Network: No password is required; you connect immediately.
- Secured Network: You need to enter a password or use other authentication methods such as:
  - WEP: Now considered as vulnerable. See [documentation](../Cryptography/WEP/README.md).
  - WPA/WPA2 Password: Common in most home and office networks. See [documentation](../Cryptography/WPA/README.md).
  - WPA3: More secure modern standard.
  - Enterprise Authentication: Requires credentials like a username and password or a certificate.

```mermaid

sequenceDiagram
    participant Device
    participant Router

    Router->>Device: Broadcasts SSID (Network Name)
    Device->>Router: Sends an association request (selects SSID)
    Router->>Device: Sends a challenge (specifies authentication type)
    Device->>Router: Encrypts challenge with password or certificate (based on security type)
    Router->>Device: Successful authentication (Connection established)

```

## Simulation

```mermaid

sequenceDiagram
    participant Device
    participant Router

    Device->>Router: Sends an association request (specifies IP, PORT and authentication type)
    Router->>Device: Sends a challenge 
    Device->>Router: Encrypts challenge with password 
    Router->>Device: Successful authentication (Connection established)

```