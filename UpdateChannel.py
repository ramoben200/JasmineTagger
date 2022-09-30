
# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text=f"Üzgünüm efendim, Yasaklandınız. İletişim Support.", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
await app.send_message(chat_id=message.chat.id, text="Lütfen Beni Kullanmak İçin Güncellemelerim Kanalına Katılın!\n ve Kontrol etmek için tıklayın /start", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Güncellemeler Kanalına Katılın 🤖", url=f"https://t.me/{Ballasresmi}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text=f"Bir şeyler yanlış gitti. İletişim Support.", parse_mode="markdown", disable_web_page_preview=True)
         return 1
