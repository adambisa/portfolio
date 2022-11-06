import random, string, datetime,time,secrets



class Check:
    def __init__(self, id :str, last_ping:str, last_ping_timestamp:str,name:str, secret_key:str,status:str):
        self.id = id
        self.last_ping=last_ping
        self.last_ping_timestamp=last_ping_timestamp
        self.name=name
        self.secret_key=secret_key
        self.status=status
    def check(self, id :str, last_ping:str, last_ping_timestamp:str,name:str, secret_key:str,status:str):
        pass
class Schedule():
    def __init__(self, id, period, grace, secret_key):
        self.id=id
        self.period=period
        self.grace=grace
        self.secret_key=secret_key
    def schedule(self, id, period, grace, secret_key):
        show_schedule=Schedule(id, period, grace, secret_key)
        return show_schedule.__dict__
        
class NotificationS:
    pass

