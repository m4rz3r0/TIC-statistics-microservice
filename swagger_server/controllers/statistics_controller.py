import connexion
import six

from swagger_server.models.survey_statistics import SurveyStatistics  # noqa: E501
from swagger_server import util


def statistics_survey_id_get(survey_id):  # noqa: E501
    """Obtener estadísticas de una encuesta

    Devuelve estadísticas relacionadas con las respuestas enviadas a una encuesta específica. # noqa: E501

    :param survey_id: ID de la encuesta
    :type survey_id: int

    :rtype: SurveyStatistics
    """
    return 'do some magic!'
