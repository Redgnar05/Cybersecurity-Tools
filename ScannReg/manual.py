


def user_manual():
    manual = """
==== MANUAL DE USUARIO ====

1. Reconocimiento Rápido (Fast Recon):
   - Comando: nmap -T4 -F <objetivo>
   - Escanea solo los puertos más comunes de manera rápida.

2. Detección Completa de Puertos (Full Port Scan):
   - Comando: nmap -p- -sS -T4 <objetivo>
   - Escanea TODOS los puertos TCP usando un escaneo SYN (semiabierto).

3. Enumeración Detallada (Service + OS Detection):
   - Comando: nmap -sS -sV -O -A -T4 <objetivo>
   - Obtiene información de servicios, versiones y sistema operativo.

4. Escaneo de UDP (Servicios en UDP):
   - Comando: nmap -sU -p 53,161,123,69 -T4 <objetivo>
   - Busca servicios importantes que usen el protocolo UDP.

5. Escaneo Silencioso (Stealth / Bypass IDS):
   - Comando: nmap -sS -T0 -Pn --data-length=50 <objetivo>
   - Evade sistemas de detección de intrusos enviando tráfico lento y disfrazado.

6. Escaneo con Scripts NSE (Vulnerabilidad Específica):
   - Comando: nmap --script vuln <objetivo>
   - Usa scripts automáticos para encontrar vulnerabilidades conocidas.

============================
"""
    print(manual)




