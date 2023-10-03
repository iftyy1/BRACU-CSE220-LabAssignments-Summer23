class Patient:
    def __init__(self, pat_id, name, age, bg):
        self.pat_id = pat_id
        self.name = name
        self.age = age
        self.bg = bg
        self.next = None
        self.prev = None


class WRM:
    def __init__(self):
        self.head = None
        self.tail = None

    def RegisterPatient(self, pat_id, name, age, bg):
        patient = Patient(pat_id, name, age, bg)

        if self.head is None:
            self.head = patient
            self.tail = patient
        else:
            patient.prev = self.tail
            self.tail.next = patient
            self.tail = patient

    def ServePatient(self):
        if self.head is None:
            print("No patient in waiting")

        print(self.head.name, "is served")
        self.head = self.head.next

    def CancelAll(self):
        self.head = None
        self.tail = None

        print("Doctor can go for lunch")

    def CanDoctorGoHome(self):
        if self.head is None:
            return True
        else:
            return False

    def ShowAllPatient(self):
        if self.head is None:
            print("No patient in waiting")
        curr = self.head

        while curr:
            print("Patient ID:", curr.pat_id)
            curr = curr.next

    def menu(self):
        while True:
            print()
            print("==Waiting Room Management==")
            print("1. Register Patient")
            print("2. Serve Patient")
            print("3. Cancel All")
            print("4. Can Doctor Go Home?")
            print("5. Show All Patient")
            print("6. Exit Menu")
            print("====================")
            print()

            choice = input("Enter your choice (1-6): ")
            print()

            if choice == "1":
                pat_id = input("Enter Patient ID: ")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                bg = input("Enter Blood Group: ")
                print()

                self.RegisterPatient(pat_id, name, age, bg)
                print("Patient Registered")

            if choice == "2":
                self.ServePatient()

            if choice == "3":
                self.CancelAll()

            if choice == "4":
                if self.CanDoctorGoHome() == True:
                    print("Yes")
                else:
                    print("No")

            if choice == "5":
                self.ShowAllPatient()

            if choice == "6":
                break


wrm = WRM()
wrm.menu()
