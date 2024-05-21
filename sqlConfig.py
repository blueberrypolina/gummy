from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

client_masters = Table('client_masters', Base.metadata,
                       Column('client_id', Integer, ForeignKey('clients.id')),
                       Column('master_id', Integer, ForeignKey('masters.id'))
                       )


class ClientModel(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    personal_data = Column(String, nullable=False)
    appointments = relationship('AppointmentModel', back_populates='client')
    masters = relationship('MasterModel', secondary=client_masters)
    reviews = relationship('ReviewModel', back_populates='client')


class MasterModel(Base):
    __tablename__ = 'masters'

    id = Column(Integer, primary_key=True)
    rating = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    reviews = relationship('ReviewModel', back_populates='master')


class ReviewModel(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    master_id = Column(Integer, ForeignKey('masters.id'))
    master = relationship('MasterModel', back_populates='reviews')
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('ClientModel', back_populates='reviews')


class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    appointment_time = Column(DateTime, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('ClientModel', back_populates='appointments')
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship('ServiceModel', back_populates='appointments')


class ServiceModel(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    payment = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    appointments = relationship('AppointmentModel', back_populates='service')
