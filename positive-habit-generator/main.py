from app.database import Base, engine
from app.cli import main_menu

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main_menu()
