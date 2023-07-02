import subprocess

# Comando para crear el entorno virtual
create_env_command = 'python3 -m venv env'

# Comando para activar el entorno virtual
activate_env_command = 'source env/bin/activate'

# Ejecutar el comando para crear el entorno virtual
subprocess.run(create_env_command, shell=True, check=True)

# Ejecutar el comando para activar el entorno virtual
subprocess.run(activate_env_command, shell=True, check=True)
