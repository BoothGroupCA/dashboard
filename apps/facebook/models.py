from apps import db


class Results(db.Model):
    __tablename__ = 'Results'
    id = db.Column(db.Integer, primary_key=True)
    page_reach= db.Column(db.BigInteger(unsigned=True), unique=True)
    source = db.Column(db.String(64), unique=True)
    date = db.Column(db.String(64), unique=True)
    

    def __str__(self)-> int:
        return self.page_reach
