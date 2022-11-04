from aiogram import Dispatcher
from .handler_main import (
    command_start,
    call14,
    call31,
    call20,
    call16,
    contact,
    call30,
    back,
)
from .handler_i import call1, call2, call3, call4, call7, call6, call5, call18, call19
from .handler_j import call8, call13, call9, call10, call11, call12
from .handler_c import call21, call22, call23, call15
from .handler_contact import (
    contact_info,
    contact_comm,
    contact_text_message,
    contact_back,
)
from .handler_ch import (
    call29,
    call32,
    call33,
    call34,
    call35,
    call37,
    call38,
    call39,
    call40,
    call41,
    call42,
    call43,
    call44,
    call45,
)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])

    dp.register_callback_query_handler(call14, text=["call14"])
    dp.register_callback_query_handler(call31, text=["call31", "call12"])

    dp.register_callback_query_handler(call20, text=["call20"])
    dp.register_callback_query_handler(call30, text=["call30"])
    dp.register_callback_query_handler(call16, text=["call16"])
    dp.register_callback_query_handler(contact, text=["contact"])

    dp.register_callback_query_handler(call29, text=["call29"])
    dp.register_callback_query_handler(call32, text=["call32"])
    dp.register_callback_query_handler(call33, text=["call33"])
    dp.register_callback_query_handler(call34, text=["call34"])
    dp.register_callback_query_handler(call35, text=["call35"])
    dp.register_callback_query_handler(call37, text=["call37"])
    dp.register_callback_query_handler(call38, text=["call38"])
    dp.register_callback_query_handler(call39, text=["call39"])
    dp.register_callback_query_handler(call40, text=["call40"])
    dp.register_callback_query_handler(call41, text=["call41"])

    dp.register_callback_query_handler(call42, text=["call42"])
    dp.register_callback_query_handler(call43, text=["call43"])
    dp.register_callback_query_handler(call44, text=["call44"])
    dp.register_callback_query_handler(call45, text=["call45"])

    dp.register_callback_query_handler(call1, text=["call1"])
    dp.register_callback_query_handler(call2, text=["call2"])
    dp.register_callback_query_handler(call3, text=["call3"])
    dp.register_callback_query_handler(call4, text=["call4"])
    dp.register_callback_query_handler(call7, text=["call7"])
    dp.register_callback_query_handler(call6, text=["call6"])
    dp.register_callback_query_handler(call5, text=["call5"])
    dp.register_callback_query_handler(call18, text=["call18"])
    dp.register_callback_query_handler(call19, text=["call19"])

    dp.register_callback_query_handler(call8, text=["call8"])
    dp.register_callback_query_handler(call13, text=["call13"])
    dp.register_callback_query_handler(call9, text=["call9"])
    dp.register_callback_query_handler(call10, text=["call10"])
    dp.register_callback_query_handler(call11, text=["call11"])
    dp.register_callback_query_handler(call12, text=["call12"])

    dp.register_callback_query_handler(call21, text=["call21"])
    dp.register_callback_query_handler(call22, text=["call22"])
    dp.register_callback_query_handler(call23, text=["call23"])
    dp.register_callback_query_handler(call15, text=["call15"])

    dp.register_callback_query_handler(contact_info, text=["contact_info"])
    dp.register_callback_query_handler(contact_comm, text=["contact_comm"])
    dp.register_callback_query_handler(contact_back, text=["contact_back"])
    dp.register_message_handler(contact_text_message)

    dp.register_callback_query_handler(back, text=["back"])
