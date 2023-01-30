# Notas Clase Terraform 28/01/2023

## _Clase 28/01/2023_


## Continous Integration (CI) & Continuous Delivery (CD)

Existen 2 modelos de CICD

**Git Flow**

<p align="center">
<img src="https://miro.medium.com/max/1400/1*9yJY7fyscWFUVRqnx0BM6A.png" width=500px>
</p>

<br>

**GitHub Flow**
<p align="center">
<img src="https://devopedia.org/images/article/403/9163.1645614913.png" width=500px>
</p>


<br>

## Terraform

Es un software para poder ejecutar en cualquier Cloud ficheros que levanten y pongan en marcha aplicaciones que desarrollamos en local.

Terraform siempre es conciente de en que estado está la nube que has programado, y cuando hagas un cambio en el archvio .yml de Terraform, el se encarga de hacer los cambios en el Cloud automáticamente.

Ejemplo codigo archivo .tf para Google Cloud

```sh
provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
}

terraform {
    backend "gcs" {
        bucket = <bucket_id>
        prefix = "terraform/state"
    }
}
```

En Terraform hay 4 pasos:

- Init: crea las librearías necesarias para ejecutar en cada Cloud provider
- Plan: hace un primer test para saber si hay algún fallo o no
- Apply: ejecuta la creación de comandos que le hayamos dicho
- Destroy: destruye la aplicación





