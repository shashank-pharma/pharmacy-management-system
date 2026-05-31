
#day 1
#function 1

def add_drug():
    print("\n--- Add New Drug ---")
    name = input("Drug name: ")
    dose = input("Dose (eg. 500mg): ")
    qty = input("Quantity: ")
    expiry = input("Expiry year: ")

    with open("pharmacy_stock.txt", "a") as f:
        f.write(f"{name},{dose},{qty},{expiry}\n")

    print(f" {name} added successfully!")

#function 2

def view_stock():
    print("\n-----current stocj------")
    print(f"{'drug':<15} {'dose':<10} {'qty':<8} {'expiry'}")
    print("-"*45)

    try:
        with open("pharmacy_stock.txt", "r") as f:
            lines = f.readlines()
            if len(lines)==0:
                print("no drug found")

        for line in lines:
            parts = line.strip().split(",")
            name = parts[0]
            dose = parts[1]
            qty  = parts[2]
            exp  = parts[3]
            print(f"{name:<15} {dose:<10} {qty:<8} {exp}")

    except FileNotFoundError:
        print("No stock file found — add a drug first!")


#function 3

def low_stock():
    print("\n-----low stock------")
    found = False

    try:
        with open("pharmacy_stock.txt",'r')as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                name = parts[0]
                qty = int(parts[2])
                if qty <= 10:
                    print(f"{name} quantity remained : {qty}")
                    found = True

    except FileNotFoundError:
        print("No stock file found")
#day 2

#function 4
def add_patient():
    print("\n-----add new patient----")

    try:
        with open("patient.txt", "r") as f:
            lines = f.readlines()
            patient_id = f"P{str(len(lines)+1).zfill(3)}"

    except FileNotFoundError:
        patient_id = "P001"

    name = input("Patient name: ")
    age = input("Patient age: ")
    gender = input("Patient gender: ")

    with open("pateinrt.txt", "a") as f:
        f.write(f"{patient_id},{name},{age},{gender},\n")

    print(f"Patient {name} added successfully!")
#day 2

#function 5

def view_patient():
    print(f"----PATIENT REPORTS----")
    print(f"{'ID':<8} {'Name':15} {'Age':<6} {'Gender'} ")
    print("-" *40)

    try:
        with open("patient.txt","r")as f:
            lines = f.readlines()
            if len(lines)==0:
                print("No Patient Records found / Empty File")
                return

            for line in lines:
                parts = line.strip().split(",")
                print(f"{parts[0]:<8} {parts[1]:15} {parts[2]:<6} {parts[3]} ")

    except FileNotFoundError:
        print("SUCH FILE NOT EXIST")

#dat 2 

#function 6

def prescribe_drug():
    print(f"\n----PRESCRIBE DRUG----")
    patient_id   = input("Patient ID: ")
    patient_name = input("Patient name: ")
    drug         = input("Drug name: ")
    dose         = input("Dose: ")

    from datetime import date
    today = str(date.today())

    with open("prescription.txt", "a") as f:
        f.write(f"{patient_id},{patient_name},{drug},{dose},{today}\n")

    print(f"Prescription for {patient_name} added successfully!")

# to view prescription

def view_prescription():
    print("\n--- All Prescriptions ---")
    print(f"{'ID':<8} {'Patient':<12} {'Drug':<15} {'Dose':<10} {'Date'}")
    print("-" * 55)

    try:
        with open("prescription.txt","r")as f:
            lines = f.readlines()
            if lines == 0:
                print("No Prescription Records found")
                return
            
            for line in lines:
                parts = line.strip().split(",")
                print(f"{parts[0]:<8} {parts[1]:<12} {parts[2]:<15} {parts[3]:<10} {parts[4]}")

    except FileNotFoundError:
        print(f"NO SUCH FILE EXISTED")

#day 3 
#func 7 record the sales



def rrecord_sales():
    print("\n-----record sales-----")
    drug = input("Enter Drug name : ")
    Qty = int(input("Enter Drug qunatity ; "))
    Price = int(input("Enter the Drug Price : "))
    total = Qty * Price

    from datetime import date
    today = str(date.today())

    with open("sales_log.txt","a") as f:
        f.write(f"{today},{drug},{Qty},{Price},{total}\n")

    print(f"sales record {drug} x {Qty} = {total} added successfully!")


#day 3 
#function 8: view the sales

def view_sales():
    print("\n-----Today's Sales-----")
    
    from datetime import date
    today = str(date.today())

    print(f"{'drug:<15'} {"Qty":<8} {'Amt'}")
    print("-"*35)

    total_revenue = 0
    try:
        with open("sales_log.txt","r") as f:
            lines = f.readlines()
            found = False
            for line in lines:
                parts = line.strip().split(",")
                if parts[0] == today:
                    drug = parts[1]
                    qty = parts[2]
                    amt = int(parts[3])
                    total_revenue += amt
                    print(f"{drug:<15} {qty:<8} {amt}")
                    found = True

            if not found:
                print("No sales for today")

    except FileNotFoundError:
        print("No sales file found")
        return

    print(f"Total Revenue: {total_revenue}")
#day 3 
#function 9: top selling drug

def top_selling():
    print("\n---Top Selling Drugs---")
    drug_count = {}
    try:
        with open("sales_log","r")as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                drug = parts[1]
                qty = int(parts[2])

                if drug in drug_count:
                    drug_count[drug] += qty
                else:
                    drug_count[drug] = qty

        if len(drug_count) == 0:
            print("No sales records found")
            return
        top = max(drug_count, key=drug_count.get)
        print(f"{'Drug':<15} {'Total sold':}")
        print("-"*30)

        for drug,qty in drug_count.items():
            print(f"{drug:<15} {qty}")
        print("-"*30)
        print(f"Top selling drug: {top} with {drug_count[top]} sales")

    except FileNotFoundError:
        print("No sales file found")


