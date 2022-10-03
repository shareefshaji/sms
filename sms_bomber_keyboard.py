from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_main = InlineKeyboardMarkup()
btn_call_inl = InlineKeyboardButton(text='☎️Call', callback_data='call')
btn_sms_inl = InlineKeyboardButton(text='💬Sms', callback_data='sms')
btn_mix_inl = InlineKeyboardButton(text='☎️💬Mix', callback_data='mix')
inline_main.add(btn_call_inl,btn_sms_inl,btn_mix_inl)