import sys
import Arab
from Arab import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import no1bros
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
LOGS = logging.getLogger("سيثون كرستال")
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدء تنزيل سيثون كرستال")
    no1bros.loop.run_until_complete(setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"<b> ⌔︙ اهلا بك لقد نصبت سيثون كرستال (7.7) بنجاح 🥁 اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/no1bros ")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return
no1bros.loop.run_until_complete(startup_process())
def start_bot():
  try:
      List = ["no1bros","SYTHON2","ppblb","SYTHON CRYSTAL","SYTHON1","TEAM SYTHON CRYSTAL","SYTHON2","SYTHON3","no1bros","SYTHON3"]
      for id in List :
          no1bros.loop.run_until_complete(no1bros(functions.channels.JoinChannelRequest(id)))
  except Exception as e:
    print(e)
    return False
Checker = start_bot()
if Checker == False:
    print("كتمل تنصيب #1")

if len(sys.argv) not in (1, 3, 4):
    no1bros.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        no1bros.run_until_disconnected()
    except ConnectionError:
        pass
