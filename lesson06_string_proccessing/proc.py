import helper


def task1():
    helper.start_task(1)

    name = "Yehor"
    surname = "Marik"
    age = "12"
    print(f"Hi! My name is {name} {surname}, I am {age} years old.")

    helper.end_task(1)


def task2():
    helper.start_task(2)

    new_line = "\n\n"

    print(f"Baa, baa, black sheep,{new_line}"
          f"Have you any wool?{new_line}"
          f"Yes sir, yes sir,{new_line}"
          f"Three bags full{new_line}\n"
          f"One for the master,{new_line}"
          f"One for the dame,{new_line}"
          f"And one for the little boy{new_line}"
          f"Who lives down the lane{new_line}\n"
          f"Baa, baa, black sheep,{new_line}"
          f"Have you any wool?{new_line}"
          f"Yes sir, yes sir,{new_line}"
          "Three bags full")

    helper.end_task(2)
