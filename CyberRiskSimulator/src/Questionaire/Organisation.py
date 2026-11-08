class Organisation:
    """
    Stores basic information about the organisation.
    """

    def __init__(self):
        self.name = ""
        self.industry = ""
        self.employees = 0

    def collect_details(self):
        print("\n=== Organisation Information ===")

        self.name = input("Organisation Name: ")
        self.industry = input("Industry: ")
        self.employees = int(input("Number of Employees: "))

    def display_details(self):
        print("\n=== Organisation Details ===")
        print(f"Organisation Name: {self.name}")
        print(f"Industry: {self.industry}")
        print(f"Number of Employees: {self.employees}")


if __name__ == "__main__":
    organisation = Organisation()
    organisation.collect_details()
    organisation.display_details()