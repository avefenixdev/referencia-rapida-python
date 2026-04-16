# Referencia rápida Python

## Extensiones Visual Studio Code

1. Python (ms-python.python)
2. Symbols (miguelsolorio.symbols)
3. Better Comments (aaron-bond.better-comments)
4. Scepter Theme (IsaacWilson.scepter)
5. Error Lens (usernamehw.errorlens)

# Variables

## Reglas básicas para los nombres de las variables

Nombres claros y en **snake_case**

* Comienza con letra
* Sin espacios
* Sin símbolos raros
* Nombre descriptivo 

# Trabajando con virtual environment (Entornos virtuales)

* Tiene sus propias dependencias
* Usa versiones controladas
* No rompe otros proyectos
* Se puede desplegar facilmente y sin errores

## Crear entorno virtual

```sh
python -m venv <nombre-entorno>
python -m venv ref-fast-py # ejemplo | se crea una carpeta llamada 'ref-fast-py'
```

## Activar entorno

> Windows

```sh
<nombre-entorno>\Scripts\activate
ref-fast-py\Scripts\activate # ejemplo
```
> Linux / Mac

```sh
source <nombre-entorno>/bin/activate
source ref-fast-py/bin/activate # ejemplo
```

## Instalar dependencias 
Para instalar dependencias se utilizar *pip* que es el gestor de paquetes de Python.

**IMPORTANTE:** Controlar que estoy en un entorno activo 

```sh
pip install <dependencias>
pip install numpy # ejemplo | última versión de numpy
pip install requests==2.25.1 # ejemplo | versión específica de requests
```

## Listar dependencias instaladas

```sh
pip list
```

## Desinstalar dependencias

```sh
pip uninstall <dependencias>
pip uninstall numpy # ejemplo | desinstala la dependencia numpy
```

## Guardar dependencias con requirements.txt

```sh
pip freeze > requirements.txt
```

## Recuperar dependencias vía requirement.txt

```sh
pip install -r requirements.txt
```

## Revisar integridad y si las dependencias están actualizadas

```sh
pip check
```

## Actualizar dependencias

```sh
pip install --upgrade -r requirements.txt
```

# Incorporando a un proyecto el .editorconfig
Es fundamental para mantener un estilo de código estandar entre todo el equipo de desarrollo. Puede gestionar:

* Identación
* Espacios
* Codificación

1. Crear el archivo *.editorconfig* en la raíz del proyecto

2. Copiar lo siguiente en el archivo

> Ejemplo base basado en las convenciones de Python (PEP 8)

```ini
# EditorConfig root
root = true

# Ajustes para archivos Python
[*.py]
indent_style = space
indent_size = 4
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
end_of_line = lf
```

3. Instalar la extensión de Visual Studio Code
La extensión lee el archivo y configura el editor.

    * EditorConfig (EditorConfig.EditorConfig)

# Repositorio oficial y centralizado de Python
Podemos encontrar bibliotecas, herramientas y módulos (paquetes) instalables.

<https://pypi.org/>