from flask_sqlalchemy import SQLAlchemy

class Chat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)

class Configuration(db.Model):
    key: Mapped[str] = mapped_column(unique=True)
    value: Mapped[str] = mapped_column(unique=True)