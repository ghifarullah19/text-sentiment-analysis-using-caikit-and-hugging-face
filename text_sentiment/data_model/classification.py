# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard
from typing import List

# Local
from caikit.core import DataObjectBase
from caikit.core.data_model import dataobject


@dataobject(package="text_sentiment.data_model")
class ClassInfo(DataObjectBase):
   """A single classification prediction."""

   class_name: str  # (required) Predicted relevant class name
   confidence: float  # (required) The confidence-like score of this prediction in [0, 1]


@dataobject(package="text_sentiment.data_model")
class ClassificationPrediction(DataObjectBase):
   """The result of a classification prediction."""

   classes: List[ClassInfo]


@dataobject(package="text_sentiment.data_model")
class TextInput(DataObjectBase):
   """A sample `domain primitive` input type for this library.
   The analog to a `Raw Document` for the `Natural Language Processing` domain."""

   text: str