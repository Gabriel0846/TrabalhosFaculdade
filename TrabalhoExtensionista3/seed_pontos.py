# atualizar_coordenadas.py
from app import app, db
from models import PontoColeta

# Dicionário com as coordenadas corretas (Nome exato : (lat, lon))
coordenadas_corretas = {
    "Paço Municipal de Arapongas": (-23.4153, -51.4294),
    "UBS Central": (-23.4168, -51.4275),
    "UBS São Vicente": (-23.4139, -51.4314),
    "UBS Jardim Petrópolis": (-23.4132, -51.4606),
    "UBS Vila Bernardes": (-23.4161, -51.4235),
    "Magazine Luiza": (-23.4101, -51.4375),
    "Moon Cell - Assistência Técnica": (-23.4085, -51.4310),
    "Conserta Cell Arapongas": (-23.4175, -51.4265),
    "Farmácia Nikkey": (-23.4067, -51.4425),
    "Drogamais São Marcos": (-23.4070, -51.4420),
    "Loja Claro": (-23.4092, -51.4368),
    "Baseware Computadores": (-23.4035, -51.4290),
    "Casa Eletrônica": (-23.3952, -51.4501),
    "Top Som & Alarmes": (-23.4032, -51.4293),
    "Renogás": (-23.4153, -51.4314),
    "Josemar L de Souza e Cia": (-23.4068, -51.4425)
}

def atualizar():
    with app.app_context():
        atualizados = 0
        for nome, (lat, lon) in coordenadas_corretas.items():
            ponto = PontoColeta.query.filter_by(nome=nome).first()
            if ponto:
                ponto.latitude = lat
                ponto.longitude = lon
                atualizados += 1
                print(f"✅ Coordenadas atualizadas: {nome} -> ({lat}, {lon})")
            else:
                print(f"⚠️  Ponto não encontrado: {nome}")

        db.session.commit()
        print(f"\nTotal de pontos atualizados: {atualizados}")

if __name__ == "__main__":
    atualizar()