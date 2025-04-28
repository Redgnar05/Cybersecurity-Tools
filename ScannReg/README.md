# ScannReg

![ScannReg Banner](#)

**ScannReg** es una herramienta de escaneo de redes modular e interactiva basada en Python y Nmap, pensada para profesionales de ciberseguridad, pentesters, administradores de sistemas y entusiastas del hacking ético.

---

## 📊 Descripción

ScannReg permite realizar diferentes tipos de escaneos de red de forma automática y estructurada usando Nmap. Proporciona una interfaz en consola fácil de usar, resultados procesados y un manual de usuario incorporado que explica cada operación.

---

## 🔍 Características Principales

- **Menú Interactivo:** Selecciona el tipo de escaneo que desees realizar.
- **Tipos de Escaneo Disponibles:**
  - Reconocimiento rápido (Fast Recon).
  - Detección completa de puertos TCP (Full Port Scan).
  - Enumeración detallada de servicios y sistemas operativos.
  - Escaneo de servicios UDP.
  - Escaneo sigiloso para evadir IDS/IPS.
  - Escaneo de vulnerabilidades mediante scripts NSE.
- **Resultados organizados:**
  - Estado de los hosts.
  - Protocolos detectados (TCP/UDP).
  - Puertos abiertos/cerrados y servicios identificados.
- **Manual de usuario integrado:** Explica las banderas utilizadas en Nmap.
- **Banner ASCII personalizado:** Estética visual para una experiencia de usuario mejorada.
- **Modularidad:** Código dividido en varios archivos para fácil mantenimiento y escalabilidad.

---

## 🚿 Instalación

### Requisitos

- Python 3.10 o superior.
- Nmap instalado y disponible en el sistema.
- Librerías Python necesarias:

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:
```text
python-nmap
pyfiglet
termcolor
```

### Instalación de Nmap

- Descarga desde: [https://nmap.org/download.html](https://nmap.org/download.html)
- Verifica la instalación ejecutando en consola:
```bash
nmap --version
```

---

## 🌍 Uso

1. Ejecuta el programa principal:

```bash
python main.py
```

2. Visualiza el banner "ScannReg".
3. Selecciona una opción del menú (1-7).
4. Ingresa el objetivo (IP o dominio).
5. Observa los resultados estructurados directamente en tu terminal.


### Estructura de archivos:
```
/ScannReg
|
|├— main.py          # Punto de entrada del programa
|├— scanner.py       # Módulo de funciones de escaneo y menú
|├— manual.py        # Texto del manual de usuario
|├— banner.py        # Código para mostrar el banner ASCII
|└— requirements.txt # Librerías requeridas
```

---

## 🔢 Tecnologías Usadas
- **Python 3.10+**
- **Nmap** (Network Mapper)
- **python-nmap** (wrapper de Nmap en Python)
- **pyfiglet** (ASCII Art)
- **termcolor** (Colores en consola)

---

## ⚡ Futuras Mejoras
- Exportación de resultados a archivos `.json` o `.txt`.
- Escaneo de múltiples objetivos a la vez.
- Creación de perfiles de escaneo personalizados.
- Automatización de reportes de vulnerabilidades.
- Integración con GUI o API web.

---

## 🚀 Contribución

Sientete libre de proponer mejoras, reportar errores o contribuir directamente a este proyecto.

---

## 🛍þï Licencia

Proyecto educativo y libre para fines de aprendizaje, éticos y de seguridad informática responsable. ¡Usar siempre con autorización del propietario de la red!

---

© ScannReg - 2025


