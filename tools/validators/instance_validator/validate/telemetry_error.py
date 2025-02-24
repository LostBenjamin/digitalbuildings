# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Container for a telemetry validation error."""

class TelemetryError(object):
  """Container for a telemetry validation error.

  Args:
    entity: name of the entity with the error
    point: name of the point with the error (can be None)
    message: specific error message
  """

  def __init__(self, entity, point, message):
    super().__init__()
    self.entity = entity
    self.point = point
    self.message = message

  def __eq__(self, other):
    if not isinstance(other, TelemetryError):
      return NotImplemented
    return (self.entity == other.entity and
            self.point == other.point and
            self.message == other.message)

  def GetPrintableMessage(self):
    """Returns a human-readable message that explains this error."""

    msg = f'- entity [{self.entity}]'
    if self.point:
      msg += f', point [{self.point}]'
    msg += f': {self.message}\n'

    return msg
