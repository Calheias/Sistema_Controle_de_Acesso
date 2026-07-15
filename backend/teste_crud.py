from database import SessionLocal
from crud import create_user, get_all_users

db = SessionLocal()

create_user(
    db=db,
    nome="Gabriel",
    uid="04A31F8C",
    tipo_credencial="RFID",
    nivel_acesso="ADMIN",
)

usuarios = get_all_users(db)

for usuario in usuarios:
    print(usuario.nome, usuario.uid)

db.close()