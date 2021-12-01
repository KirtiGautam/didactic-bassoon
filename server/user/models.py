from server import db
from sqlalchemy.sql.elements import BinaryExpression
from marshmallow import EXCLUDE, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.username}"

    @classmethod
    def filter(self, *criterion: BinaryExpression or bool):
        db_query = db.session.query(self)
        return db_query.filter(*criterion)

    @classmethod
    def get_by_id(self, id):
        return self.filter(self.id == id).first()

    @classmethod
    def upsert(self, obj: "UserSchema"):
        if not obj.username or not obj.password:
            raise ValueError("Please provide username and password")

        if obj.id:
            model = self.get_by_id(obj.id)
            model.password = obj.password
            model.username = obj.username
        else:
            model = User(username=obj.username, password=obj.password)
            db.session.add(model)
        db.session.flush()
        db.session.commit()
        return self.get_by_id(model.id)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        unknown = EXCLUDE

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument
        return self.Meta.model(**data_dict)
