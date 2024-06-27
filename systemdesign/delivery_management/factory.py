from systemdesign.delivery_management.impl import DeliveryManager, RandomPartnerAssigner
from systemdesign.delivery_management.interface import IPartnerAssigner, ITripPartnerFinder


class DeliveryFactory:
    @staticmethod
    def create_delivery(delivery_id: str, details: dict):
        return DeliveryManager.get_instance().create_delivery(delivery_id, details)

class PartnerAssignerFactory:
    @staticmethod
    def create_partner_assigner(assigner_type: str, trip_partner_finder: ITripPartnerFinder) -> IPartnerAssigner:
        if assigner_type == "random":
            return RandomPartnerAssigner(trip_partner_finder)
        else:
            raise ValueError("Unknown partner assigner type")
