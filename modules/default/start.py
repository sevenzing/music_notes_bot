from aiogram import types
import logging

from modules.default import messages
from modules.database.models import User, get_user, create_if_not_exists, update_user
from modules.database import db_handler

@db_handler(commit=True)
async def cmd_start(session, message: types.Message):
    '''
    Conversation's entry point. Send start message
    '''

    user: User = create_if_not_exists(chat_id=message.chat.id)
    #user.username = message.from_user.username
    update_user(chat_id=message.chat.id, username=message.from_user.username)
    logging.info(f"user created: {user}")
    await message.answer(messages.ON_CMD_START)
