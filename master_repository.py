class MasterRepository:
    def __init__(self):
        self.masters = []

    def save_master(self, master):
        self.masters.append(master)

    def find_master_by_id(self, master_id):
        for master in self.masters:
            if master.master_id == master_id:
                return master
        return None