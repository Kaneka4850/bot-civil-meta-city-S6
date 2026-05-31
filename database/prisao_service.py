import discord
from datetime import datetime

def criar_embed_prisao(dados, autor):
    embed = discord.Embed(title="📚 Registro de Prisão", color=discord.Color.red())
    embed.add_field(name="👮 QRA da Primária", value=dados["qra"], inline=True)
    embed.add_field(name="🪪 Passaporte da Primária", value=dados["passaporte_qra"], inline=True)
    embed.add_field(name="👤 Nome do Preso", value=dados["nome_preso"], inline=True)
    embed.add_field(name="🆔 Passaporte do Preso", value=dados["passaporte_preso"], inline=True)
    embed.add_field(name="📜 Artigos", value=dados["artigos"], inline=False)
    embed.add_field(name="💰 Houve multa?", value=dados["houve_multa"], inline=True)
    embed.add_field(name="🔢 Valor", value=dados["valor_multa"], inline=True)
    embed.add_field(name="📌 Advogado", value=dados.get("advogado", "Não informado"), inline=True)
    embed.add_field(name="🪪 Passaporte Advogado", value=dados.get("passaporte_advogado", "Não informado"), inline=True)
    embed.set_footer(text=f"⏰ Prisão registrada em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
    embed.set_author(name=f"Registrado por: {autor}")
    return embed