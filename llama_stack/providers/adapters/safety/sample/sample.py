# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from .config import SampleConfig


from llama_stack.apis.safety import *  # noqa: F403


class SampleSafetyImpl(Safety):
    def __init__(self, config: SampleConfig):
        self.config = config

    async def initialize(self):
        pass
