import os
import json
import random
from twitchio.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        # Initialize bot with secrets from .env
        super().__init__(
            token=os.getenv('TMI_TOKEN'),
            prefix=os.getenv('PREFIX'),
            initial_channels=[os.getenv('CHANNEL')]
        )
        self.db_file = "points.json"

    # --- JSON PERSISTENCE (Simple Database) ---
    def load_db(self):
        # Check if database file exists
        if not os.path.exists(self.db_file):
            return {}
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading DB: {e}")
            return {}

    def save_db(self, data):
        # Write data back to the file
        with open(self.db_file, 'w') as f:
            json.dump(data, f)

    # --- EVENTS ---
    async def event_ready(self):
        print(f'✅ Connected to Twitch as: {self.nick}')
        print(f'📺 Monitoring channel: {os.getenv("CHANNEL")}')

    async def event_message(self, message):
        # Ignore messages sent by the bot itself
        if message.echo:
            return

        # Loyalty Logic: Award 10 points per message
        user = message.author.name.lower()
        data = self.load_db()
        
        if user not in data:
            data[user] = 0
        
        data[user] += 10
        self.save_db(data)
        
        # Process commands if they exist in the message
        await self.handle_commands(message)

    # --- COMMANDS ---

    @commands.command(name='hello')
    async def hello_command(self, ctx):
        await ctx.send(f'Hey @{ctx.author.name}! 🤖 Greetings from AWS Cloud!')

    @commands.command(name='coins')
    async def coins_command(self, ctx):
        user = ctx.author.name.lower()
        data = self.load_db()
        points = data.get(user, 0)
        await ctx.send(f'💰 @{ctx.author.name}, you currently have {points} Stream-Coins.')

    @commands.command(name='gamble')
    async def gamble_command(self, ctx):
        user = ctx.author.name.lower()
        data = self.load_db()
        min_bet = 50
        
        # Check if user has enough balance
        if user not in data or data[user] < min_bet:
            await ctx.send(f'❌ Not enough coins! You need at least {min_bet} to gamble.')
            return

        # RNG Logic (50/50 Chance)
        result = random.choice(["WIN", "LOSE"])
        
        if result == "WIN":
            data[user] += 100
            await ctx.send(f'🎰 JACKPOT! @{ctx.author.name} won 100 coins!')
        else:
            data[user] -= 50
            await ctx.send(f'📉 Bad luck... @{ctx.author.name} lost 50 coins.')
            
        self.save_db(data)

# Run the bot
bot = Bot()
bot.run()