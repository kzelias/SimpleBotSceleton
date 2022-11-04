from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize


kb_urls = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(emojize(":red_exclamation_mark:"), callback_data="call14")
b3 = InlineKeyboardButton(emojize(":money_with_wings:"), callback_data="call31")
b4 = InlineKeyboardButton(emojize(":currency_exchange:"), callback_data="call20")
b5 = InlineKeyboardButton(emojize(":bookmark_tabs:"), callback_data="call30")
b6 = InlineKeyboardButton(emojize(":bookmark_tabs:"), callback_data="call16")
b7 = InlineKeyboardButton(emojize(":megaphone: contact"), callback_data="contact")
kb_urls.add(b1, b3, b4, b5, b7)


kb_urls_ch = InlineKeyboardMarkup(row_width=2)
ch1 = InlineKeyboardButton(emojize("1"), callback_data="call29")
ch2 = InlineKeyboardButton(emojize("2"), callback_data="call32")
ch3 = InlineKeyboardButton(emojize("3"), callback_data="call33")
ch5 = InlineKeyboardButton(emojize("4"), callback_data="call34")
ch6 = InlineKeyboardButton(emojize("5"), callback_data="call35")
ch7 = InlineKeyboardButton(emojize("6"), callback_data="call36")
ch8 = InlineKeyboardButton(emojize("7"), callback_data="call37")
ch9 = InlineKeyboardButton(emojize("8"), callback_data="call38")
ch10 = InlineKeyboardButton(emojize("9"), callback_data="call39")
ch11 = InlineKeyboardButton(emojize("10"), callback_data="call40")
ch12 = InlineKeyboardButton(emojize("11"), callback_data="call41")
ch13 = InlineKeyboardButton(emojize("12"), callback_data="call42")
ch14 = InlineKeyboardButton(emojize("13"), callback_data="call43")
ch15 = InlineKeyboardButton(emojize("14"), callback_data="call44")
back = InlineKeyboardButton(emojize(":BACK_arrow:"), callback_data="back")
kb_urls_ch.add(
    ch1, ch2, ch3, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, back
)


kb_urls_i = InlineKeyboardMarkup(row_width=1)
d1 = InlineKeyboardButton(emojize(":red_exclamation_mark:"), callback_data="call1")
d2 = InlineKeyboardButton(emojize(":derelict_house:"), callback_data="call2")
d3 = InlineKeyboardButton(emojize(":page_facing_up:"), callback_data="call3")
d5 = InlineKeyboardButton(emojize(":mobile_phone:"), callback_data="call4")
d6 = InlineKeyboardButton(emojize(":credit_card:"), callback_data="call5")
d7 = InlineKeyboardButton(emojize(":person_running:"), callback_data="call6")
d8 = InlineKeyboardButton(emojize(":hammer_and_wrench:"), callback_data="call7")
d9 = InlineKeyboardButton(emojize(":closed_book:"), callback_data="call18")
d10 = InlineKeyboardButton(emojize(":card_index_dividers:"), callback_data="call19")

back = InlineKeyboardButton(emojize(":BACK_arrow:"), callback_data="back")
kb_urls_i.add(d1, d2, d3, d5, d6, d7, d8, d9, d10, back)

kb_urls_j = InlineKeyboardMarkup(row_width=1)
j1 = InlineKeyboardButton(emojize(":hammer_and_wrench:"), callback_data="call8")
j2 = InlineKeyboardButton(emojize(":derelict_house:"), callback_data="call13")
kb_urls_j.add(j1, j2, back)

kb_urls_j_d = InlineKeyboardMarkup()
jd1 = InlineKeyboardButton(emojize(":file_folder:"), callback_data="call9")
jd2 = InlineKeyboardButton(emojize(":crossed_swords:"), callback_data="call10")
jd3 = InlineKeyboardButton(emojize(":desktop_computer:"), callback_data="call11")
job_back = InlineKeyboardButton(emojize(":BACK_arrow:"), callback_data="call12")
kb_urls_j_d.add(jd1, jd2, jd3, job_back)

kb_urls_j_i = InlineKeyboardMarkup()
ji1 = InlineKeyboardButton(emojize(":ferry:"), callback_data="call13")
kb_urls_j_i.add(ji1, job_back)

kb_urls_j_back = InlineKeyboardMarkup()
kb_urls_j_back.add(job_back)

kb_urls_c = InlineKeyboardMarkup()
c0 = InlineKeyboardButton(emojize(":derelict_house:"), callback_data="call21")
c1 = InlineKeyboardButton(emojize("🚕"), callback_data="call22")
c2 = InlineKeyboardButton(emojize("🗺"), callback_data="call23")
c3 = InlineKeyboardButton(emojize("🍳"), callback_data="call15")
kb_urls_c.add(c0, c1, c2, c3, back)

kb_urls_contact = InlineKeyboardMarkup(row_width=1)
con1 = InlineKeyboardButton(emojize(":microphone: info"), callback_data="contact_info")
con2 = InlineKeyboardButton(
    emojize(":money_bag: comm offer"), callback_data="contact_comm"
)
kb_urls_contact.add(con1, con2, back)

kb_urls_contact_back = InlineKeyboardMarkup(row_width=1)
con_back = InlineKeyboardButton(emojize(":BACK_arrow:"), callback_data="contact_back")
kb_urls_contact_back.add(con_back)
