import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor(sensorId):  # noqa: E501
    """Finds Sensor by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param sensorId: ID of sensor to return
    :type sensorId: int

    :rtype: List[Measure]
    """
    return 'do some magic!'
