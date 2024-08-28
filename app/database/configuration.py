#Datos para la conexion BD

dataBaseName="gestordb"
userName="root"
userPassword=None
connnectionPort=3306
server="localhost"

# Creando la base de datos
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connnectionPort}/{dataBaseName}"

print(dataBaseConnection)