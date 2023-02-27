# work_with_db.py
from sqlalchemy import create_engine, Column, Integer, String, insert, select, update, delete
from sqlalchemy.orm import declared_attr, declarative_base, Session

# Обычно класс, на основе которого создаётся декларативная база,
# называют так же, как и сам класс декларативной базы.
class Base:
    @declared_attr
    # В моделях-наследниках свойство __tablename__ будет создано
    # из имени модели, переведённого в нижний регистр.
    # Возвращаем это значение.
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):    
    # Описываем свойства модели/колонки таблицы:    
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    Base.metadata.create_all(engine)
    session = Session(engine)

    session.execute(update(Pep).where(Pep.status == 'Active').values(status='Draft'))

    #session.query(Pep).filter(Pep.pep_number > 20).delete()

    #pep8 = session.query(Pep).filter(Pep.status == 'Active').first()
    #session.delete(pep8)
    #pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()    
    #pep8.status = 'Closed'  
    #print(pep8)
#   results = session.query(Pep).filter(Pep.status == 'Active')
# Переменная results хранит объект Query...
#    print(results.all())
    #print(result.all())

    session.commit()