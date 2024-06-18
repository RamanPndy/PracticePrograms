class UsbCable:
    def __init__(self) -> None:
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True

class UsbPort:
    def __init__(self) -> None:
        self.portAvailable = True
    
    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False

usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)

class MicroUsbCable:
    def __init__(self) -> None:
        self.isPlugged = False
    
    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable) -> None:
        super().__init__()
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()

microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microToUsbAdapter)

'''
Allows the interface of an existing class to be used as another interface.
'''
class EuropeanPlug:
    def plug_in(self):
        return "220V"

class USPlug:
    def connect(self):
        return "110V"

class Adapter:
    def __init__(self, plug):
        self.plug = plug

    def plug_in(self):
        return self.plug.connect()

# Usage
us_plug = USPlug()
adapter = Adapter(us_plug)
print(adapter.plug_in())  # 110V
