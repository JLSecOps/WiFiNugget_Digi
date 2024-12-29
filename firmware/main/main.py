# Main program entry point
from ai.ai_logic import AILogic
from ai.xp_manager import XPManager
from ai.tasks import complete_task

# Initialize AI and XP system
ai = AILogic()
xp_manager = XPManager()

# Example: Complete tasks
complete_task("scan_networks", xp_manager)
complete_task("deauth_attack", xp_manager)

# Check AI state
ai.gain_xp(xp_manager.xp)
