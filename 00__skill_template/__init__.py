# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'eward'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class GingerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(GingerSkill, self).__init__(name="GingerSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        Lion_intent = IntentBuilder("LionIntent").\
            require("LionKeyword").build()
        self.register_intent(lion_intent, self.handle_Lion_intent)

        Monkey_intent = IntentBuilder("MonkeyIntent").\
            require("MonkeyKeyword").build()
        self.register_intent(monkey_intent,
                             self.handle_monkey_intent)
        
        Bear_intent = IntentBuilder("BearIntent").\
            require("BearKeyword").build()
        self.register_intent(bear_intent,
                             self.handle_bear_intent)

        Dolphin_intent = IntentBuilder("DolphinIntent").\
            require("DolphinKeyword").build()
        self.register_intent(dolphin_intent,
                             self.handle_dolphin_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def monkey_intent(self, message):
        self.speak_dialog("the.monkey.swings.in.the.three")

    def dolphin_intent(self, message):
        self.speak_dialog("the.dolphin.jumps.really.high")
        
    def lion_intent(self, message):
        self.speak_dialog("the lion is going to catch a monkey")

    def bear_intent(self, message):
        self.speak_dialog("the.bear.is.trying.to.eat.honey")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return GingerSkill()
