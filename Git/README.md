# NOTAS GIT

<br>

## Configuración utilizando WSL2 en Visual Studio Code

<br>


El uso de git se realiza desde el Windows Subsystem for Linux (WSL2) dentro de Visual Studio Code. Para ello, hay que resolver primero un fallo dentro del WSL que no permite conectarse a direcciones https por defecto. Para ello se han seguido los siguientes pasos (https://stackoverflow.com/questions/55649015/could-not-resolve-host-github-com-only-in-windows-bash):

 1. Cambiar el archivo /etc/wsl.conf con los siguiente:

    ```sh
    [network]
    generateResolvConf = false
    ```

2. Modificar (o crear si no existe) el archivo /etc/resolv.conf con lo siguiente:

    ```sh
    nameserver 1.1.1.1
    ```
    Es **muy importante** que solo aparezca esa linea en el archivo, ya que si no da problemas.



<br>
<br>

## Comandos para control de repositorios desde la terminal de WSL2

<br>

### Configuración previa

Para configurar Git y tener acceso a tu repositorio, hay que configurar primero la cuenta. Los comandos a ejecutar son:

```bash
git config --global user.name "your_username"

git config --global user.email "your_email_address@example.com"
```

<br>


### Gestión del repositorio

Lo primero es hacer un clonado del repositorio a algún directorio dentro de ~/home. Para ello hay que ejecutar la siguiente línea de comando:

```bash
git clone <url of repository>.git
```


Una vez que tenemos el repositorio clonado, podemos abrirlo en VS Code y empezar a modificar, crear o eliminar tanto archivos como carpetas. Los cambios serán automáticamente detectados, y cambiará el color del archivo/directorio. Aparecerá una M y color naranja para archivos modificados, una U y color verde para archivos creados que todavía no están en el repositorio remoto, y archivos tachados y en color rojo para los que han sido eliminados


Los siguientes comandos son los que hay que utilizar para la sincronización del repositorio local con el repositorio en GitHub (https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html):

1. Es necesario hacer un pull para asegurarse de que no hay cambios en GitHub:

    ```bash
    git pull <REMOTE> <name-of-branch>
    ```
    Ejemplo con mi repositorio:

    ```bash
    git pull origin draft
    ```

<br>

2. Para crear una rama usar: 

    ```bash
    git checkout -b <name-of-branch>
    ```

<br>

3. Para cambiar de rama:

    ```bash
    git checkout <name-of-branch>
    ```




