# Guía de Migración de VM por USB y Asignación de IP por Grupo

Este documento describe cómo trasladar una máquina virtual de **Oracle VM VirtualBox** (como `ubts_w2`) desde un equipo origen a los puestos de trabajo del aula mediante un pendrive USB **conservando intacta su instantánea (`BASELINE – BEFORE WORKSHOP`)**, así como los pasos para asignar una dirección IP estática única a cada grupo de trabajo.

---

## 1. Exportar la Máquina Virtual desde el PC Origen al Pendrive USB

> **Importante:** No utilices la opción *Archivo → Exportar servicio virtualizado* (`.ova` / `.ovf`), ya que VirtualBox fusiona los discos y **elimina las instantáneas**. Copia siempre la carpeta completa de la VM.

### Requisitos previos
1. **Pendrive USB formateado en `exFAT` o `NTFS`:** Los archivos de disco virtual (`.vdi`) superan los 4 GB, por lo que un pendrive en `FAT32` fallará durante la copia.
2. **Máquina virtual completamente apagada:** Asegúrate de que la VM no esté en ejecución ni en estado guardado.

### Comandos en Windows (CMD)
*(Ejemplo asumiendo la VM en `F:\VMs\ubts_w2` y el pendrive en `D:`)*

1. **Verificar la ruta exacta de la máquina virtual y apagarla:**
   ```cmd
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" showvminfo "ubts_w2" | findstr /I "Config file"
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm "ubts_w2" poweroff
   ```
2. **Comprobar el sistema de archivos del pendrive USB (`D:`):**
   ```cmd
   fsutil fsinfo volumeinfo D:\
   ```
   *(Si indica `FAT32` y el pendrive está vacío, formatéalo a `exFAT` antes de copiar: `format D: /FS:exFAT /Q /V:W2_LAB`).*
3. **Copiar la carpeta completa de la VM (incluyendo `.vbox`, `.vdi` y la subcarpeta `Snapshots/`):**
   ```cmd
   robocopy "F:\VMs\ubts_w2" "D:\ubts_w2" /E /R:2 /W:2
   ```
4. **Verificar la copia en el pendrive:**
   ```cmd
   dir "D:\ubts_w2"
   dir "D:\ubts_w2\Snapshots"
   ```

---

## 2. Importar y Registrar la Máquina Virtual en el Equipo Destino (`VB_dir`)

No ejecutes la máquina virtual directamente desde el pendrive USB; cópiala primero al almacenamiento local del equipo anfitrión.

### Opción A: En Windows (CMD)
*(Asumiendo el pendrive en `D:\ubts_w2` y el directorio local de VirtualBox en `C:\VMs\ubts_w2`)*

1. **Copiar la carpeta completa al disco local:**
   ```cmd
   robocopy "D:\ubts_w2" "C:\VMs\ubts_w2" /E /R:2 /W:2
   ```
2. **Registrar la máquina virtual en VirtualBox (mantiene sus instantáneas):**
   ```cmd
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" registervm "C:\VMs\ubts_w2\ubts_w2.vbox"
   ```
3. **Verificar el registro de la VM y su instantánea base:**
   ```cmd
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" list vms
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" snapshot "ubts_w2" list
   ```
4. **Configurar el adaptador de red Solo-Anfitrión (`192.168.56.1/24`) y arrancar:**
   ```cmd
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" hostonlyif create
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" hostonlyif ipconfig "VirtualBox Host-Only Ethernet Adapter" --ip 192.168.56.1 --netmask 255.255.255.0
   "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "ubts_w2" --type headless
   ```

### Opción B: En Ubuntu (Terminal Bash)
*(Asumiendo el pendrive montado en `/media/$USER/W2_LAB/ubts_w2` y el destino local en `~/VirtualBox VMs/ubts_w2`)*

1. **Comprobar el punto de montaje del pendrive USB:**
   ```bash
   lsblk -o NAME,LABEL,MOUNTPOINT
   ```
2. **Copiar la carpeta completa al directorio local de VirtualBox:**
   ```bash
   mkdir -p ~/"VirtualBox VMs"
   cp -rv "/media/$USER/W2_LAB/ubts_w2" ~/"VirtualBox VMs/"
   ```
3. **Registrar la máquina virtual en VirtualBox:**
   ```bash
   VBoxManage registervm "$HOME/VirtualBox VMs/ubts_w2/ubts_w2.vbox"
   ```
4. **Verificar el registro de la VM y su instantánea base:**
   ```bash
   VBoxManage list vms && VBoxManage snapshot "ubts_w2" list
   ```
5. **Configurar el adaptador Solo-Anfitrión (`vboxnet0` en `192.168.56.1/24`), vincularlo a `NIC 2` y arrancar:**
   ```bash
   VBoxManage hostonlyif create
   VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1 --netmask 255.255.255.0
   VBoxManage modifyvm "ubts_w2" --hostonlyadapter2 vboxnet0
   VBoxManage startvm "ubts_w2" --type headless
   ```

---

## 3. Asignación de IP Estática Única por Grupo (Netplan)

Cuando se despliega la misma imagen base en varios equipos del aula, cada grupo debe configurar su propia dirección IP estática en la interfaz Solo-Anfitrión (`enp0s8`, por ejemplo `192.168.56.101`, `.102`, `.103`...) para evitar colisiones de red. Los servicios (`ssh`, `nginx`, `webmin`) y `ufw` escuchan en todas las interfaces (`0.0.0.0`), por lo que no requieren cambios adicionales.

1. **Iniciar sesión en la VM y localizar el archivo YAML de Netplan:**
   ```bash
   ls /etc/netplan/
   ```
2. **Editar la dirección IPv4 de `enp0s8` en el archivo correspondiente** (por ejemplo, `00-installer-config.yaml` o `50-cloud-init.yaml`):
   ```bash
   sudo nano /etc/netplan/00-installer-config.yaml
   ```
   Sustituye `192.168.56.102/24` por la IP asignada al grupo (manteniendo `enp0s3` con `dhcp4: true`).
3. **Aplicar y verificar la nueva dirección IP:**
   ```bash
   sudo netplan apply && ip -br -4 addr
   ```
4. **Actualizar la instantánea limpia del grupo:**
   Apaga la VM (`sudo poweroff`) y actualiza la instantánea `BASELINE – BEFORE WORKSHOP` en el equipo del grupo para que cualquier restauración posterior conserve su IP asignada.