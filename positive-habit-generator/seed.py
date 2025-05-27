from app.database import Session
from app.models import User, Category

session = Session()

# Add a user
user = User(name="Cynthia")
session.add(user)

# Add categories
cat1 = Category(name="Health")
cat2 = Category(name="Productivity")
session.add_all([cat1, cat2])

session.commit()
session.close()
print("Seeded database!")
