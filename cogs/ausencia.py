import discord
from discord.ext import commands
from datetime import datetime

# --- CONFIGURAÇÕES ---
# ID do canal onde os registros de ausência serão enviados
ID_CANAL_LOGS = 1420450395762987090  

class AbsenceModal(discord.ui.Modal, title="Formulário de Ausência"):
    """
    Representa o formulário que abre quando o usuário clica no botão.
    """
    qra = discord.ui.TextInput(
        label="QRA (Identificação do Oficial)",
        placeholder="Ex: Arima Kishou",
        style=discord.TextStyle.short,
        required=True
    )
    
    inicio = discord.ui.TextInput(
        label="Início da Ausência",
        placeholder="DD/MM/YYYY",
        style=discord.TextStyle.short,
        required=True,
        min_length=10,
        max_length=10
    )
    
    motivo = discord.ui.TextInput(
        label="Motivo da Ausência",
        placeholder="Descreva brevemente o motivo...",
        style=discord.TextStyle.paragraph,
        required=True
    )
    
    termino = discord.ui.TextInput(
        label="Término da Ausência",
        placeholder="DD/MM/YYYY",
        style=discord.TextStyle.short,
        required=True,
        min_length=10,
        max_length=10
    )

    def is_valid_date(self, date_str: str) -> bool:
        """Verifica se a string segue o padrão de data brasileiro."""
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    async def on_submit(self, interaction: discord.Interaction):
        # Validação de datas antes de prosseguir
        if not self.is_valid_date(self.inicio.value) or not self.is_valid_date(self.termino.value):
            return await interaction.response.send_message(
                "❌ Erro: Uma das datas inseridas é inválida. Use o formato DD/MM/YYYY.", 
                ephemeral=True
            )

        log_channel = interaction.guild.get_channel(ID_CANAL_LOGS)
        if not log_channel:
            return await interaction.response.send_message(
                "❌ Erro crítico: Canal de logs não configurado corretamente.", 
                ephemeral=True
            )

        # Construção do Embed de Log
        embed = discord.Embed(
            title="📌 Ausência Registrada",
            description=f"O oficial {interaction.user.mention} solicitou um período de ausência.",
            color=discord.Color.dark_orange(),
            timestamp=datetime.now()
        )
        embed.add_field(name="🆔 QRA", value=self.qra.value, inline=True)
        embed.add_field(name="📅 Período", value=f"{self.inicio.value} ➔ {self.termino.value}", inline=True)
        embed.add_field(name="📝 Motivo", value=self.motivo.value, inline=True)
        embed.set_footer(text=f"ID do Usuário: {interaction.user.id}")

        # Envio para o canal de logs mencionando o usuário
        await log_channel.send(content=f"🔔 Nova ausência: {interaction.user.mention}", embed=embed)
        
        await interaction.response.send_message("✅ Sua ausência foi registrada com sucesso!", ephemeral=True)


class AbsencePersistentView(discord.ui.View):
    """
    View que contém o botão para abrir o modal. 
    O custom_id é essencial para a persistência.
    """
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Solicitar Ausência", 
        style=discord.ButtonStyle.primary, 
        custom_id="btn_absence_request_persistent" 
    )
    async def open_modal(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(AbsenceModal())


class AbsenceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Registra a View no Bot para que ela responda mesmo após o Bot reiniciar.
        """
        self.bot.add_view(AbsencePersistentView())
        print(f"[{self.__class__.__name__}] View persistente carregada.")

    @commands.command(name="setup_ausencia")
    @commands.has_permissions(administrator=True)
    async def setup_ausencia(self, ctx: commands.Context):
        """
        Envia a mensagem principal com o botão de ausência.
        Uso: !setup_ausencia
        """
        embed = discord.Embed(
            title="✈️ Registro de Ausência",
            description=(
                "Utilize o botão abaixo para preencher o formulário de ausência.\n\n"
                "**Regras:**\n"
                "• Preencha o QRA corretamente.\n"
                "• Use apenas o formato **DD/MM/YYYY** para datas.\n"
                "• Informe um motivo claro."
            ),
            color=discord.Color.dark_orange()
        )
        
        await ctx.send(embed=embed, view=AbsencePersistentView())
        
        # Opcional: Deletar a mensagem do comando !setup_ausencia para limpar o chat
        try:
            await ctx.message.delete()
        except:
            pass

    @setup_ausencia.error
    async def setup_error(self, ctx, error):
        """Tratamento de erro para falta de permissão."""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Você não tem permissão para configurar este menu.", delete_after=10)


async def setup(bot: commands.Bot):
    await bot.add_cog(AbsenceCog(bot))