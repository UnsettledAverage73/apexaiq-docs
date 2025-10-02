# Virtual Environments & Pip

Managing project dependencies and ensuring consistent development environments are crucial in Python. Virtual environments and `pip` are the primary tools for achieving this.

## Pip: Python's Package Installer

`pip` is the standard package-management system used to install and manage software packages written in Python. Many packages are hosted on the Python Package Index (PyPI).

### Basic `pip` Commands

*   **Install a package:**
    ```bash
    pip install package_name
    ```
    Example: `pip install requests`

*   **Install a specific version:**
    ```bash
    pip install package_name==1.2.3
    ```

*   **Upgrade a package:**
    ```bash
    pip install --upgrade package_name
    ```

*   **Uninstall a package:**
    ```bash
    pip uninstall package_name
    ```

*   **List installed packages:**
    ```bash
    pip list
    ```

*   **Show package details:**
    ```bash
    pip show package_name
    ```

*   **Create a `requirements.txt` file:**
    This file lists all the dependencies for your project and their exact versions.
    ```bash
    pip freeze > requirements.txt
    ```

*   **Install packages from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

## Virtual Environments

A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to manage dependencies for different projects separately, preventing conflicts.

### Why Use Virtual Environments?

*   **Dependency Isolation**: Each project can have its own set of dependencies without interfering with other projects or the global Python installation.
*   **Reproducibility**: You can easily recreate the exact environment of a project on another machine using `requirements.txt`.
*   **Cleanliness**: Keeps your global Python environment clean.

### Creating a Virtual Environment

Python 3 comes with the `venv` module, which is the recommended way to create virtual environments.

1.  **Navigate to your project directory:**
    ```bash
    cd my_project_folder
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv  # 'venv' is the common name for the environment folder
    ```
    (On some systems, you might use `python -m venv venv` if `python` defaults to Python 3).

### Activating a Virtual Environment

Before installing packages for your project, you must activate the virtual environment.

*   **On Linux/macOS:**
    ```bash
    source venv/bin/activate
    ```

*   **On Windows (Command Prompt):**
    ```cmd
    venv\Scripts\activate.bat
    ```

*   **On Windows (PowerShell):**
    ```powershell
    venv\Scripts\Activate.ps1
    ```

Once activated, your terminal prompt will typically show the name of the active virtual environment (e.g., `(venv) your_username@your_machine:~/my_project_folder$`).

Any `pip install` commands run now will install packages into this isolated environment.

### Deactivating a Virtual Environment

To exit the virtual environment and return to your global Python environment, simply type:

```bash
deactivate
```

### Deleting a Virtual Environment

To remove a virtual environment, simply delete its directory:

```bash
rm -rf venv
```
(On Windows, you might use `rmdir /s /q venv` in Command Prompt or `Remove-Item -Recurse -Force venv` in PowerShell).
