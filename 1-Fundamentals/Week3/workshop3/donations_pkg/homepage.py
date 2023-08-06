def show_homepage():
    print("""   
                === DonateMe Homepage ===
              -------------------------------
              |1. Login   |2. Register      |
              -------------------------------
              |3. Donate  |4. Show Donations|
              -------------------------------
              |5. Exit    |6. Show Users    |
              """)


def show_donations(donations):
    print("""\n-------  All Donations  -------""")
    if len(donations) == 0:
      print("There are currently no donations.")
    else:
      for donation in donations:
        print(donation)