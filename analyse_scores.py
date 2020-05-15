import json
from statistics import mean
import sys


def find_avg_for_all_sub_per_class(students_scores, all_classes):
    """
    analyse students details by class name
    
    :param students_scores: list contains details about students as dictionaries
    :param all_classes: set which contains the class name
    :return: 
    """
    analysed_class_details = []
    stu_avg_for_all_subjects_by_class = []

    for class_name in all_classes:
        class_science = []
        class_literature = []
        class_details_dic = {}
        class_details_list = []

        class_dictionaries = list(filter(lambda a: a['class'] == class_name, students_scores))

        for student in class_dictionaries:
            class_science.append(student['science'])
            class_literature.append(int(student['literature']))
            marks_for_all_subjects = [int(student['math']), student['science'], student['english'],
                                      int(student['literature'])]
            class_details_dic['id'] = student['student_id']
            class_details_dic['avg_all_subjects'] = mean(marks_for_all_subjects)
            class_details_dic['class'] = student['class']
            class_details_list.append(class_details_dic)

        analysed_class_details.append(
            {'class': class_name, 'avg_science': mean(class_science), 'avg_lit': mean(class_literature)})
        stu_avg_for_all_subjects_by_class.append({'class': class_name, 'data': class_details_list})

    while True:
        print("\n\n\t\t\t\t------------------------------Navigation List-----------------------------\n")
        print("\t\t\t\tfind no of classes which are having above 70% average for science >>> Enter 1")
        print("\t\t\t\tfind no of classes which are having above 70% average for literature >>> Enter 2")
        print("\t\t\t\tfind top 3 classes according to average >>> Enter 3")
        print("\t\t\t\tfind the best student of the classes >>> Enter 4")
        print("\t\t\t\tfind no of section heads >>> Enter 5")
        print("\t\t\t\tFinish >>> Enter 6\n")

        key = int(input("Enter your choice : "))
        if key == 1:
            find_class_count_for_avg_science(analysed_class_details)
        elif key == 2:
            find_class_count_for_avg_literature(analysed_class_details)
        elif key == 3:
            select_top_classes(stu_avg_for_all_subjects_by_class, key)
        elif key == 4:
            select_top_classes(stu_avg_for_all_subjects_by_class, key)
        elif key == 5:
            select_top_classes(stu_avg_for_all_subjects_by_class, key)
        elif key == 6:
            sys.exit()


def find_class_count_for_avg_science(class_details):
    """
    function to find the no of classes above average of 70% to science

    :param class_details: list which contains dictionaries consists of student's analysed details
    :return:
    """
    count = 0
    for _class in class_details:
        if _class['avg_science'] >= 70:
            count += 1

    print('No of classes above 70% of average for science : ' + str(count))


def find_class_count_for_avg_literature(class_details):
    """
    function to find the cno of classes above average of 70% to literature

    :param class_details: list which contains dictionaries consists of student's analysed details
    :return:
    """
    count = 0
    for _class in class_details:
        if _class['avg_lit'] >= 70:
            count += 1

    print('No of classes above 70% of average for literature : ' + str(count))


def select_top_classes(stu_avg_for_all_subjects_by_class, key):
    """
    function to find the top 3 classes based on the student who is having the highest average for all subjects

    :param stu_avg_for_all_subjects_by_class: list contains dictionaries contains details of classes
    :param key: user input
    :return:
    """
    classes_max_avg_list = []
    classes_max_list = []
    for dic in stu_avg_for_all_subjects_by_class:
        all_avg_marks = []
        for stu in dic['data']:
            all_avg_marks.append(stu['avg_all_subjects'])

        max_avg = max(all_avg_marks)
        classes_max_list.append(max_avg)
        classes_max_avg_list.append({'class': dic['class'], 'max': max_avg, 'id': stu['id']})
    top_marks = sorted(list(set(classes_max_list)))
    top_marks = top_marks[:3]

    if key == 3:
        print("top 3 classes : ", end=" ")
        for classs in classes_max_avg_list:
            for mark in top_marks:
                if classs['max'] == mark:
                    print(classs['class'] + " ", end=" ")
    elif key == 4:
        get_best_student_per_class(classes_max_avg_list)
    elif key == 5:
        get_no_section_first(classes_max_list)


def get_best_student_per_class(classes_max_avg_list):
    """
    function to display the max averaged student in a class

    :param classes_max_avg_list: list contains dictionaries which consists max average values of each classes
    :return:
    """
    print("class \t\t Id \t\t average \t\t")
    for _class in classes_max_avg_list:
        print(_class['class'] + "\t " + _class['id'] + "\t " + str(_class['max']))


def get_no_section_first(classes_max_list):
    """
    function to get no of section firsts in the section

    :param classes_max_list: list which consists max average values of classes
    :return:
    """
    print("no of section first : " + str(classes_max_list.count(classes_max_list[0])))


if __name__ == '__main__':
    file_name = 'student_scores.json'
    score_data = open(file_name, 'r', encoding='utf-8')
    score_list = json.load(score_data)  # converting to json object

    total_classes_list = []

    for score_student in score_list:
        total_classes_list.append(score_student['class'])

    total_classes = set(total_classes_list)

    find_avg_for_all_sub_per_class(score_list, total_classes)
