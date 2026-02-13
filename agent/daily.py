from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context
import logger

@AgentServer.custom_action("InviteAuto")
class InviteAuto(CustomAction):
    def __init__(self):
        # 导入logger
        super().__init__()
        self.logger = logger.get_logger()

    def run(
            self,
            context: Context,
            argv: CustomAction.RunArg,
    ) -> bool:
        """
            遍历日常并进行战斗
        """
