from pacai.ui import token
from pacai.ui.frame import Frame

class PacmanFrame(Frame):
    # Override
    def _getAgentBaseToken(self, x, y, agentIndex, state):
        if (state.getAgentState(agentIndex).isPacman()):
            return token.PACMAN_1
        else:
            return token.GHOST_1 + (agentIndex - 1) * 100

    # Override
    def _getCapsuleBaseToken(self, x, y, state):
        return token.DEFAULT_FOOD_BASE

    # Override
    def _getFoodBaseToken(self, x, y, state):
        return token.DEFAULT_FOOD_BASE

    # Override
    def _getWallBaseToken(self, x, y, state):
        return token.BLUE_WALL_BASE