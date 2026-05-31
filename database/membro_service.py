from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# 🔹 Modelos de Banco de Dados
class Membro(Base):
    __tablename__ = 'membros'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(Integer, unique=True, nullable=False)
    nome = Column(String(100)) # Nome Real
    id_game = Column(String(20)) # ID dentro do GTA
    telefone = Column(String(20))
    usuario_discord = Column(String(100))
    aprovado = Column(Boolean, default=False)
    
    prisoes = relationship("Prisao", back_populates="oficial")
    advertencias = relationship("Advertencia", back_populates="oficial")

class Prisao(Base):
    __tablename__ = 'prisoes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    oficial_id = Column(Integer, ForeignKey('membros.id'))
    preso_nome = Column(String(100))
    motivo = Column(String(500))
    data = Column(DateTime, default=datetime.datetime.utcnow)
    
    oficial = relationship("Membro", back_populates="prisoes")

class Advertencia(Base):
    __tablename__ = 'advertencias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    oficial_id = Column(Integer, ForeignKey('membros.id'))
    motivo = Column(String(500))
    aprovador_id = Column(Integer)
    data = Column(DateTime, default=datetime.datetime.utcnow)
    
    oficial = relationship("Membro", back_populates="advertencias")

class Ticket(Base): # Adicionado para resolver o erro de import no crud.py
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    discord_id = Column(Integer)
    status = Column(String(20), default="Aberto")

# 🔹 Funções de Serviço (Helpers)
def verificar_cargo(membro, cargo_id):
    if not membro: return False
    return membro.guild_permissions.administrator or any(role.id == cargo_id for role in membro.roles)

def formatar_nome(membro):
    if not membro: return "Desconhecido"
    return membro.display_name or membro.name