# ================================
# PHARMACY MANAGEMENT SYSTEM
# Day 4 — Expiry Checker
# ================================

from datetime import datetime

def add_expiry():
    print("\n--- Add Drug Expiry ---")
    name   = input("Drug name: ")
    dose   = input("Dose: ")
    expiry = input("Expiry date (YYYY-MM): ")

    with open("expiry_data.txt", "a") as f:
        f.write(f"{name},{dose},{expiry}\n")
    print(f" {name} expiry added — {expiry}")

def check_expired():
    print("\n--- Expired Drugs ---")
    today = datetime.now()
    found = False
    try:
        with open("expiry_data.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts  = line.strip().split(",")
                name   = parts[0]
                dose   = parts[1]
                expiry = datetime.strptime(parts[2], "%Y-%m")
                if expiry < today:
                    print(f" {name} ({dose}) — Expired: {parts[2]}")
                    found = True
        if not found:
            print("No expired drugs!")
    except FileNotFoundError:
        print("No expiry file found!")

def expiring_soon():
    print("\n--- Expiring in 6 Months ---")
    today = datetime.now()
    found = False
    try:
        with open("expiry_data.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts       = line.strip().split(",")
                name        = parts[0]
                dose        = parts[1]
                expiry      = datetime.strptime(parts[2], "%Y-%m")
                months_left = (expiry.year - today.year) * 12 + (expiry.month - today.month)
                if 0 <= months_left <= 6:
                    print(f"⚠ {name} ({dose}) — Expires: {parts[2]} ({months_left} months left)")
                    found = True
        if not found:
            print("No drugs expiring soon!")
    except FileNotFoundError:
        print("No expiry file found!")


# ================================
# PHARMACY MANAGEMENT SYSTEM
# Day 5 — Main Menu + Report
# ================================

from datetime import datetime, date

def generate_report():
    print("\n--- Generating Daily Report ---")
    today = str(date.today())

    with open("daily_report.txt", "w") as report:
        report.write("=" * 50 + "\n")
        report.write(f"   PHARMACY DAILY REPORT — {today}\n")
        report.write("=" * 50 + "\n\n")

        # Stock section
        report.write("STOCK STATUS\n")
        report.write("-" * 30 + "\n")
        try:
            with open("pharmacy_stock.txt", "r") as f:
                for line in f:
                    parts  = line.strip().split(",")
                    qty    = int(parts[2])
                    status = "⚠ LOW" if qty < 10 else "✅ OK"
                    report.write(f"{parts[0]:<15} Qty: {parts[2]:<8} {status}\n")
        except FileNotFoundError:
            report.write("No stock data!\n")

        # Sales section
        report.write("\nSALES TODAY\n")
        report.write("-" * 30 + "\n")
        total_revenue = 0
        try:
            with open("sales_log.txt", "r") as f:
                found = False
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == today:
                        report.write(f"{parts[1]:<15} Qty: {parts[2]:<8} ₹{parts[3]}\n")
                        total_revenue += int(parts[3])
                        found = True
                if not found:
                    report.write("No sales today!\n")
        except FileNotFoundError:
            report.write("No sales data!\n")
        report.write(f"Total Revenue: ₹{total_revenue}\n")

        # Expiry section
        report.write("\nEXPIRY ALERTS\n")
        report.write("-" * 30 + "\n")
        now = datetime.now()
        try:
            with open("expiry_data.txt", "r") as f:
                for line in f:
                    parts       = line.strip().split(",")
                    expiry      = datetime.strptime(parts[2], "%Y-%m")
                    months_left = (expiry.year - now.year) * 12 + (expiry.month - now.month)
                    if months_left <= 0:
                        report.write(f"❌ {parts[0]} — EXPIRED!\n")
                    elif months_left <= 6:
                        report.write(f"⚠ {parts[0]} — {months_left} months left\n")
        except FileNotFoundError:
            report.write("No expiry data!\n")

    print("✅ Report saved — daily_report.txt")

def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("   PHARMACY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("  1. Add Drug to Stock")
        print("  2. View Stock")
        print("  3. Low Stock Alert")
        print("  4. Add Patient")
        print("  5. View Patients")
        print("  6. Prescribe Drug")
        print("  7. View Prescriptions")
        print("  8. Record Sale")
        print("  9. View Today's Sales")
        print(" 10. Top Selling Drugs")
        print(" 11. Add Drug Expiry")
        print(" 12. Check Expired Drugs")
        print(" 13. Expiring Soon")
        print(" 14. Generate Daily Report")
        print("  0. Exit")
        print("=" * 40)

        choice = input("Enter choice: ")

        if choice == "1":      add_drug()
        elif choice == "2":    view_stock()
        elif choice == "3":    low_stock()
        elif choice == "4":    add_patient()
        elif choice == "5":    view_patients()
        elif choice == "6":    prescribe_drug()
        elif choice == "7":    view_prescriptions()
        elif choice == "8":    record_sale()
        elif choice == "9":    view_sales()
        elif choice == "10":   top_selling()
        elif choice == "11":   add_expiry()
        elif choice == "12":   check_expired()
        elif choice == "13":   expiring_soon()
        elif choice == "14":   generate_report()
        elif choice == "0":
            print("\n✅ Goodbye! Stay healthy! 💊")
            break
        else:
            print("❌ Invalid choice!")


main_menu()