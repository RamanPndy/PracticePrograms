# Define a TripPartnerFinder Implementation
from typing import List
from systemdesign.delivery_management.factory import DeliveryFactory, PartnerAssignerFactory
from systemdesign.delivery_management.impl import DeliveryManager, PartnerTracker
from systemdesign.delivery_management.interface import ITripPartnerFinder

'''
Singleton Pattern for Delivery Manager
Strategy Pattern for Partner Assignment
Observer Pattern for Real-Time Tracking
Factory Pattern for Creating Instances
'''

class TripPartnerFinder(ITripPartnerFinder):
    def find_free_partners(self) -> List[str]:
        return ["partner1", "partner2", "partner3"]

# Create Delivery Manager instance
delivery_manager = DeliveryManager.get_instance()

# Create a Delivery
DeliveryFactory.create_delivery("delivery1", {"details": "Sample Delivery"})

# Set Partner Assigner
trip_partner_finder = TripPartnerFinder()
partner_assigner = PartnerAssignerFactory.create_partner_assigner("random", trip_partner_finder)
delivery_manager.partner_assigner = partner_assigner

# Set Tracker
tracker = PartnerTracker()
delivery_manager.tracker = tracker

# Assign Partner and Track
delivery_manager.assign_partner("delivery1")

# Get Partner Location
print(tracker.get_location("partner1"))
