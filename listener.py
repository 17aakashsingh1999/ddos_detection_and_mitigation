import threading
from priority_queue import PriorityQueue
from sqlalchemy import create_engine, Integer, Float, Column, String
from sqlalchemy.ext.declarative import declararive_base
from sql.orm import sessionmaker

def init_db():
	engine = create_engine('sqlite:///db.sql', echo=False)
	Base = declarative_base()

	class Packet(Base):
		def __init__(self):
			self.__tablename__ = "packet"
			self.address = Column(Integer)
			self.arrival = Column(Float)
			self.avg_arrival_prev_pkt = Column(Float)
			self.avg_arrival_curr_pkt = Column(Float)
			self.diff = Column(Float)
		def __str__(self):
			return "ip: {}, time_of_arrival: {}".format(self.address,self.arrival)

	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()
	return (session, Packet)

def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

@synchronized
def listener(session,Packet):
	