import interactions
import asyncio

import config

bot = interactions.Client(token=config.token)

guildID = config.guildID if config.guildID else interactions.MISSING


@bot.command(
    name="hello_world",
    description="Does this update?",
    scope=guildID
)
async def hello_world(ctx: interactions.CommandContext):
    await ctx.send("Hello there")


@bot.command(
    name="command_with_option",
    description="Now this doesn't work",
    scope=guildID,
    options=[
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def command_with_options(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"You said '{text}'!")


@bot.command(
    name="command_with_subcommands",
    description="This description isn't seen in UI (yet?)",
    scope=guildID,
    options=[
        interactions.Option(
            name="first_subcommand",
            description="Much wow",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="option",
                    description="A descriptive description",
                    type=interactions.OptionType.INTEGER,
                    required=True,
                ),
            ],
        ),
        interactions.Option(
            name="second_command",
            description="Very pog",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="second_option",
                    description="A descriptive description",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
            ],
        ),
        interactions.Option(
            name="third_command",
            description="Very pog",
            type=interactions.OptionType.SUB_COMMAND,
            options=[
                interactions.Option(
                    name="third_option",
                    description="Some thing",
                    type=interactions.OptionType.STRING,
                    required=False,
                )
            ]
        ),
    ],
)
async def cmd(ctx: interactions.CommandContext,
              sub_command: str = None,
              second_option: str = None,
              option: int = None,
              third_option: str = None):
    print(f"sub_command: {sub_command}, second_option: {second_option}, option: {option}, third_option: {third_option}")
    if sub_command == "first_subcommand":
        await ctx.send(f"You selected the command_name sub command and put in {option}")
    elif sub_command == "second_command":
        await ctx.send(f"You selected the second_command sub command and put in {second_option}")
    elif sub_command == "third_command":
        await ctx.send(f"You selected the third_command sub and put in {third_option}")
    else:
        await ctx.send("Received unknown command")


button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Button test",
    custom_id="hello"
)


@bot.command(
    name="button_test",
    description="Test for a button",
    scope=guildID,
)
async def button_test(ctx):
    await ctx.send("testing", components=button)


@bot.component("hello")
async def button_response(ctx):
    await ctx.send("You clicked the Button :O", ephemeral=True)


@bot.command(
    name="timeit",
    description="Send an answer in x seconds",
    scope=guildID,
    options=[
        interactions.Option(
            name="time",
            description="What you want to say",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def command_with_options(ctx: interactions.CommandContext, time: int):
    await ctx.send(f"Responding in {time} seconds")
    await asyncio.sleep(time)
    await ctx.send("Response")


bot.start()
