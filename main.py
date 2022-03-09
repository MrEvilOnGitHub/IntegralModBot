import interactions

import config

bot = interactions.Client(token=config.token)


@bot.command(
    name="helloWorld",
    description="Hello World",
    # scope=685499370959011855,
)
async def HelloWorld(ctx: interactions.CommandContext):
    await ctx.send("Hello World!")


bot.start()
