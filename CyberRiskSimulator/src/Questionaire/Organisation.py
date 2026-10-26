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


if __name__ == "__main__":
    organisation = Organisation()
    organisation.collect_details()

    print("\nOrganisation Details")
    print("Name:", organisation.name)
    print("Industry:", organisation.industry)
    print("Employees:", organisation.employees)
    