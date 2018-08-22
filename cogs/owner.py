import inspect
import io
import traceback
from contextlib import redirect_stdout
import subprocess

from discord.ext import commands

class Eval:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["exe"])
    async def eval(self, ctx, *, code: str):
        if ctx.message.author.id == 296084893459283968 or 256962349217349632:
            stdout = io.StringIO()
            result = ""
            try:
                with redirect_stdout(stdout):
                    for executor in (eval, exec):
                        try:
                            result = executor(code)
                            if inspect.isawaitable(result):
                                result = await result
                            break
                        except SyntaxError as e:
                            result = get_syntax_error(e)
            except:
                result = stdout.getvalue() + traceback.format_exc()
            finally:
                if not result:
                    result = stdout.getvalue()

                self.last_result = result

            await ctx.send(f"```py\n{str(result)[:1990]}\n```")


def setup(bot):
    bot.add_cog(Eval(bot))
