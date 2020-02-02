# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_student(self):
        """Test case for add_student

        Add a new student
        """
        body = Student()
        body.first_name = 'Andrea'
        body.last_name = 'Lopez'
        body.grades = {'math': 8, 'history': 9}
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        self.assertTrue(response.is_json)
        self.assertIsInstance(response.json, dict)

    def test_delete_student(self):
        """Test case for delete_student

        
        """
        response = self.client.open(
            '/service-api/pet/{student_id}'.format(student_id=789),
            method='DELETE')
        # self.assert200(response,
        #                'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
