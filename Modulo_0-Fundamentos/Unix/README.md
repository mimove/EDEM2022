# NOTAS SOBRE UNIX


## Uso de WSL en Visual Studio Code

Cuando se quiera utilizar WSL con VS Code hay que seguir los siguientes pasos:

1. Install WSL Ubuntu: https://ubuntu.com/wsl

2. Search History in Ubuntu : You have to uncomment two lines in ```/etc/inputrc``` or add these two lines to your ```$HOME/.inputrc``` file (https://unix.stackexchange.com/questions/5366/command-line-completion-from-command-history): 

    ```sh
    "\e[5~": history-search-backward 
    "\e[6~": history-search-forward
    ```

3. Set Default ubuntu running this command in PowerShell:

    ```bash
    wsl -s Ubuntu
    ```

4. Install python extension in VS code for WSL: Ubuntu

5. Install docker extension in VS code for WSL: Ubuntu


<br>

## Cambios en Windows PowerShell

1. Instalar VIM en local: https://www.w3schools.io/editor/vim-install/. Importante marcar opción de añadir a directorio .bat para poder usar el comando vi desde linea de comandos


2. Quitar proteccion perfil: https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system

    ```bash
    Set-ExecutionPolicy RemoteSigned
    ```


3. Crear perfil de bash-like y comandos para recorrer bash_history: https://dev.to/ofhouse/add-a-bash-like-autocomplete-to-your-powershell-4257

    3.1 Crear Perfil de Powershell ejecutando:

    ```bash
    # Create profile when not exist
    if (!(Test-Path -Path $PROFILE.CurrentUserAllHosts)) {
    New-Item -ItemType File -Path $PROFILE.CurrentUserAllHosts -Force
    }

    # Open the profile with an editor (e.g. good old Notepad)
    ii $PROFILE.CurrentUserAllHosts
    ```

    3.2 Abrir editor y añadir las siguientes líneas:

    ```bash
    # Shows navigable menu of all options when hitting Tab
    Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete

    # Autocompletion for arrow keys
    Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
    Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
    ```


    ## Actualizar VS Code si da problemas

    Seguir los pasos del siguiente enlace:

    <https://stackoverflow.com/questions/64743231/vs-code-failed-to-install-visual-studio-code-update>