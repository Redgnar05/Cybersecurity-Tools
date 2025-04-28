


import nmap
from manual import user_manual

def display_results(nm):
    for host in nm.all_hosts():
        print(f"\n[+] Resultados para: {host}")
        print(f"Estado: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port].get('name', 'desconocido')
                print(f"  Puerto {port}: {state} ({service})")

def fast_recon(nm, target):
    nm.scan(hosts=target, arguments="-T4 -F")
    display_results(nm)

def full_port_scan(nm, target):
    nm.scan(hosts=target, arguments="-p- -sS -T4")
    display_results(nm)

def detailed_enumeration(nm, target):
    nm.scan(hosts=target, arguments="-sS -sV -O -A -T4")
    display_results(nm)

def udp_scan(nm, target):
    nm.scan(hosts=target, arguments="-sU -p 53,161,123,69 -T4")
    display_results(nm)

def stealth_scan(nm, target):
    nm.scan(hosts=target, arguments="-sS -T0 -Pn --data-length=50")
    display_results(nm)

def nse_vuln_scan(nm, target):
    nm.scan(hosts=target, arguments="--script vuln")
    display_results(nm)

def menu():
    nm = nmap.PortScanner()

    print("\n=== Menú de Opciones - Escaneo Nmap ===")
    print("1. Reconocimiento Rápido (Fast Recon)")
    print("2. Detección Completa de Puertos (Full Port Scan)")
    print("3. Enumeración Detallada (Service + OS Detection)")
    print("4. Escaneo de UDP (Servicios en UDP)")
    print("5. Escaneo Silencioso (Stealth / Bypass IDS)")
    print("6. Escaneo con Scripts NSE (Vulnerabilidad Específica)")
    print("7. Manual de usuario")

    try:
        choice = int(input("\nSelecciona una opción (1-7): "))
    except ValueError:
        print("\nPor favor ingresa un número válido.")
        return

    if choice != 7:
        target = input("\nIntroduce la IP o dominio objetivo: ")

    match choice:
        case 1:
            fast_recon(nm, target)
        case 2:
            full_port_scan(nm, target)
        case 3:
            detailed_enumeration(nm, target)
        case 4:
            udp_scan(nm, target)
        case 5:
            stealth_scan(nm, target)
        case 6:
            nse_vuln_scan(nm, target)
        case 7:
            user_manual()
        case _:
            print("\nOpción inválida. Por favor elige entre 1 y 7.")







