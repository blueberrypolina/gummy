import datetime

from client import Client
from Appointment import Appointment
from service import Service
class Rules():
    def __init__(self, rew_rep):
        self.reviews = rew_rep
        self.app = []

    def service_rating(self, master, master_rep): #увольнение мастера
        sum = 0
        count = 0
        for i in self.reviews.reviews:
            if i.master == master:
                sum += i.rating
                count += 1
        if count != 0:
            master.rating = sum / count
        else:
            master.rating = 0
        master_rep.save_master(master)
        if master.rating <= 2:
            master_rep.masters.remove(master)

    def Service_Review(self, client, app): #1 отзыв 1 услуга
        for i in client.reviews:
            if i.appointment == app:
                return False #переходим на другую страницу
        return True #предлагаем написать отззыв




    def OneServiceInTime(self, client, service, ap_time): #1 временной слот 1 услуги
        for i in client.appointment:
            if i.service == service:
                if i.appointment_time.date() == ap_time.date():
                    return False
        return True



    def OnlyOneTime(self, appointment_time, client):  #нельзя записаться на 2 услуги в одно время
        # Проверяем, есть ли уже запись клиента на услугу в заданное время
        for app in client.appointment:
            if app.appointment_time == appointment_time:
                return False
        return True

    def booking(self,client: Client, service: Service, time):
        flag = True
        if self.OnlyOneTime(time, client) == False:
            flag = False
            return -1
        if self.OneServiceInTime(client, service, time):
            flag = False
            return -1

        if flag:
            client.appointment.append(Appointment(client, service, datetime.datetime.now()))
            return 1


