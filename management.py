class Main:
    total_Qty = 0
    total_ammount = 2056
    SL_NO = 0

    def __init__(self):
        self.invoice = {}

    def add(self, Data, truckNumber, Description, Size, UOM, Qty, rate):
        Main.SL_NO += 1
        ammount = rate * Qty
        item = {
            "SL_NO": Main.SL_NO,
            "Data": Data,
            "truckNumber": truckNumber,
            "Description": Description,
            "Size": Size,
            "UOM": UOM,
            "Qty": Qty,
            "rate": rate,
            "ammount": ammount
        }
        self.invoice[Main.SL_NO] = item
        Main.total_ammount += ammount
        Main.total_Qty += Qty

    def calculation(self):
        print(f"Total QTY {Main.total_Qty} and Total amount {Main.total_ammount}")

    def all_data(self):
        if self.invoice!= {}:
            for item in self.invoice.values():
                print(item)
            print()
        else:
            print("Empty")

    def find_by_index(self):
        index = int(input("Give an SL_NO: "))
        if index== True:
            for item in self.invoice.values():
                if index == item["SL_NO"]:
                    print(item)
        else:
            print("Give right data")

    # @staticmethod
    # def number_to_words(number=None):
    #     if number is None:
    #         number = Main.total_ammount
    #
    #     units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    #     teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    #     tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    #
    #     if number == 0:
    #         return "Zero"
    #
    #     words = ""
    #     crore = ["", "Hundred", "Thousand", "Lakh", "Crore"]
    #
    #     i = 0
    #     while number > 0:
    #         part = number % 1000
    #         if part > 0:
    #             if i > 0:
    #                 words = units[part // 100] + " " + crore[i] + " " + words
    #             else:
    #                 words = units[part // 100] + " " + crore[i] + words
    #
    #             if part % 100 != 0:
    #                 if part % 100 < 10:
    #                     words = words + " and " + units[part % 100]
    #                 elif part % 100 < 20:
    #                     words = words + " and " + teens[part % 100 - 10]
    #                 else:
    #                     words = words + " and " + tens[(part % 100) // 10] + " " + units[part % 10]
    #
    #         number //= 1000
    #         i += 1
    #
    #     return words.strip()
    #


def main_menu():
    print("0. All data")
    print("1. Add Invoice Item")
    print("2. View Total Calculation")
    print("3. Not Aviable")
    print("4. Not Aviable")
    print("5. View fixed SL_NO data")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice


if __name__ == "__main__":
    main_instance = Main()  # Create an instance of Main

    while True:
        choice = main_menu()

        if choice == "0":
            main_instance.all_data()
        elif choice == "1":
            data = input("Enter Data: ")
            truck_number = input("Enter Truck Number: ")
            description = input("Enter Description: ")
            size = input("Enter Size: ")
            uom = input("Enter UOM: ")
            qty = float(input("Enter Quantity: "))
            rate = float(input("Enter Rate: "))
            main_instance.add(data, truck_number, description, size, uom, qty, rate)
            print("Invoice item added successfully!")
        elif choice == "2":
            main_instance.calculation()
        # elif choice == "3":
        #     words = main_instance.number_to_words()
        #    print(words)  # Print the words here
        # elif choice == "4":
        #     print("Exiting the program. Goodbye!")
        #     break
        elif choice == "5":
            main_instance.find_by_index()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
