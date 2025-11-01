from models import create_tables
from services import create_user, get_user, get_all_user, update_user, delete_user

# create tables
# create_tables()

# create user
# create_user("John Doe", "john@example.com")
# create_user("saimun", "saimun@example.com")

# get user by id
user = get_user(1)
print(user)

# update user
# user = update_user(2, "saimun@gmail.com")

# get all users
users = get_all_user()
print(users)

# # delete user
# delete_user(1)
