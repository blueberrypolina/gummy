class Rules():
    def __init__(self, rew_rep):
        self.reviews = rew_rep

    def service_rating(self, master, master_rep):
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

    def Service_Review(self, client, app):
        if app in client.appointment:
            return False
        return True



    def OneServiceInTime(self, client, service, ap_time):
        for i in client.appointment:
            if i.service == service:
                if i.appointment_time.date() == ap_time.date():
                    return False
        return True



    def OnlyOneTime(self, appointment_time, client):
        # Проверяем, есть ли уже запись клиента на услугу в заданное время
        for app in client.appointment:
            if app.appointment_time == appointment_time:
                return False
        return True
