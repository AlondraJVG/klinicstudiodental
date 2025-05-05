from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import yagmail
from datetime import datetime

citas_db = {}

