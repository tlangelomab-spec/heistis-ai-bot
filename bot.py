from telegram.ext import Application, CommandHandler

TOKEN = "8612154903:AAHCd6yUu81EXC41h6D3GasdKKNjOT_ahG8"

async def start(update, context):
    await update.message.reply_text("🤖 **Heistis Ai is Active!**

Zaka Heist fx Trading Community

Commands:
/status
/trade
/brain")

async def status(update, context):
    await update.message.reply_text("✅ Active
🎯 68% Win Rate
💰 $12,450 Portfolio")

async def trade(update, context):
    await update.message.reply_text("🔍 Analyzing BTC...
📈 $50,240
🎯 Entry: $50,200
💪 87% Confidence")

async def brain(update, context):
    await update.message.reply_text("🧠 Dashboard: http://localhost:8501")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))
app.add_handler(CommandHandler("trade", trade))
app.add_handler(CommandHandler("brain", brain))

print("🤖 Heistis Ai running on Render...")
app.run_polling()
