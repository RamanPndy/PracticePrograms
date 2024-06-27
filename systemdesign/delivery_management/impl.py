from systemdesign.delivery_management.interface import IDeliveryManager, IPartnerAssigner, ITracker, ITripPartnerFinder

class DeliveryManager(IDeliveryManager):
    _instance = None

    @staticmethod
    def get_instance():
        if DeliveryManager._instance is None:
            DeliveryManager()
        return DeliveryManager._instance

    def __init__(self):
        if DeliveryManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DeliveryManager._instance = self
            self.deliveries = {}
            self.partner_assigner = None
            self.tracker = None

    def create_delivery(self, delivery_id: str, details: dict):
        self.deliveries[delivery_id] = details

    def assign_partner(self, delivery_id: str):
        if self.partner_assigner:
            partner_id = self.partner_assigner.assign(delivery_id)
            if self.tracker:
                self.tracker.start_tracking(partner_id)

class RandomPartnerAssigner(IPartnerAssigner):
    def __init__(self, trip_partner_finder: ITripPartnerFinder):
        self.trip_partner_finder = trip_partner_finder

    def assign(self, delivery_id: str) -> str:
        free_partners = self.trip_partner_finder.find_free_partners()
        return free_partners[0] if free_partners else None

class PartnerTracker(ITracker):
    def __init__(self):
        self.partners = {}

    def start_tracking(self, partner_id: str):
        self.partners[partner_id] = "Started tracking"

    def stop_tracking(self, partner_id: str):
        if partner_id in self.partners:
            del self.partners[partner_id]

    def get_location(self, partner_id: str) -> str:
        return f"Location of partner {partner_id}"

