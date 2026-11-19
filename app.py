# app.py
courses = ["B toifasi (Yengil avto)", "A toifasi (Mototsikl)", "C toifasi (Yuk mashinasi)"]
def register_student(name, category):
    print(f"O'quvchi ro'yxatga olindi: {name} - Kurs: {category}")

def list_courses():
    print("Avtomaktab o'quv kurslari:")
    for i, c in enumerate(courses, 1):
        print(f"{i}. {c}")


if __name__ == "__main__":
    list_courses()
    