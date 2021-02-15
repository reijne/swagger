import connexion
import six

from flask import json

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.service import student_service


def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        # sent_student = Student(first_name=body.first_name, last_name=body.last_name, grades=body.grades)
        db_response = student_service.add_student(body)
        return db_response
    return 405
    # return 'do some magic!'


def get_student_by_id(student_id, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """
    # if connexion.request.is_json:
      # body = Student.from_dict(connexion.request.get_json())  # noqa: E501
      # get_student_by_id(student_id, subject)
    db_response = student_service.get_student_by_id(student_id, subject)

    if (db_response is None):
      return 'student not found', 404
      
    return db_response
    # return 'do some magic!'


def student_student_id_delete(student_id):  # noqa: E501
    """Delete a student by ID

    Delete a single student that is identified by its student_id # noqa: E501

    :param student_id: ID of the student to delete
    :type student_id: int

    :rtype: Student
    """
    db_response = student_service.delete_student(student_id)

    if (db_response is None):
      return 'student not found', 404
      
    return db_response
    # return 'do some magic!'
