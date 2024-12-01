# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.survey_statistics import SurveyStatistics  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatisticsController(BaseTestCase):
    """StatisticsController integration test stubs"""

    def test_statistics_survey_id_get(self):
        """Test case for statistics_survey_id_get

        Obtener estadísticas de una encuesta
        """
        response = self.client.open(
            '/statistics/{survey_id}'.format(survey_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
