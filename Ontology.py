import owlready2
from owlready2 import *

owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk-11.0.2\\bin\\java.exe"

onto = get_ontology("http://test.org/onto.owl")

with onto:

    class SubjectThing(Thing):
        namespace = onto

    class Student(SubjectThing):
        namespace = onto


    class SubjectAssociation(Thing):
        namespace = onto


    class Mark(SubjectAssociation):
        namespace = onto


    class InterestPoint(SubjectAssociation):
        namespace = onto


    class Subject(Thing):
        namespace = onto


    class Theme(Thing):
        namespace = onto


    class RequirementThing(Thing):
        namespace = onto


    class EduStandart(SubjectThing):
        namespace = onto


    class Market(Thing):
        namespace = onto


    class Job(RequirementThing):
        namespace = onto


    class Requirement(SubjectAssociation):
        namespace = onto


    class has_name(DataProperty):
        range = [str]


    class has_mark(ObjectProperty):
        domain = [Student]
        range = [Mark]


    class has_interest_point(ObjectProperty):
        domain = [Student]
        range = [InterestPoint]


    class depends_on(Subject >> Subject, TransitiveProperty):
        pass


    class has_subject(ObjectProperty):
        domain = [SubjectThing]
        range = [Subject]


    class related_to_subject(ObjectProperty):
        domain = [SubjectAssociation]
        range = [Subject]


    class include_theme(ObjectProperty):
        domain = [Subject]
        range = [Theme]


    class has_job(ObjectProperty):
        domain = [Market]
        range = [Job]


    class has_requirement(ObjectProperty):
        domain = [RequirementThing]
        range = [Requirement]


subject1 = Subject("DiscreteMath")
subject2 = Subject("LinearAlgebra")
subject3 = Subject("Algorithms", depends_on=[subject1, subject2])
subject4 = Subject("GameDeveloping", depends_on=[subject3])

student = Student("Ruslan")
student.has_subject = [subject1, subject2, subject3]

markMath = Mark("40")
student.has_mark.append(markMath)
markMath.related_to_subject.append(subject1)

markAlgebra = Mark("74")
student.has_mark.append(markAlgebra)
markAlgebra.related_to_subject.append(subject2)

markAlgo = Mark("85")
student.has_mark.append(markAlgo)
markAlgo.related_to_subject.append(subject3)

print(subject3.depends_on)
print(subject4.INDIRECT_depends_on)

print(student.has_subject)
print(subject4.include_theme)
print(student.has_mark)
print(onto.search_one(is_a = onto.Mark,
                      related_to_subject = [subject2]))


onto.save(file = "edu_file")
