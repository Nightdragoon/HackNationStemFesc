from fastapi import FastAPI , BackgroundTasks
from sqlalchemy import create_engine, Select, Insert, except_ , desc
from sqlalchemy.ext.automap import automap_base
from UsuarioInsertar import UsuarioInsertar
from UsuarioBuscar import UsuarioBuscar
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import Orchestrator
from RespuestaConversacionActual import RespuestaConversacionActual
from HistorialInstancias import HistorialInstancia

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


@app.get("/desarrolloConversacion")
async def desarrolloConversacion(id: int):
    try:

        getDesarrollo = Select(Base.classes.conversacion).where(Base.classes.conversacion.idConversacion == id
                                                                    ).order_by(desc(Base.classes.conversacion.id))
        res = RespuestaConversacionActual()
        with engine.connect() as connection3:
            rows = connection3.execute(getDesarrollo).mappings().all()
            rows += [{}] * max(0, 4 - len(rows))
            res.emma = (rows[0].get("mensajeAgente") or "")
            res.esve = (rows[1].get("mensajeAgente") or "")
            res.rodri = (rows[2].get("mensajeAgente") or "")
            res.brandon = (rows[3].get("mensajeAgente") or "")
        res.isSuccess = True
        return res

    except Exception as e:
        return {"isSuccess": False, "error": str(e)}

@app.get("/conversation")
async def conversation(topic: str , id: int , background_tasks: BackgroundTasks ):
   try:
       # generar la instancia
       id_instancia = ""
       insertarInstancia = Insert(Base.classes.Instancia).values(nombreConversacion=topic, idUsuario=id)
       encontrarInstancia = Select(Base.classes.Instancia).where(Base.classes.Instancia.nombreConversacion == topic,
                                                                 Base.classes.Instancia.idUsuario == id)
       with engine.connect() as connection:
           connection.execute(insertarInstancia)
           connection.commit()
       with engine.connect() as connection2:
           result = connection2.execute(encontrarInstancia)
           for row in result:
               id_instancia = row._data[0]

       orchestrator = Orchestrator(gemini_api, engine, Base, id_instancia)
       background_tasks.add_task(
           orchestrator.run_discussion,topic


       )

       return {"isSuccess": True , "id": id_instancia
               }
   except Exception as e:
       return {"isSuccess": False, "error": str(e)}


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

@app.get("/historial")
async def historial(id: int):
   try:
       datos = []
       historial = Select(Base.classes.Instancia).where(Base.classes.Instancia.idUsuario == id)
       with engine.connect() as connection:
           result = connection.execute(historial)
           for row in result:
               datos.append(HistorialInstancia(row._data[1], row._data[0], row._data[2]))
           return {"isSuccess": True, "data": datos}
   except Exception as e:
        return {"isSuccess": False, "message": str(e)}







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

