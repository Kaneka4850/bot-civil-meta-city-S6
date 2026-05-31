import discord
from datetime import datetime

def criar_embed_denuncia(denunciante, acusado, motivo):
    embed = discord.Embed(title="🕵️ Denúncia Registrada", color=discord.Color.dark_red())
    embed.add_field(name="📣 Denunciante", value=denunciante.mention, inline=True)
    embed.add_field(name="👤 Acusado", value=acusado.mention, inline=True)
    embed.add_field(name="📄 Motivo", value=motivo, inline=False)
    embed.set_footer(text=f"⏰ Denúncia registrada em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
    return embed