# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A random agent for starcraft."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy

from pysc2.agents import base_agent
from pysc2.lib import actions
import time

class RandomAgent(base_agent.BaseAgent):
  """A random agent for starcraft."""

  def step(self, obs):
    super(RandomAgent, self).step(obs)
    function_id = numpy.random.choice(obs.observation.available_actions)
    args = [[numpy.random.randint(0, size) for size in arg.sizes]
            for arg in self.action_spec.functions[function_id].args]
    return actions.FunctionCall(function_id, args)


class RandomAgentVerbose(base_agent.BaseAgent):
  """A random agent for starcraft."""
  def __init__(self):
    super().__init__()
    self.restlim = 50
    self.cur_rests = 0
    self.resting = 0


  def step(self, obs):
    super().step(obs)
    function_id = numpy.random.choice(obs.observation.available_actions)
    # function_id = numpy.random.choice([function_id,2])  # hieghten chances of a funciotn id 2.
    function_id = 2

    
    args = [[numpy.random.randint(0, size) for size in arg.sizes]
            for arg in self.action_spec.functions[function_id].args]
    args = [[1],[5,5]]

    if self.resting == 1:
      self.cur_rests += 1
      if self.cur_rests == self.restlim:  #reset rest
        self.cur_rests = 0; self.resting = 0
      function_id = 0
      args = []
    
    # print('dir', dir(obs.observation))
    # print(obs.observation.feature_units)

    # for unit in obs.observation.feature_units:
    #   for k, v in vars(unit)['_index_names'][0].items():
    #     print(k, unit[k])
    #   print('-'*10)
    # print('v'*10)


      # print('VARS', vars(unit))
      # # print(keys(unit))
      # print('DIR',   dir(unit))
      # for x in unit:
      #   print(x)
      # print(unit.x, unit.y, unit.alliance, unit.facing, unit.is_selected, unit.display_type)

    # print('feat_units', obs.observation.feature_units)

    # if function_id < 10:
    #   time.sleep(1.0)
    if len(args) == 2 and len(args[1]) == 2:
      # time.sleep(1.0)
      if function_id == 2:
        # pass
        # time.sleep(4.0)
        self.resting = 1
      else:
        # self.resting = 1
        pass
    print('Did:', function_id, args)
    return actions.FunctionCall(function_id, args)