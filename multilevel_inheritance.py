class ElectronicDevice:
    devices1=["Desktop","Radio","TV","DVD","Speakers","Mikes"]
    def printdetails(self):
        return f"{devices1}"


class PocketGadjet(ElectronicDevice):
    devices2 = ["Earphones","FM","Camera","Phones"]

    def printdetails(self):
        return f"{devices2}"


class Phones(PocketGadjet):
    devices3 = ["Landlines","Tablets","Smartphones"]

    def printdetails(self):
        return f"{devices3}"


ED=ElectronicDevice()
PG=PocketGadjet()
PH=Phones()

print(f"{ED.devices1} {PG.devices2}")
print(f"{PG.devices2} {ED.devices1}")
print(f"{PH.devices3} {PG.devices2} {ED.devices1} ")
