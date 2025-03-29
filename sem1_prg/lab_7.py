import csv


def department_with_highest_experience():
    d = {}
    d1 = {}
    l = []
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'r') as file1:
        contents = csv.reader(file1)
        next(contents)
        for content in contents:
            dept = content[2]
            years = int(content[3])
            if dept not in d:
                d[dept] = {"Exp": 0, "count": 0}
            d[dept]["Exp"] += years
            d[dept]["count"] += 1
        print(d)
        for i in d:
            d1[i] = int(d[i]['Exp']) / int(d[i]['count'])
        m = max(d1.values())
        for i in d1:
            if d1[i] == m:
                print(f"{i}: {m}")


# department_with_highest_experience()

def salary_by_age_group():
    d = {'20-30': 0, '31-40': 0, '41-50': 0}
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'r') as file1:
        contents = csv.reader(file1)
        next(contents)
        for content in contents:
            salary = int(content[4])
            if int(content[1]) >= 20 and int(content[1]) <= 30:
                d['20-30'] += salary
            elif int(content[1]) > 30 and int(content[1]) <= 40:
                d['31-40'] += salary
            else:
                d['41-50'] += salary
        print(d)


#salary_by_age_group()


def employees_above_average_salary():
    d = {}
    d1 = {}
    l = []
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'r') as file1:
        contents = csv.reader(file1)
        next(contents)
        for content in contents:
            dept = content[2]
            salary = int(content[4])
            if dept not in d:
                d[dept] = {"Sal": 0, "count": 0}
            d[dept]["Sal"] += salary
            d[dept]["count"] += 1
        print(d)
        for i in d:
            d1[i] = int(d[i]['Sal']) / int(d[i]['count'])
        print(d1)

        with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'r') as file1:
            contents = csv.reader(file1)
            next(contents)
            d2 = {}
            for content in contents:
                name = content[0]
                dept = content[2]
                sal = int(content[4])
                if sal > d1[dept]:
                    print(name)


# employees_above_average_salary()


def give_raises():
    d = {}
    l = []

    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'r') as file1:
        contents = csv.reader(file1)
        next(contents)
        for content in contents:
            l.append(content)
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\employees.csv", 'w', newline="") as file2:
        writer = csv.writer(file2)
        writer.writerow(['Name', 'Age', 'Department', 'Years_of_Experience', 'Salary'])
        for content in l:
            if int(content[3]) > 5:
                content[4] = str(int(content[4]) * 1.1)
        writer.writerows(l)


#give_raises()


def keyword_count():
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\feedback.txt", 'r') as f1:
        l = []
        key = {'excellent': 0, "great": 0, "satisfied": 0, "happy": 0, "poor": 0, "bad": 0, "disappointed": 0,
               "unsatisfied": 0}
        contents = csv.reader(f1)
        str(contents).replace(",", "")
        for content in contents:
            #print(content)
            for i in key:
                if i in str(content):
                    key[i] += 1
        return key


#keyword_count()

def feedback_texts():
    with open(r"C:\Users\shrye\Documents\weeek7[1]\weeek7\feedback.txt", 'r') as f1:
        l1 = ["excellent", "great", "satisfied", "happy"]
        l1_c = 0
        l2_c = 0
        l2 = ["poor", "bad", "disappointed", "unsatisfied"]
        contents = csv.reader(f1)
        str(contents).replace(",", "")
        for content in contents:
            #print(content)
            for i in l1:
                #print("i: ",i)
                if i in str(content):
                    print(content)
                    with open('good_feedback.txt', 'a') as f2:
                        f2.write(f"{str(content)}\n")
                        l1_c += 1
                        break

            for i in l2:
                #print("i: ",i)
                if i in str(content):
                    print(content)
                    with open('bad_feedback.txt', 'a') as f3:
                        f3.write(f"{str(content)}\n")
                        l2_c += 1
                        break
        return (l1_c, l2_c)

    #feedback_texts()


def Summarize_counts():
    with open("keyword_counts.csv", 'w', newline='') as f:
        k = keyword_count()
        writer = csv.writer(f)
        writer.writerow(k)
        (c1, c2) = feedback_texts()
        writer.writerow(str(c1))
        writer.writerow(str(c2))


#Summarize_counts()

def apply_discount(bill_amount):
    is_member = input("Are you a member? (y/n): ")
    if is_member.lower().startswith('y'):
        bill_amount *= 0.95

    is_promo_day = input("Is it a special promotion day? (y/n): ")
    if is_promo_day.lower().startswith('y'):
        bill_amount *= 0.93

    return bill_amount
def add_service_charge(bill_amount):
    dining_option = input("Is this for Dine-in or Takeout? (d/t): ")
    takeout_tax_rate = 5

    if dining_option.lower().startswith('d'):
        bill_amount += 20
    elif dining_option.lower().startswith('t'):
        bill_amount += takeout_tax_rate
    return bill_amount
def calculate_final_bill(initial_amount):
    discounted_amount = apply_discount(initial_amount)
    final_amount = add_service_charge(discounted_amount)
    final_amount += 0.2 * final_amount

    return final_amount

initial_bill_amount = float(input("Enter the initial bill amount: "))
final_bill_amount = calculate_final_bill(initial_bill_amount)
print("Final Bill Amount: ", round(final_bill_amount, 2))





correct_answers = []

with open("week7/output_key.txt", "r") as key_file:
    for line in key_file:
        correct_answers.append(line.strip().split(" "))

student_scores = []

for student_index in range(10):
    student_answers = []
    with open(f"week7/student_{student_index + 1}.txt", "r") as student_file:
        for line in student_file:
            student_answers.append(line.strip().split(" "))

    score = 0
    for question_index in range(10):
        if correct_answers[question_index] == student_answers[question_index]:
            score += 2

    student_scores.append(score)

for student_index in range(10):
    print(f"Student {student_index + 1} got {student_scores[student_index]} marks")


