class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.delivered = False

    def deliver(self):
        if not self.delivered:
            self.delivered = True
            print(self.name, "yetkazildi")

    def show_package(self):
        status = "Yetkazildi" if self.delivered else "Yo'lda"
        print(self.name, "-", self.weight, "kg -", status)


class DeliveryService:
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def deliver_all(self):
        for p in self.packages:
            p.deliver()

    def show_packages(self):
        for p in self.packages:
            p.show_package()


def main():
    p1 = Package("Telefon", 1)
    p2 = Package("Laptop", 3)

    service = DeliveryService()

    service.add_package(p1)
    service.add_package(p2)

    service.deliver_all()

    service.show_packages()


main()
