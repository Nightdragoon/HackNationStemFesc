from fastapi import FastAPI
from sqlalchemy import create_engine , Select , Insert
from sqlalchemy.ext.automap import automap_base
from UsuarioInsertar import UsuarioInsertar
from UsuarioBuscar import UsuarioBuscar
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import Orchestrator

engine = create_engine("mysql+pymysql://upiw3mqa58obep4h:VMqMoO6MuFgXjBt6ddl@b96lcxztraqbollhfyj6-mysql.services.clever-cloud.com:20670/b96lcxztraqbollhfyj6")

Base = automap_base()

# Reflect the database schema and prepare the base
Base.prepare(autoload_with=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini_api = ""
stmt = Select(Base.classes.APIS).where(Base.classes.APIS.nombre == "gemini")
with engine.connect() as connection:
    result = connection.execute(stmt)
    for row in result:
        gemini_api = row._data[2]


@app.post("/registrarUsuario")
async  def insertarUsuario(usuario: UsuarioInsertar):
    try:
        insertion = Insert(Base.classes.Usuarios).values(nombre=usuario.nombre, contrasena=usuario.contrasena)
        with engine.connect() as connection:
            connection.execute(insertion)
            connection.commit()
        return {"isSuccess": True}
    except Exception as e:
        return {"isSuccess": False , "message": str(e)}


@app.post("/loginUsuario")
async def loginUsuario(usuario: UsuarioInsertar):
    try:
        buscar = Select(Base.classes.Usuarios).where(Base.classes.Usuarios.nombre == usuario.nombre , Base.classes.Usuarios.contrasena == usuario.contrasena)
        with engine.connect() as connection:
            result = connection.execute(buscar)
            for row in result:
                if row != None:
                    return UsuarioBuscar(True , "usuario logeado" , True , row._data[0])

        return UsuarioBuscar(True, "usuario no encontrado", False , 0)
    except Exception as e:
        return {"isSuccess": False , "message": str(e)}






@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

