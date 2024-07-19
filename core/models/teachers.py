from core import db
from core.libs import helpers,assertions
from core.apis.decorators import AuthPrincipal



class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)
    
    @classmethod
    def get_all_teachers(cls,auth_principal: AuthPrincipal):

        assertions.assert_valid(auth_principal.principal_id is not None,'Assignment belongs to another teacher')
        
        return cls.query.all()