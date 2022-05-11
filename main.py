import interactions

import Events
import config

bot = interactions.Client(token=config.token)

guild_id = config.guildID if config.guildID else interactions.MISSING

current_events_setup: dict[int, Events.EventDataCollector] = dict()


@bot.command(
    name="set_channel",
    description="Set this channel as the event channel",
    scope=guild_id
)
async def set_channel(ctx: interactions.CommandContext):
    Events.channel = ctx.get_channel()
    await ctx.send("Channel set")


@bot.command(
    name="create_event",
    description="Create a new event",
    scope=guild_id
)
async def create_event(ctx: interactions.CommandContext):
    if not Events.channel:
        await ctx.send("You need to first set a channel for the events. \
                        Use /set_channel where you want the events to be sent to")
        return
    await ctx.send("Starting to event creation chain")
    event = Events.EventDataCollector(ctx.author.id)
    current_events_setup[event.author_id] = event
    await ctx.send("Please enter the event name")
    modal = interactions.Modal(
        title="Event title",
        custom_id="enter_event_title_text_field",
        components=[Events.enterEventTitleTextField],
    )
    await ctx.popup(modal)


@bot.modal("enter_event_title_text_field")
async def enter_event_title_text_field_response(ctx: interactions.CommandContext, response: str):
    await ctx.send("Got event title")
    await ctx.send("Please enter the event description")
    current_events_setup[ctx.author.id].title = response
    modal = interactions.Modal(
        title="Event description",
        custom_id="enter_event_description_text_field",
        components=[Events.enterEventDescriptionTextField]
    )
    await ctx.popup(modal)


@bot.modal("enter_event_description_text_field")
async def enter_event_description_text_field_response(ctx: interactions.CommandContext, response: str):
    await ctx.send("Got event description")
    await ctx.send("Please enter the max nr of participants")
    current_events_setup[ctx.author.id].description = response
    modal = interactions.Modal(
        title="Max nr of participants",
        custom_id="enter_event_max_participants",
        components=[Events.enterEventParticipantsNrField]
    )
    await ctx.popup(modal)


@bot.modal("enter_event_max_participants")
async def enter_event_max_participants_response(ctx: interactions.CommandContext, response: str):
    try:
        max_participants = int(response)
        if max_participants < 0:
            raise ValueError("Nr too low")
    except ValueError:
        await ctx.send("Couldn't convert your input to a valid number")


bot.start()
