import interactions
import time
from datetime import datetime

channel: interactions.Channel = None


enterEventTitleTextField = interactions.TextInput(
    style=interactions.TextStyleType.SHORT,
    label="Enter the name of the event you want to create",
    custom_id="event_creator_event_title",
    min_length=1,
    max_length=30
)

enterEventDescriptionTextField = interactions.TextInput(
    style=interactions.TextStyleType.PARAGRAPH,
    label="Enter the description of the event you want to create",
    custom_id="event_creator_event_description",
    min_length=1
)

enterEventParticipantsNrField = interactions.TextInput(
    style=interactions.TextStyleType.SHORT,
    label="Enter the max nr of participants",
    custom_id="event_creator_event_max_participants",
    min_length=1,
    max_length=3
)


class EventDataCollector:

    title = ""
    description = ""
    nr_participants = 0

    def __init__(self, aid):
        self.timestamp = time.time()
        self.author_id = aid


class Event:
    participants = list()

    def __init__(self, bot: interactions.Client):
        self.bot = bot
