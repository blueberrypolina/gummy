from sqlConfig import ClientModel, MasterModel, ReviewModel, AppointmentModel, ServiceModel

class Rules:
    def __init__(self, session):
        self.session = session

    def service_rating(self, master):
        reviews = self.session.query(ReviewModel).filter_by(master_id=master.id).all()
        if reviews:
            master.rating = sum(review.rating for review in reviews) / len(reviews)
        else:
            master.rating = 0
        self.session.commit()
        if master.rating <= 2:
            self.session.delete(master)
            self.session.commit()

    def Service_Review(self, client, app):
        for review in client.reviews:
            if review.appointment_id == app.id:
                return False
        return True

    def OneServiceInTime(self, client, service, ap_time):
        for appointment in client.appointments:
            if appointment.service_id == service.id and appointment.appointment_time.date() == ap_time.date():
                return False
        return True

    def OnlyOneTime(self, appointment_time, client):
        for appointment in client.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def booking(self, client, service, date):
        if not self.OnlyOneTime(date, client):
            return -1
        if not self.OneServiceInTime(client, service, date):
            return -1

        # appointment = AppointmentModel(client_id=client.id, service_id=service.id, appointment_time=date)
        # client.appointments.append(appointment)
        # self.session.add(appointment)
        # self.session.commit()
        return 1
