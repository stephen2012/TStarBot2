"""Adopted from

Zheng Yang's demo_bot.py showing the per-unit-control via raw interface of s2client-proto.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tstarbot.build import DancingDronesMgr
from tstarbot.data.demo_dc import DancingDrones
from tstarbot.act_mgr import ActMgr
from pysc2.agents import base_agent

class DancingDronesAgent(base_agent.BaseAgent):
    """An agent that makes drones dancing.

    Show how to send per-unit-control actions."""

    def __init__(self):
        super(DancingDronesAgent, self).__init__()
        #self.dc = DataContext()
        self.dc = DancingDrones()
        self.am = ActMgr()

        self._mgr = DancingDronesMgr()

    def step(self, timestep):
        super(DancingDronesAgent, self).step(timestep)
        # print(timestep)
        self.dc.update(timestep)
        self._mgr.update(self.dc, self.am)
        return self.am.pop_actions()