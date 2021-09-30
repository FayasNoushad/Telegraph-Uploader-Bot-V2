import motor.motor_asyncio


class Database:
    def __init__(self, url, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(url)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, user_id):
        return dict(id=user_id)

    async def add_user(self, user_id):
        user = self.new_user(user_id)
        await self.col.insert_one(user)

    async def is_user_exist(self, user_id):
        user = await self.col.find_one({'id': int(user_id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
